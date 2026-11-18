# Recommended settings from the Dolphin wiki

Generated 2026-11-18 by `tools/gen_recommended_settings.py`.

- Wiki pages with a Configuration template: 329
- Games with at least one bug-fix setting: 252 (990 lookup keys incl. 3-letter prefixes)
- Settings included: 322
- Settings skipped: 117

## Included, by setting

- Texture Cache Accuracy → `[Video_Settings] SafeTextureCacheColorSamples`: 100
- Store EFB Copies to Texture Only → `[Video_Hacks] EFBToTextureEnable`: 74
- Manual Texture Sampling → `[Video_Hacks] FastTextureSampling`: 67
- Enable Dual Core → `[Core] CPUThread`: 16
- Store XFB Copies to Texture Only → `[Video_Hacks] XFBToTextureEnable`: 14
- Immediately Present XFB → `[Video_Hacks] ImmediateXFBEnable`: 11
- Defer EFB Copies to RAM → `[Video_Hacks] DeferEFBCopies`: 7
- Skip EFB Access from CPU → `[Video_Hacks] EFBAccessEnable`: 7
- Vertex Rounding Hack → `[Video_Hacks] VertexRounding`: 5
- Enable MMU → `[Core] MMU`: 4
- Force 24-Bit Color → `[Video_Enhancements] ForceTrueColor`: 4
- Synchronize GPU Thread → `[Core] SyncGPU`: 4
- Scaled EFB Copy → `[Video_Hacks] EFBScaledCopy`: 3
- Ignore Format Changes → `[Video_Hacks] EFBEmulateFormatChanges`: 2
- Fast Depth Calculation → `[Video_Settings] FastDepthCalc`: 2
- DSP Emulator Engine → `[Core] DSPHLE`: 2

## Skipped, by reason

- `forcetexturefiltering`: enhancement (26)
- `*`: no game ID redirects on the wiki (25)
- `antialiasing`: enhancement (10)
- `gfxbackend`: backend choice (PC-only / device-specific) (8)
- `cpuclock`: CPU clock override (performance tweak) (7)
- `aspectratio`: Delphis' Screen setting owns aspect ratio (6)
- `internalres`: resolution (5)
- `panichandlers`: PC-only UI (4)
- `progressivescan`: SYSCONF, not a GameSettings key (4)
- `skipbios`: boot preference (3)
- `shadercomp`: performance (shader compilation mode) (3)
- `enablespeakerdata`: real Wii Remote only (3)
- `cpuengine`: CPU core choice (JIT vs interpreter is a huge speed cost on Android; not mapped) (2)
- `patches`: free text, not a setting (2)
- `fastdepth`: desktop backend/OS-specific note (2)
- `pixellighting`: enhancement (2)
- `vbiskip`: performance (2)
- `type`: unknown/deprecated parameter (1)
- `ntscj`: region/console setting, not a per-game fix (1)
- `fastdisc`: load-speed tweak (1)

## Values not recognised (review by hand)


## Every included setting

