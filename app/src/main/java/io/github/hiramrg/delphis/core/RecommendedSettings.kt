package io.github.hiramrg.delphis.core

import io.github.hiramrg.delphis.core.RecommendedSettingsTable.Setting

/**
 * "Recommended settings": the bug-fix settings the Dolphin wiki lists for a game (its Configuration
 * table, bundled as [RecommendedSettingsTable]), written into GameSettings/<id>.ini when the game starts.
 *
 * Every line the player (or Dolphin's own per-game screen) wrote stays as it is:
 *  - a key that isn't set yet gets the wiki's value, plus a marker comment in the same section
 *    (`# Delphis: recommended <key> = <value>`) so Delphis knows the key is its own;
 *  - a key already set to another value without Delphis' marker is the player's: it's kept;
 *  - a key Delphis set but the player changed since is the player's from then on (marker dropped).
 * Turning the feature off ([revert]) removes only keys that still carry Delphis' marker and value.
 */
object RecommendedSettings {
    const val MARK_PREFIX = "# Delphis: recommended "

    fun forGame(gameId: String?): List<Setting> = RecommendedSettingsTable.forGame(gameId)?.settings.orEmpty()

    data class Result(
        val ini: String,
        /** Settings now in effect from the wiki (written now or earlier by Delphis, or already set the same). */
        val applied: List<Setting>,
        /** Settings left alone because the game's file already sets them differently: setting → current value. */
        val keptPlayer: List<Pair<Setting, String>>,
    )

    private fun mark(key: String, value: String) = "$MARK_PREFIX$key = $value"

    /** Delphis' markers in [section]: key → value Delphis wrote. */
    private fun marks(ed: IniEditor, section: String): Map<String, String> = ed.lines(section)
        .map { it.trim() }.filter { it.startsWith(MARK_PREFIX) }
        .associate { it.removePrefix(MARK_PREFIX).substringBefore('=').trim() to it.substringAfter('=').trim() }

    /** Writes [settings] into [existing] (see the class comment), and undoes Delphis' keys no longer recommended. */
    fun apply(existing: String, settings: List<Setting>): Result {
        val ed = IniEditor(existing)
        val applied = mutableListOf<Setting>()
        val kept = mutableListOf<Pair<Setting, String>>()
        for (s in settings) {
            val current = ed.get(s.section, s.key)
            val ours = marks(ed, s.section)[s.key]
            when {
                current == null -> {
                    ours?.let { ed.removeLine(s.section, mark(s.key, it)) }
                    ed.set(s.section, mapOf(s.key to s.value)); ed.addLine(s.section, mark(s.key, s.value)); applied += s
                }
                current == s.value -> applied += s // Delphis' (marked) or already the player's choice: either way in effect.
                ours != null && current == ours -> {
                    // Delphis wrote an older recommendation; the wiki changed it since.
                    ed.removeLine(s.section, mark(s.key, ours))
                    ed.set(s.section, mapOf(s.key to s.value)); ed.addLine(s.section, mark(s.key, s.value)); applied += s
                }
                else -> {
                    // The player's own value wins; a stale marker (player changed Delphis' value) goes.
                    ours?.let { ed.removeLine(s.section, mark(s.key, it)) }
                    kept += s to current
                }
            }
        }
        // Keys Delphis wrote that the table no longer recommends for this game.
        val wanted = settings.map { it.section to it.key }.toSet()
        for (section in ed.sections()) for ((key, value) in marks(ed, section)) {
            if ((section to key) !in wanted) revertKey(ed, section, key, value)
        }
        return Result(ed.toString(), applied, kept)
    }

    /** Removes every key Delphis wrote (still at Delphis' value) and all of Delphis' markers; nothing else. */
    fun revert(existing: String): String {
        if (!existing.contains(MARK_PREFIX)) return existing
        val ed = IniEditor(existing)
        for (section in ed.sections()) for ((key, value) in marks(ed, section)) revertKey(ed, section, key, value)
        return ed.toString()
    }

    private fun revertKey(ed: IniEditor, section: String, key: String, value: String) {
        if (ed.get(section, key) == value) ed.remove(section, key)
        ed.removeLine(section, mark(key, value))
        ed.removeSectionIfEmpty(section)
    }

    /** "Store XFB Copies to Texture Only: Off" — the wiki's own wording, for the game page. */
    fun label(s: Setting) = "${s.label}: ${s.wikiValue}"
}
