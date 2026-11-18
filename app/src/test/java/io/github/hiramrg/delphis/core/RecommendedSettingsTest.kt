package io.github.hiramrg.delphis.core

import io.github.hiramrg.delphis.core.RecommendedSettingsTable.Setting
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class RecommendedSettingsTest {
    private val xfb = Setting("Video_Hacks", "XFBToTextureEnable", "False", "Store XFB Copies to Texture Only", "Off", "")

    @Test
    fun strikersGetsXfbToTextureOffInEveryRegion() {
        for (id in listOf("G4QE01", "G4QP01", "G4QJ01")) {
            val s = RecommendedSettings.forGame(id)
            assertTrue(id, s.any { it.section == "Video_Hacks" && it.key == "XFBToTextureEnable" && it.value == "False" })
        }
        val ini = RecommendedSettings.apply("", RecommendedSettings.forGame("G4QE01")).ini
        assertEquals("False", IniEditor(ini).get("Video_Hacks", "XFBToTextureEnable"))
    }

    @Test
    fun prefixFallbackFindsAnUnlistedRevisionOfTheSameGame() {
        // G4QD01 isn't on the wiki; every G4Q… ID belongs to Super Mario Strikers, so the prefix finds it.
        assertEquals("Super Mario Strikers", RecommendedSettingsTable.forGame("G4QD01")?.title)
        assertNotNull(RecommendedSettingsTable.forGame("G4Q"))
        assertNull(RecommendedSettingsTable.forGame("ZZZE99"))
        assertTrue(RecommendedSettings.forGame(null).isEmpty())
    }

    @Test
    fun playersOwnLinesSurvive() {
        val existing = """
            [Controls]
            PadProfile1 = Delphis GameCube

            [Video_Settings]
            AspectRatio = 1

            [Video_Hacks]
            EFBToTextureEnable = False
        """.trimIndent() + "\n"
        val r = RecommendedSettings.apply(existing, listOf(xfb))
        val e = IniEditor(r.ini)
        assertEquals("Delphis GameCube", e.get("Controls", "PadProfile1"))
        assertEquals("1", e.get("Video_Settings", "AspectRatio"))
        assertEquals("False", e.get("Video_Hacks", "EFBToTextureEnable"))
        assertEquals("False", e.get("Video_Hacks", "XFBToTextureEnable"))
        assertEquals(listOf(xfb), r.applied)
    }

    @Test
    fun aKeyThePlayerSetDifferentlyIsKept() {
        val existing = "[Video_Hacks]\nXFBToTextureEnable = True\n"
        val r = RecommendedSettings.apply(existing, listOf(xfb))
        assertEquals(existing, r.ini)
        assertEquals(listOf(xfb to "True"), r.keptPlayer)
        assertTrue(r.applied.isEmpty())
    }

    @Test
    fun turningOffRemovesOnlyDelphisKeys() {
        val existing = "[Controls]\nPadProfile1 = Delphis GameCube\n\n[Video_Hacks]\nEFBToTextureEnable = False\n"
        val on = RecommendedSettings.apply(existing, listOf(xfb)).ini
        assertTrue(on.contains(RecommendedSettings.MARK_PREFIX))
        val off = RecommendedSettings.revert(on)
        assertEquals(existing, off)
        // Applying twice changes nothing.
        assertEquals(on, RecommendedSettings.apply(on, listOf(xfb)).ini)
    }

    @Test
    fun revertLeavesAValueThePlayerChangedAfterDelphis() {
        val on = RecommendedSettings.apply("", listOf(xfb)).ini
        // The player flips the key itself in Dolphin (Delphis' marker comment stays as it was).
        val changed = on.lines().joinToString("\n") { if (it == "XFBToTextureEnable = False") "XFBToTextureEnable = True" else it }
        assertTrue(changed.contains(RecommendedSettings.MARK_PREFIX + "XFBToTextureEnable = False"))
        val off = RecommendedSettings.revert(changed)
        assertEquals("True", IniEditor(off).get("Video_Hacks", "XFBToTextureEnable"))
        assertFalse(off.contains(RecommendedSettings.MARK_PREFIX))
        // On again: the player's value stays and the stale marker goes.
        val again = RecommendedSettings.apply(changed, listOf(xfb))
        assertEquals("True", IniEditor(again.ini).get("Video_Hacks", "XFBToTextureEnable"))
        assertFalse(again.ini.contains(RecommendedSettings.MARK_PREFIX))
    }

    @Test
    fun aRecommendationDroppedFromTheTableIsTakenOut() {
        val on = RecommendedSettings.apply("[Core]\nCPUThread = True\n", listOf(xfb)).ini
        val r = RecommendedSettings.apply(on, emptyList())
        assertEquals("[Core]\nCPUThread = True\n", r.ini)
    }

    @Test
    fun revertWithoutDelphisKeysIsANoOp() {
        val ini = "[Video_Hacks]\nXFBToTextureEnable = False\n"
        assertEquals(ini, RecommendedSettings.revert(ini))
    }
}