| Game | Wiki setting | Wiki value | INI | Wiki note |
|---|---|---|---|---|
| 007: Agent Under Fire | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| 007: From Russia with Love | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Render bloom |
| 007: From Russia with Love | Defer EFB Copies to RAM | Off | `[Video_Hacks] DeferEFBCopies = False` | Layer bloom correctly |
| 007: From Russia with Love | Vertex Rounding Hack | On | `[Video_Hacks] VertexRounding = True` | Correct odd lines at higher than native resolution |
| 007: From Russia with Love | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| 007: Nightfire | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Advance Game Port | Enable MMU | Off | `[Core] MMU = False` | Fix hang when selecting menu items |
| America's Next Top Model | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Avoid makeup facial texture errors |
| American Chopper 2: Full Throttle | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Avoid purple frames between video clips |
| Arkanoid Plus! | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fix invulnerable boss issue |
| Assault | Store EFB Copies to Texture Only | On | `[Video_Hacks] EFBToTextureEnable = True` | Corrects for for green rectangle partially covering screen |
| BMX XXX | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Rider Editor Rider Style options |
| Baroque | Enable Dual Core | Off | `[Core] CPUThread = False` | Correct fog problems |
| Batman Vengeance | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Render videos /wo purple borders |
| Billy Hatcher and the Giant Egg | Force 24-Bit Color | Off | `[Video_Enhancements] ForceTrueColor = False` | Fix non-player shadows not rendering |
| Billy Hatcher and the Giant Egg | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Correct missing text and darkness puddles |
| Blood Omen 2: Legacy of Kain | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Enables post-processing effects (when using Charm ability for example) |
| Blood Omen 2: Legacy of Kain | Defer EFB Copies to RAM | Off | `[Video_Hacks] DeferEFBCopies = False` | Fixes distortion effect in Eternal Prison level. |
| BlowOut | Scaled EFB Copy | Off | `[Video_Hacks] EFBScaledCopy = False` | Correct black textures |
| Bomberman Jetters | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Avoid purple frames between video clips |
| Bonsai Barber | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct photos |
| Boogie | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Bully: Scholarship Edition | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Required for in-game graphics |
| Carnival Games | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes stuttering on mini game icons. |
| Cars (Wii) | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Enable pause menu screenshots |
| Cartoon Network: Punch Time Explosion XL | Enable Dual Core | Off | `[Core] CPUThread = False` | Account for Invalid Read errors |
| Case Closed: The Mirapolis Investigation | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fix wrong character portraits |
| Chicken Little: Ace in Action | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Avoid purple video borders |
| Chronos Twins DX | Store EFB Copies to Texture Only | On | `[Video_Hacks] EFBToTextureEnable = True` | Show upper screen |
| Counter Force | Texture Cache Accuracy | Medium or Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes broken text in menus |
| Crazy Taxi | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Display texture artifacts appropriately |
| Crunchyroll Channel | Enable MMU | Enabled | `[Core] MMU = True` | Already set in INI settings, but it needs to be set manually if the channel is started from the Wii Menu. |
| Dancing with the Stars | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Dead Space: Extraction | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoids odd glitchy lines |
| Dead Space: Extraction | Defer EFB Copies to RAM | Off | `[Video_Hacks] DeferEFBCopies = False` | Fixes flash effect and Chapter 8 shadow issues |
| Dead Space: Extraction | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes flash effect and Chapter 8 shadow issues |
| Def Jam: Fight for NY | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Disney Princess: Enchanted Journey | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` |  |
| Dragon Quest X: Mezameshi Itsutsu no Shuzoku Online | Skip EFB Access from CPU | On | `[Video_Hacks] EFBAccessEnable = False` | Fixes crash when looking at the map |
| DreamWorks Super Star Kartz | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid scrambled text |
| EA Sports Active | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| EA Sports Active 2 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| EA Sports Active: More Workouts | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| EA Sports Active: NFL Training Camp | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Escape from Bug Island | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fix minimap not rendering |
| Excite Truck | Skip EFB Access from CPU | Off | `[Video_Hacks] EFBAccessEnable = True` | Emulate sun flare effect |
| Excite Truck | Defer EFB Copies to RAM | Off | `[Video_Hacks] DeferEFBCopies = False` | Fix broken shadows in multiplayer |
| Excite Truck | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Fix FMV corruption |
| F-Zero GX | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Corrects Master end credits sequence inaccuracies |
| F-Zero GX | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Working Emblem Editor cursor |
| F1 2002 | Texture Cache Accuracy | Position 2 | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Fixes stuttering cutscenes |
| FIFA Soccer 06 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| FIFA Soccer 07 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| FIFA Soccer 2003 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| FIFA Soccer 2004 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| FIFA Soccer 2005 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| FIFA Street | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| FIFA Street 2 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| FIFA World Cup: Germany 2006 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Fantastic Football Fan Party | Texture Cache Accuracy | Position 2 | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Fixes Opening Splashscreens |
| Far Cry Vengeance | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes intro videos |
| Fight Night Round 2 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Final Fantasy Crystal Chronicles: The Crystal Bearers | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Avoids obscured screen after jumping down the blue hexagon in the Subterranean Ruins. |
| Finest Hour | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes HUD not showing issue |
| Fishing Resort | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Allows unknown fish to be visible as black silhouettes in the fish book |
| Game Boy Player | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes flickering when playing Game Boy and Game Boy Color games |
| Gintama: Yorozuya Chuubu | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct pointer |
| Go Vacation | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Allow photo capture and correct black avatar icons |
| GoldenEye: Rogue Agent | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Gotcha Force | Enable MMU | On | `[Core] MMU = True` | Allows proper "Force 20 Glitch" Behavior |
| Guitar Hero: Warriors of Rock | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct instrument textures |
| Harley Pasternak's Hollywood Workout | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text properly |
| Harry Potter and the Prisoner of Azkaban | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Correct Warner Bros FMV |
| Harry Potter and the Prisoner of Azkaban | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Harvest Moon: Animal Parade | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Allow album to work |
| Harvey Birdman: Attorney at Law | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid frozen / out-of-sync animation |
| Homebrew Channel | Skip EFB Access from CPU | Off | `[Video_Hacks] EFBAccessEnable = True` | Required for screenshots to work properly |
| Horrible Histories: Ruthless Romans | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show cut-scenes appropriately |
| Hot Wheels: World Race | Texture Cache Accuracy | Position 2 | `[Video_Settings] SafeTextureCacheColorSamples = 512` | THQ logo issues otherwise |
| How to Train Your Dragon | Store EFB Copies to Texture Only | On | `[Video_Hacks] EFBToTextureEnable = True` | Solves some graphics problems (pink ocean) |
| Hugo: Magic in the Troll Woods | Ignore Format Changes | Off | `[Video_Hacks] EFBEmulateFormatChanges = True` | Correct blurry images |
| I SPY: Two Games in One | Skip EFB Access from CPU | On | `[Video_Hacks] EFBAccessEnable = False` | Allow interaction with some items |
| Imabikisō Kaimei Hen | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid Text Glitch |
| Interactive Multi Game Demo Disc v10 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Take pictures in Wind Waker |
| Interactive Multi Game Demo Disc v12 | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Correct missing text in Billy Hatcher |
| Interactive Multi Game Demo Disc v2 | Enable MMU | On | `[Core] MMU = True` | Required for Rogue Leader movie |
| Interactive Multi Game Demo Disc v31 | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display text |
| Interactive Multi Game Demo Disc v32 | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display text |
| Interactive Multi Game Demo Disc v33 | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display text |
| Interactive Multi Game Demo Disc v4 | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Avoid purple transitions |
| Interactive Multi Game Demo Disc v5 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Needed for correct glow rendering in Star Fox |
| Interactive Multi Game Demo Disc v6 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct glow rendering in Star Fox and correct graffiti behavior in Sunshine |
| Interactive Multi Game Demo Disc v7 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct graffiti behavior in Super Mario Sunshine |
| Interactive Multi Game Demo Disc v8 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct graffiti behavior in Super Mario Sunshine |
| Iron Chef America: Supreme Cuisine | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show sauces |
| JumpStart: Crazy Karts | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid opcode errors |
| Jurassic: The Hunted | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text |
| Lego Star Wars: The Video Game | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid crashes |
| Let's Dance with Mel B | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Littlest Pet Shop | Texture Cache Accuracy | Not Fast | `[Video_Settings] SafeTextureCacheColorSamples = 128` | Show video appropriately |
| Luigi's Mansion | Enable Dual Core | Off | `[Core] CPUThread = False` | Fix Luigi's model in the game intro |
| MVP Baseball 2005 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Madagascar: Escape 2 Africa | Texture Cache Accuracy | Not Fast | `[Video_Settings] SafeTextureCacheColorSamples = 128` | Show video appropriately |
| Madden NFL 12 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Mahō Sensei Negima!? Neo-Pactio Fight!! | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Required in any backend to correctly render text (missing letters). |
| Manhunt 2 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fix black screens |
| Mario Kart Wii | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Support Wii Pinboard pictures |
| Mario Kart Wii | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show lens flares |
| Mario Kart Wii | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes map in Coin Runners Mode. |
| Mario Kart: Double Dash‼ | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct lens flare effect and BBA kart flags |
| Mario Kart: Double Dash‼ Bonus Disc | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Avoid glitches in Mario Party 5 Demo |
| Mario Party 4 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Avoid shadow issues |
| Mario Party 4 | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show Trace Race correctly |
| Mario Party 4 | Fast Depth Calculation | Off | `[Video_Settings] FastDepthCalc = False` | Avoid Z-Fighting |
| Mario Party 4 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Fixes Texture Seams in minigame description message boxes. |
| Mario Party 5 | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Update Bus Buffer paint properly |
| Mario Party 5 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Fixes Texture Seams in minigame description message boxes (plus others at >1x IR) |
| Mario Party 7 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Fixes Texture Seams |
| Mario Party 9 | Texture Cache Accuracy | Position 2 (Medium) | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Fix "Hole Hogs" minigame |
| Mario Strikers Charged | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Display "Freeze Frame!" photographs properly |
| Mario Super Sluggers | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Display correct blur |
| Marvel Nemesis: Rise of the Imperfects | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Marvel Super Hero Squad | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display text correctly |
| Marvel: Ultimate Alliance | Immediately Present XFB | Off | `[Video_Hacks] ImmediateXFBEnable = False` | Avoid screen flicker |
| Marvel: Ultimate Alliance 2 | Immediately Present XFB | Off | `[Video_Hacks] ImmediateXFBEnable = False` | Avoid screen flicker |
| Medal of Honor: European Assault | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Medal of Honor: Frontline | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Medal of Honor: Heroes 2 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Medal of Honor: Rising Sun | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Medal of Honor: Vanguard | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Show VP6 videos appropriately |
| Merv Griffin's Crosswords | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Show VP6 videos appropriately |
| Metroid Prime (GC) | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Render rain effect correctly |
| Mission: Impossible - Operation Surma | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct Night Vision |
| Monopoly Collection | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Needed for intro movie to not stutter |
| Monster Hunter Tri | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Render screenshot after quest completion |
| My Fitness Coach 2: Exercise & Nutrition | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Render text correctly |
| My Pokémon Ranch | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Correct photos |
| NBA JAM | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Prevents menu corruption |
| NBA Live 06 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| NBA Live 08 | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Avoid pink flash during wrist strap warning |
| NBA Live 08 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Show VP6 videos appropriately |
| NBA Live 09 All-Play | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show player limbs appropriately |
| NBA Live 09 All-Play | Defer EFB Copies to RAM | Off | `[Video_Hacks] DeferEFBCopies = False` | Show player limbs appropriately |
| NBA Live 2003 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| NBA Live 2004 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| NBA Live 2005 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| NBA Street | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| NBA Street Vol. 2 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| NHL 2K10 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show audience |
| NHL 2K11 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show audience |
| NHL 2K9 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show audience |
| Need for Speed: Hot Pursuit | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Need for Speed: Hot Pursuit 2 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Need for Speed: Most Wanted | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Need for Speed: Nitro | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid potential freeze on boot, and harmless opcode errors in-game. |
| Need for Speed: Nitro | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Need for Speed: ProStreet | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Need for Speed: Undercover | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Need for Speed: Underground | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes cutscene stutters |
| Need for Speed: Underground 2 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| NewU Fitness First: Mind Body - Yoga & Pilates Workout | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes text |
| Ni Hao, Kai-Lan: Super Game Day | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Account for laggy cut-scenes |
| Nickelodeon Fit | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Account for laggy cut-scenes |
| No More Heroes | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Enables post processing effects. |
| One Piece: Pirates' Carnival | Vertex Rounding Hack | On | `[Video_Hacks] VertexRounding = True` | Fixes white line at the left and top edges during the title card for IR>1 |
| Overlord: Dark Legend | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text properly |
| Paper Mario | Enable Dual Core | Off | `[Core] CPUThread = False` | Show File Select menus properly |
| Paper Mario: The Thousand-Year Door | Enable Dual Core | Off | `[Core] CPUThread = False` | Fixes 60Hz mode reverting to 50Hz in EU version |
| Peach's Castle | Enable Dual Core | Off | `[Core] CPUThread = False` | Prevent FIFO error/crash in coin demo |
| Pet Vet: Marine Patrol | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show textures appropriately |
| Petz Rescue: Wildlife Vet | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Petz: Crazy Monkeyz | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Required for photo album |
| Petz: Horse Club | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Show VP6 videos |
| Phantasy Star Online Episode I & II Plus | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Render text appropriately |
| Phelios (Arcade) | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid stuttering video |
| Pikmin (GC) | Texture Cache Accuracy | Position 2 (Medium) | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Resolves pre-rendered video stuttering |
| Pikmin (GC) | DSP Emulator Engine | LLE | `[Core] DSPHLE = False` | Render audio appropriately |
| Pikmin 2 (Wii) | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Correct garbled bottom line on PAL version |
| Planet Basket 2009/2010 | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Correct corrupted text |
| PokéPark Wii: Pikachu's Adventure | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Required for taking snapshots only |
| Pokémon Battle Revolution | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes broken rental pass trainer images |
| Pokémon Channel | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Enable programs/painting |
| Pokémon Channel | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Makes the Smeargle painting tools more responsive. |
| Pokémon Fushigi no Dungeon: Ikuzo! Arashi no Bōkendan | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes map updates |
| Pokémon Fushigi no Dungeon: Mezase! Hikari no Bōkendan | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes map updates |
| Pokémon Puzzle League | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Functional transition effects |
| Pokémon Snap | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid tutorial lockups |
| Pony Friends 2 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show horse during grooming |
| Prince of Persia: The Forgotten Sands | Synchronize GPU Thread | On | `[Core] SyncGPU = True` | Avoid flickering shadows |
| Prince of Persia: The Sands of Time | Enable Dual Core | Off | `[Core] CPUThread = False` | Fixes unknown opcode error before credits |
| Prince of Persia: The Sands of Time | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Fixes purple transitions |
| Project Runway | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Rabbids Go Home | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Required to remove artifacts from FMVs on some GPUs |
| Rampage: Total Destruction (Wii) | Texture Cache Accuracy | Not fast | `[Video_Settings] SafeTextureCacheColorSamples = 128` | Show bonus game appropriately |
| Rampage: Total Destruction (Wii) | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Show VP6 videos |
| Rayman Raving Rabbids | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Required to remove artifacts from FMVs on some GPUs |
| Reload: Target Down | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Resident Evil | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Corrects map bugs |
| Resident Evil 3: Nemesis | Texture Cache Accuracy | Position 1 (safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Prevents item icons from occasionally disappearing on inventory screen |
| Resident Evil 4 | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | avoid incorrect rendering of some text |
| Resident Evil 4: Wii edition | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Avoid colored lines on borders |
| Resident Evil Archives: Resident Evil Zero | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Prevents some elements becoming invisible |
| Resident Evil: The Darkside Chronicles | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fix bright lighting |
| Retro City Rampage | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes an issue where some menus/dialog boxes fail to update |
| Ribbit King | Texture Cache Accuracy | Position 2 (Medium) | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Fixes flickering videos |
| Ribbit King Plus! | Texture Cache Accuracy | Position 1 (Medium) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes flickering |
| Robotech: Battlecry | DSP Emulator Engine | LLE | `[Core] DSPHLE = False` | Avoids missing audio cues |
| Rock Band 2 | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes the animation of the first few seconds of the credits |
| Rocky | Enable Dual Core | Off | `[Core] CPUThread = False` | Prevents flickering in menus/certain stages |
| Rugby League 3 | Texture Cache Accuracy | Not fast | `[Video_Settings] SafeTextureCacheColorSamples = 128` | Show intro appropriately |
| Runaway: The Dream of the Turtle | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| SPRay | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show liquids appropriately |
| SSX 3 | Skip EFB Access from CPU | Off | `[Video_Hacks] EFBAccessEnable = True` | Appropriately display sun |
| SSX 3 | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| SSX Blur | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| SSX on Tour | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Schlag den Raab | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes text |
| Science Papa | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show animations appropriately |
| Sengoku Basara 2 Heroes | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Removes the green line that would otherwise appear at the bottom of the screen |
| Sengoku Musou 3 Moushouden | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` |  |
| Serious Sam: Next Encounter | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` |  |
| Serious Sam: Next Encounter | Defer EFB Copies to RAM | Off | `[Video_Hacks] DeferEFBCopies = False` | Fixes splitscreen issues. Not necessary in single player. |
| Serious Sam: Next Encounter | Force 24-Bit Color | Off | `[Video_Enhancements] ForceTrueColor = False` | Fix blotchy textures |
| Sesame Street: Cookie's Counting Carnival | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Sesame Street: Elmo's A-to-Zoo Adventure | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Sesame Street: Elmo's Musical Monsterpiece | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Sesame Street: Ready, Set, Grover! | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| Shadow the Hedgehog | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes 2nd player screen. Not necessary in single player. |
| Shadow the Hedgehog | Vertex Rounding Hack | On | `[Video_Hacks] VertexRounding = True` | Address higher IR rendering issues |
| Shark Tale | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show pause menu backgrounds |
| Shrek Smash n' Crash Racing | Scaled EFB Copy | Off | `[Video_Hacks] EFBScaledCopy = False` | Avoid vertical white lines |
| Shrek Smash n' Crash Racing | Vertex Rounding Hack | On | `[Video_Hacks] VertexRounding = True` | Alternative method to avoid vertical white lines |
| Silent Hill: Shattered Memories | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show snow. correct flickering |
| SimAnimals | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Allow interaction with items |
| SimAnimals | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display text appropriately |
| SimAnimals Africa | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Allow interaction with items |
| SimAnimals Africa | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display text appropriately |
| Sin & Punishment: Star Successor | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Avoid minor graphics bugs |
| Skylanders: Giants | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Required to remove artifacts from FMVs on some GPUs |
| Skylanders: Spyro's Adventure | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Required to remove artifacts from FMVs on some GPUs |
| Skylanders: Trap Team | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Required to remove artifacts from FMVs on some GPUs |
| Sonic Adventure 2: Battle | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Text in cutscenes updates properly |
| Sonic Adventure DX: Director's Cut | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes display issues in Game Gear titles |
| Sonic Mega Collection | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid minor issues with 2D titles |
| SoulCalibur Legends | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Allows the game to launch |
| Soulcalibur II | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Needed for lens flare effects |
| Space Camp | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Show VP6 videos |
| Spider-Man 3 | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Avoid pink screens in cut scenes |
| SpongeBob SquarePants: Plankton's Robotic Revenge | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Show FMVs without artifacts |
| SpongeBob's Truth or Square | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Needed to display text properly |
| Spore Hero | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Avoid creature color issues |
| Spy Fox in Dry Cereal | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fix cutscenes |
| Spyro: A Hero's Tail | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fix light glow |
| Spyro: A Hero's Tail | Force 24-Bit Color | Off | `[Video_Enhancements] ForceTrueColor = False` | Fix blotchy textures |
| Star Fox Adventures | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Needed for correct glow rendering |
| Star Wars Rogue Squadron II: Rogue Leader | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid crashing |
| Star Wars Rogue Squadron II: Rogue Leader | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes menu fadeouts |
| Star Wars Rogue Squadron III: Rebel Strike | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid crashing |
| Star Wars Rogue Squadron III: Rebel Strike | Skip EFB Access from CPU | Off | `[Video_Hacks] EFBAccessEnable = True` | Makes engine glow visible |
| Star Wars Rogue Squadron III: Rebel Strike | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Fixes purple transitions and purple models at far distances |
| StarBlade | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid Unknown Opcode errors |
| StarBlade | Ignore Format Changes | Off | `[Video_Hacks] EFBEmulateFormatChanges = True` | Restore original colors of graphics |
| StarBlade | Force 24-Bit Color | Off | `[Video_Enhancements] ForceTrueColor = False` | Restore original colors of graphics |
| Strike Force Bowling | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Render pin preview |
| Strike Force Bowling | Defer EFB Copies to RAM | Off | `[Video_Hacks] DeferEFBCopies = False` | Render pin preview correctly |
| Super Mario All-Stars: 25th Anniversary Edition | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Account for pink line at bottom of screen |
| Super Mario Galaxy | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Support Wii Message Board images; fix Cosmic Mario/Luigi Shell; show Mii face icons |
| Super Mario Galaxy 2 | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Fix Wii Message Board Images |
| Super Mario Strikers | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Show loading animations |
| Super Mario Sunshine | Synchronize GPU Thread | On | `[Core] SyncGPU = True` | Avoids Shaky Props issue |
| Super Smash Bros. Brawl | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes black background in hoops when a character goes off-screen Stops screenshots from being a garbled mess or black Required for NES graphics to show up |
| Super Smash Bros. Brawl | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes NES and SNES graphics not updating sometimes |
| Super Smash Bros. Brawl | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Fixes purple rectangle when clearing stage in Classic Mode |
| Super Smash Bros. Melee | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Properly save screenshots in Camera Mode of Special Melee |
| Suzumiya Haruhi no Heiretsu | Fast Depth Calculation | Off | `[Video_Settings] FastDepthCalc = False` | Fixes wireframe-like glitches on models |
| TMNT (Wii) | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid intro glitches |
| TMNT (Wii) | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Account for horizontal lines in FMVs |
| Tales of Symphonia: Dawn of the New World | Texture Cache Accuracy | Position 2 (Medium) | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Display skits correctly |
| Tales of Symphonia: Dawn of the New World | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Show appropriate backgrounds in skits |
| Target: Terror | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid enemy glitches |
| Target: Terror | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| The Godfather: Blackhand Edition | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| The Incredibles: Rise of the Underminer | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Avoid purple bands on videos |
| The Last Story | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Prevent display of green line across bottom of screen |
| The Legend of Spyro: A New Beginning | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes light glow |
| The Legend of Zelda: Majora's Mask | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fixes the game "under" the pause screen becoming black on pause. Useful for pause buffering. |
| The Ninja Warriors | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Avoid stuttering video |
| The Oregon Trail | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| The Princess and the Frog | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| The Simpsons Hit & Run | Skip EFB Access from CPU | Off | `[Video_Hacks] EFBAccessEnable = True` | Emulate sun flare effect. |
| The Sims 2 | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Shows parents when generating a sim |
| The Smurfs 2 | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| The Smurfs: Party Pack | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Show text appropriately |
| The Voice: I Want You | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Correct singer flickering |
| Tiger Woods PGA Tour 06 | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes garbled text |
| Tiger Woods PGA Tour 12: The Masters | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Accurately display distance percentage |
| TimeSplitters: Future Perfect | Synchronize GPU Thread | On | `[Core] SyncGPU = True` | Avoid FIFO Errors |
| Tom Clancy's Ghost Recon (GC) | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Display loading screens properly |
| Tom Clancy's Rainbow Six: Lockdown | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Display loading screen details |
| Tomb Raider: Anniversary | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Account for horizontal lines in FMV |
| Tornado Outbreak | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Render VP6 video |
| Toy Story Mania! | Manual Texture Sampling | On | `[Video_Hacks] FastTextureSampling = False` | Correct lines in FMVs |
| Trivial Pursuit: Bet You Know It | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Avoid screen flashing rapidly |
| Tron: Evolution - Battle Grids | Texture Cache Accuracy | Position 1 (Safe) | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes an issue where random text characters would be missing. |
| Ultimate Shooting Collection | Texture Cache Accuracy | Safe/Normal | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Fixes text display in Radirgy. |
| WWE '12 | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display all Create A Superstar items |
| WWE '13 | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Display all Create a Superstar items |
| Wall•E | Store XFB Copies to Texture Only | Off | `[Video_Hacks] XFBToTextureEnable = False` | Avoid purple video borders |
| Wall•E | Texture Cache Accuracy | Safe | `[Video_Settings] SafeTextureCacheColorSamples = 0` | Correct text display |
| WarioWare: Smooth Moves | Texture Cache Accuracy | Medium | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Fixes slight graphical errors during FMVs |
| Wii Fit Channel | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fix Mii faces and graph in banner |
| Wii Fit Plus Channel | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Fix Mii faces and graph in banner |
| Wii Sports Resort | Vertex Rounding Hack | On | `[Video_Hacks] VertexRounding = True` | Fixes misaligned UI for IR>1 |
| Wipeout 2 | Scaled EFB Copy | Off | `[Video_Hacks] EFBScaledCopy = False` | Avoid black lines |
| World Series of Poker: Tournament of Champions: 2007 Edition | Immediately Present XFB | On | `[Video_Hacks] ImmediateXFBEnable = True` | Remove green line |
| X-Men Legends | Texture Cache Accuracy | Position 2 (Medium) | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Fixes stuttering videos |
| Xenoblade Chronicles | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Enable screenshot when saving/loading |
| Yakuman Wii: Ide Yosuke no Kenkou Mahjong | Enable Dual Core | Off | `[Core] CPUThread = False` | Avoid flickering Mii's |
| Zenkoku Dekotora Matsuri | Synchronize GPU Thread | On | `[Core] SyncGPU = True` | Avoid flickering reflections |
| Zenkoku Dekotora Matsuri | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Enable painting and photographs |
| Zero: Tsukihami no Kamen | Store EFB Copies to Texture Only | Off | `[Video_Hacks] EFBToTextureEnable = False` | Enable seeing pictures in the album |
| Zumba Fitness | Texture Cache Accuracy | Position 2 (Medium) | `[Video_Settings] SafeTextureCacheColorSamples = 512` | Prevents flickering on character model |
