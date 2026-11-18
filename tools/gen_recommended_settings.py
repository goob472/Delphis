#!/usr/bin/env python3
"""
generates app/src/main/java/io/github/hiramrg/delphis/core/RecommendedSettingsTable.kt from the
Configuration section ({{Config ...}} template) of every game page on the Dolphin wiki.

    python tools/gen_recommended_settings.py            # fetch the wiki, write the cache, Kotlin and report
    python tools/gen_recommended_settings.py --offline  # rebuild from tools/wiki_config_cache.json only

Reads raw wikitext through the MediaWiki API (no HTML scraping) and never runs at app runtime.
Only settings that fix emulation bugs are kept (see MAPPINGS and EXCLUDED below); everything else,
and anything whose value can't be read with confidence, is skipped and listed in
tools/recommended_settings_report.md.

Template parameter names and labels: https://wiki.dolphin-emu.org/index.php?title=Template:Config
INI section/key names: Dolphin Source/Core/Core/Config/GraphicsSettings.cpp, MainSettings.cpp, and
ConfigLoaders/GameConfigLoader.cpp (GameSettings [Video_Hacks] = GFX "Hacks", [Video_Settings] =
GFX "Settings", [Video_Enhancements] = GFX "Enhancements", [Core] = Main "Core").
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://wiki.dolphin-emu.org/api.php"
UA = "delphis-recommended-settings-generator/1.0 (+https://github.com/HiramRG/Delphis)"
ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "tools" / "wiki_config_cache.json"
REPORT = ROOT / "tools" / "recommended_settings_report.md"
KOTLIN = ROOT / "app/src/main/java/io/github/hiramrg/delphis/core/RecommendedSettingsTable.kt"

ON = {"on", "enabled", "enable", "true", "yes", "checked"}
OFF = {"off", "disabled", "disable", "false", "no", "unchecked"}


def boolean(invert=False, only=None):
    """On/Off parameter -> 'True'/'False' (inverted for 'Skip…'/'Ignore…'/'Disable…' labels).
    [only] keeps just that wiki value (e.g. 'off' for enhancements, where only turning it off fixes bugs)."""
    def parse(v):
        v = v.lower()
        if v in ON:
            on = True
        elif v in OFF:
            on = False
        else:
            return None
        if only is not None and on != (only == "on"):
            return "skip:enhancement turned on (not a bug fix)"
        return "True" if on != invert else "False"
    return parse


def dsp(v):
    v = v.lower()
    if v.startswith("lle"):
        return "False"
    if v.startswith("hle"):
        return "True"
    return None


def texcache(v):
    # Dolphin's slider: Safe = 0 samples, Medium = 512, Fast = 128 (VideoCommon/ … GraphicsSettings).
    v = v.lower()
    if "safe" in v or "position 1" in v or v in {"left", "1"}:
        return "0"
    if "medium" in v or "position 2" in v or v in {"middle", "2"}:
        return "512"
    if "fast" in v or "position 3" in v or v in {"right", "3"}:
        return "128"
    return None


# wiki parameter -> (label shown on the wiki, INI section, INI key, value parser)
MAPPINGS = {
    # General / Game Properties (Main "Core")
    "dualcore": ("Enable Dual Core", "Core", "CPUThread", boolean()),
    "syncgputhread": ("Synchronize GPU Thread", "Core", "SyncGPU", boolean()),
    "mmu": ("Enable MMU", "Core", "MMU", boolean()),
    "fprf": ("Enable FPRF", "Core", "FPRF", boolean()),
    "dspengine": ("DSP Emulator Engine", "Core", "DSPHLE", dsp),
    # Graphics hacks (GFX "Hacks" -> [Video_Hacks])
    "skipcpuefbaccess": ("Skip EFB Access from CPU", "Video_Hacks", "EFBAccessEnable", boolean(invert=True)),
    "formatchanges": ("Ignore Format Changes", "Video_Hacks", "EFBEmulateFormatChanges", boolean(invert=True)),
    "efb2texonly": ("Store EFB Copies to Texture Only", "Video_Hacks", "EFBToTextureEnable", boolean()),
    "deferefb": ("Defer EFB Copies to RAM", "Video_Hacks", "DeferEFBCopies", boolean()),
    "xfb2texonly": ("Store XFB Copies to Texture Only", "Video_Hacks", "XFBToTextureEnable", boolean()),
    "xfbimmediate": ("Immediately Present XFB", "Video_Hacks", "ImmediateXFBEnable", boolean()),
    "boundingbox": ("Disable Bounding Box", "Video_Hacks", "BBoxEnable", boolean(invert=True)),
    "vertexrounding": ("Vertex Rounding Hack", "Video_Hacks", "VertexRounding", boolean()),
    "manualtexturesampling": ("Manual Texture Sampling", "Video_Hacks", "FastTextureSampling", boolean(invert=True)),
    "efbscaledcopy": ("Scaled EFB Copy", "Video_Hacks", "EFBScaledCopy", boolean(only="off")),
    # GFX "Settings" -> [Video_Settings]
    "accuratetexturecache": ("Texture Cache Accuracy", "Video_Settings", "SafeTextureCacheColorSamples", texcache),
    "fastdepth": ("Fast Depth Calculation", "Video_Settings", "FastDepthCalc", boolean()),
    # Enhancements: only "Off" is a fix (On is a cosmetic upgrade).
    "force24bit": ("Force 24-Bit Color", "Video_Enhancements", "ForceTrueColor", boolean(only="off")),
    "arbmipmap": ("Arbitrary Mipmap Detection", "Video_Enhancements", "ArbitraryMipmapDetection", boolean(only="off")),
}

# Parameters left out on purpose, with the reason that goes into the report.
EXCLUDED = {
    "speedlimit": "performance/preference", "ntscj": "region/console setting, not a per-game fix",
    "panichandlers": "PC-only UI", "skipbios": "boot preference", "cpuengine": "CPU core choice (JIT vs interpreter is a huge speed cost on Android; not mapped)",
    "cpuclock": "CPU clock override (performance tweak)", "gfxbackend": "backend choice (PC-only / device-specific)",
    "fullres": "PC-only display", "aspectratio": "Delphis' Screen setting owns aspect ratio", "vsync": "PC-only display",
    "startfull": "PC-only UI", "rendertomain": "PC-only UI", "shadercomp": "performance (shader compilation mode)",
    "compilefirst": "performance (shader precompile)", "internalres": "resolution", "antialiasing": "enhancement",
    "pixellighting": "enhancement", "forcetexturefiltering": "enhancement", "widescreenhack": "Delphis' Screen setting owns widescreen",
    "disablefog": "enhancement", "gputexdecode": "performance", "crop": "display preference", "progressivescan": "SYSCONF, not a GameSettings key",
    "vbiskip": "performance", "audiobackend": "PC-only", "pal60": "SYSCONF", "screensaver": "SYSCONF", "sdcard": "Wii setting, not a bug fix",
    "usbkeyboard": "Wii peripheral", "systemlang": "SYSCONF language", "enablespeakerdata": "real Wii Remote only", "wiimotemotor": "real Wii Remote only",
    "fastdisc": "load-speed tweak", "patches": "free text, not a setting",
}

# Notes that tie a value to a desktop backend/OS: the fix may not apply on Android, so skip.
PC_ONLY_NOTE = re.compile(r"\b(d3d|direct3d|dx1[12]|metal|macos|mac os|windows|nvidia|amd|intel)\b", re.I)


def api(params):
    params = dict(params, format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body = r.read().decode("utf-8")
            if body.lstrip().startswith("<"):
                sys.exit("The wiki returned HTML instead of JSON (bot check?). Stopping; see the script header.")
            return json.loads(body)
        except (OSError, json.JSONDecodeError) as e:
            if attempt == 4:
                raise
            print(f"  retry after {e}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))


def query_all(params):
    """Runs a query, following 'continue'; yields each response."""
    cont = {}
    while True:
        data = api(dict(params, **cont))
        yield data
        if "continue" not in data:
            return
        cont = data["continue"]
        time.sleep(0.5)


def fetch():
    titles = []
    for d in query_all({"action": "query", "list": "embeddedin", "eititle": "Template:Config", "einamespace": "0", "eilimit": "max"}):
        titles += [p["title"] for p in d["query"]["embeddedin"]]
    titles = sorted(set(titles))
    print(f"{len(titles)} pages use Template:Config", file=sys.stderr)
    pages = {}
    for i in range(0, len(titles), 50):
        batch = titles[i:i + 50]
        for d in query_all({"action": "query", "prop": "revisions", "rvprop": "content|ids", "rvslots": "main", "titles": "|".join(batch)}):
            for p in d["query"].get("pages", []):
                if "revisions" in p:
                    rev = p["revisions"][0]
                    pages.setdefault(p["title"], {})["wikitext"] = rev["slots"]["main"]["content"]
                    pages[p["title"]]["revid"] = rev["revid"]
        for d in query_all({"action": "query", "prop": "redirects", "rdlimit": "max", "rdnamespace": "0", "titles": "|".join(batch)}):
            for p in d["query"].get("pages", []):
                pages.setdefault(p["title"], {}).setdefault("redirects", []).extend(r["title"] for r in p.get("redirects", []))
        print(f"  {min(i + 50, len(titles))}/{len(titles)}", file=sys.stderr)
        time.sleep(1)
    return pages


GAME_ID = re.compile(r"^[A-Z0-9]{3}[A-Z][A-Z0-9]{2}$")


def game_ids(redirects):
    return sorted({r for r in redirects if GAME_ID.match(r) and any(c.isdigit() for c in r)})


def config_block(wikitext):
    """Body of the first {{Config ...}} template, matching nested braces."""
    m = re.search(r"\{\{\s*Config\s*\|", wikitext)
    if not m:
        return None
    depth, i = 0, m.start()
    while i < len(wikitext):
        if wikitext.startswith("{{", i):
            depth += 1; i += 2; continue
        if wikitext.startswith("}}", i):
            depth -= 1; i += 2
            if depth == 0:
                return wikitext[m.end():i - 2]
            continue
        i += 1
    return None


def split_params(body):
    """Splits template parameters on top-level '|' only."""
    parts, depth, cur, i = [], 0, [], 0
    while i < len(body):
        two = body[i:i + 2]
        if two in ("{{", "[["):
            depth += 1; cur.append(two); i += 2; continue
        if two in ("}}", "]]"):
            depth -= 1; cur.append(two); i += 2; continue
        if body[i] == "|" and depth == 0:
            parts.append("".join(cur)); cur = []; i += 1; continue
        cur.append(body[i]); i += 1
    parts.append("".join(cur))
    out = {}
    for p in parts:
        if "=" in p:
            k, v = p.split("=", 1)
            out[k.strip().lower()] = v
    return out


def clean(v):
    v = re.sub(r"<!--.*?-->", "", v, flags=re.S)
    v = re.sub(r"<ref[^>]*/>|<ref[^>]*>.*?</ref>", "", v, flags=re.S | re.I)
    v = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", v)       # [[link|text]] -> text
    v = re.sub(r"\[https?://\S+\s+([^\]]*)\]", r"\1", v)         # [url text] -> text
    v = re.sub(r"'{2,}", "", v)
    v = re.sub(r"<[^>]+>", " ", v)
    return " ".join(v.split()).strip()


def kt(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("$", "\\$") + '"'


def build(pages):
    included, skipped, id_owner = [], [], {}
    games = []  # (title, ids, settings)
    for title in sorted(pages):
        page = pages[title]
        body = config_block(page.get("wikitext", ""))
        if body is None:
            continue
        params = split_params(body)
        ids = game_ids(page.get("redirects", []))
        settings = []
        for name, raw in params.items():
            if name.endswith("notes"):
                continue
            value = clean(raw)
            if not value:
                continue
            note = clean(params.get(name + "notes", ""))
            if name in EXCLUDED:
                skipped.append((title, name, value, EXCLUDED[name])); continue
            if name not in MAPPINGS:
                skipped.append((title, name, value, "unknown/deprecated parameter")); continue
            label, section, key, parse = MAPPINGS[name]
            if PC_ONLY_NOTE.search(note) or PC_ONLY_NOTE.search(value):
                skipped.append((title, name, value, f"desktop backend/OS-specific ({note[:60]})")); continue
            ini = parse(value)
            if ini is None:
                skipped.append((title, name, value, "value not recognised")); continue
            if ini.startswith("skip:"):
                skipped.append((title, name, value, ini[5:])); continue
            settings.append((section, key, ini, label, value, note))
            included.append((title, label, value, f"[{section}] {key} = {ini}", note))
        if not settings:
            continue
        if not ids:
            skipped.append((title, "*", "", "no game ID redirects on the wiki")); continue
        games.append((title, ids, settings))
        for gid in ids:
            id_owner.setdefault(gid, []).append(title)

    # 3-character prefix fallback (e.g. G4Q for a revision/region the wiki doesn't list), only
    # when every known ID with that prefix belongs to the same page.
    prefix_owner = {}
    for title, ids, _ in games:
        for gid in ids:
            prefix_owner.setdefault(gid[:3], set()).add(title)
    return games, included, skipped, {p for p, t in prefix_owner.items() if len(t) == 1}, id_owner


def write_kotlin(games, prefixes, stamp):
    lines = [
        "package io.github.hiramrg.delphis.core",
        "",
        "// GENERATED by tools/gen_recommended_settings.py on " + stamp + " — do not edit by hand.",
        "// Source: the Configuration section ({{Config}} template) of each game page on the Dolphin wiki",
        "// (https://wiki.dolphin-emu.org), read as raw wikitext through the MediaWiki API. Only bug-fix settings",
        "// are kept; tools/recommended_settings_report.md lists what was included and skipped, and why.",
        "// Regenerate: python tools/gen_recommended_settings.py   (or --offline to rebuild from the cache).",
        "",
        "/** The wiki's recommended Dolphin settings per game, as GameSettings/<ID>.ini lines. */",
        "object RecommendedSettingsTable {",
        "    data class Setting(val section: String, val key: String, val value: String, val label: String, val wikiValue: String, val note: String)",
        "    data class Game(val title: String, val settings: List<Setting>)",
        "",
        "    fun forGame(gameId: String?): Game? {",
        "        if (gameId == null) return null",
        "        val i = IDS[gameId] ?: IDS[gameId.take(4)] ?: IDS[gameId.take(3)] ?: return null",
        "        return GAMES[i]",
        "    }",
        "",
        "    private fun s(section: String, key: String, value: String, label: String, wikiValue: String, note: String) =",
        "        Setting(section, key, value, label, wikiValue, note)",
        "",
        "    private val GAMES: List<Game> = listOf(",
    ]
    index = {}
    for n, (title, ids, settings) in enumerate(games):
        lines.append(f"        Game({kt(title)}, listOf( // {n}")
        for (section, key, ini, label, value, note) in settings:
            lines.append(f"            s({kt(section)}, {kt(key)}, {kt(ini)}, {kt(label)}, {kt(value)}, {kt(note)}),")
        lines.append("        )),")
        for gid in ids:
            index[gid] = n
            if gid[:3] in prefixes:
                index.setdefault(gid[:3], n)
    lines += ["    )", "", "    private val IDS: Map<String, Int> = mapOf("]
    for gid in sorted(index):
        lines.append(f"        {kt(gid)} to {index[gid]},")
    lines += ["    )", "}", ""]
    KOTLIN.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return len(index)


def write_report(games, included, skipped, n_pages, n_keys, stamp):
    from collections import Counter
    out = [f"# Recommended settings from the Dolphin wiki", "", f"Generated {stamp} by `tools/gen_recommended_settings.py`.", "",
           f"- Wiki pages with a Configuration template: {n_pages}",
           f"- Games with at least one bug-fix setting: {len(games)} ({n_keys} lookup keys incl. 3-letter prefixes)",
           f"- Settings included: {len(included)}",
           f"- Settings skipped: {len(skipped)}", "",
           "## Included, by setting", ""]
    for (label, ini), c in Counter((l, i.split(' = ')[0]) for _, l, _, i, _ in included).most_common():
        out.append(f"- {label} → `{ini}`: {c}")
    out += ["", "## Skipped, by reason", ""]
    reasons = Counter((name, why if not why.startswith("desktop") else "desktop backend/OS-specific note") for _, name, _, why in skipped)
    for (name, why), c in sorted(reasons.items(), key=lambda x: -x[1]):
        out.append(f"- `{name}`: {why} ({c})")
    out += ["", "## Values not recognised (review by hand)", ""]
    for title, name, value, why in skipped:
        if why == "value not recognised":
            out.append(f"- {title}: `{name}` = {value!r}")
    out += ["", "## Every included setting", "", "| Game | Wiki setting | Wiki value | INI | Wiki note |", "|---|---|---|---|---|"]
    for title, label, value, ini, note in included:
        out.append(f"| {title} | {label} | {value} | `{ini}` | {note.replace('|', '/')} |")
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="use tools/wiki_config_cache.json instead of the wiki")
    a = ap.parse_args()
    if a.offline:
        cache = json.loads(CACHE.read_text(encoding="utf-8"))
    else:
        cache = {"fetched": time.strftime("%Y-%m-%d"), "pages": fetch()}
        # Keep only the Configuration template in the cache (small, diffable, no other wiki prose).
        slim = {}
        for t, p in cache["pages"].items():
            body = config_block(p.get("wikitext", ""))
            slim[t] = {"revid": p.get("revid"), "redirects": sorted(set(p.get("redirects", []))),
                       "wikitext": "{{Config|" + body + "}}" if body is not None else ""}
        cache["pages"] = slim
        CACHE.write_text(json.dumps(cache, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    games, included, skipped, prefixes, _ = build(cache["pages"])
    n_keys = write_kotlin(games, prefixes, "wiki fetched " + cache["fetched"])
    write_report(games, included, skipped, sum(1 for p in cache["pages"].values() if p.get("wikitext")), n_keys, cache["fetched"])
    print(f"{len(games)} games, {len(included)} settings included, {len(skipped)} skipped -> {KOTLIN.relative_to(ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    main()
