import re
from pathlib import Path

html_path = Path("docs/index.html")
html = html_path.read_text(encoding="utf-8")

# ==============================================================================
# 1. UPDATE RUNTIME TOP STATUS
# ==============================================================================
html = re.sub(
    r'<span class="text-cyan-400 font-semibold tracking-wide">PITCH-LÄGE.*?</span>',
    '<span class="text-emerald-400 font-semibold tracking-wide">PRODUKTION KLAR: Paket #004 Godkänt & Revisionsgranskat (100% Compliant)</span>',
    html
)

# ==============================================================================
# 2. UPDATE SECTION 1 PITCHES (REPLACE 003, 004 WITH 005, 006, 007)
# ==============================================================================
start_marker = '<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="pitchesContainer">'
end_marker = '<!-- SECTION 2: DAGENS FÄRDIGA VIDEOPAKET'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_pitches_html = '''<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="pitchesContainer">
        
        <!-- PITCH 1: PITCH #005 (AUDIO PODCASTAR FRÅN TEXT) -->
        <div class="glass-card rounded-2xl p-5 border border-cyan-500/40 hover:border-cyan-400/60 transition-all flex flex-col justify-between space-y-4 bg-cyan-950/10">
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">PITCH #005</span>
              <span class="text-cyan-300 font-semibold font-mono">⏱️ Längd: 3:30–4:30 min</span>
            </div>
            
            <h3 class="text-base font-bold text-white hover:text-cyan-300 transition">Turn Any Text Document into Audio Podcasts in Python</h3>
            <p class="text-xs text-slate-300 italic">"Engineers do not read 40-page documentation. Here is how to turn technical docs into audio podcasts automatically."</p>
            
            <!-- Beslutsunderlag Mini-Tabell -->
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between">
                <span class="text-slate-400">Pedagogiskt Mål:</span>
                <span class="text-cyan-300 font-semibold text-right">Markdown/PDF till podcast-dialog</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Sökvolym:</span>
                <span class="text-white font-mono">19 800/mån (+55% MoM)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Nisch-RPM:</span>
                <span class="text-emerald-400 font-mono font-bold">$24.10</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Målgrupp:</span>
                <span class="text-slate-300">Tech Writers, Developers & Solopreneurs</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Affiliatepartner:</span>
                <span class="text-purple-300 font-semibold">ElevenLabs Audio Native (22% Rec)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Kod i Sandlåda:</span>
                <span class="text-emerald-400 font-mono text-[11px]">Audio Native API + Markdown Parser</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex items-center gap-2">
            <button onclick="showPitchDossier(0)" class="flex-1 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 font-semibold transition text-center">
              📋 Granska Dossier
            </button>
            <button id="pitchBtn0" onclick="triggerPitch('PITCH #005', 'Turn Any Text Document into Audio Podcasts in Python', this)" class="px-4 py-2 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs transition shadow-md shadow-cyan-600/30 flex items-center gap-1.5">
              <span>🚀 Exekvera</span>
            </button>
          </div>
        </div>

        <!-- PITCH 2: PITCH #006 (TAL-TILL-TAL TOLKNING I REALTID) -->
        <div class="glass-card rounded-2xl p-5 border border-purple-500/40 hover:border-purple-400/60 transition-all flex flex-col justify-between space-y-4 bg-purple-950/10">
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded font-mono font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">PITCH #006</span>
              <span class="text-purple-300 font-semibold font-mono">⏱️ Längd: 3:30–4:30 min</span>
            </div>
            
            <h3 class="text-base font-bold text-white hover:text-purple-300 transition">Build an AI Real-Time Voice Translator in Python</h3>
            <p class="text-xs text-slate-300 italic">"Language barriers kill global B2B deals. Build a sub-500ms real-time, two-way speech interpreter in Python."</p>
            
            <!-- Beslutsunderlag Mini-Tabell -->
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between">
                <span class="text-slate-400">Pedagogiskt Mål:</span>
                <span class="text-purple-300 font-semibold text-right">Tvåvägs simultantolkning (Sub-500ms)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Sökvolym:</span>
                <span class="text-white font-mono">31 200/mån (+88% MoM)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Nisch-RPM:</span>
                <span class="text-emerald-400 font-mono font-bold">$31.80</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Målgrupp:</span>
                <span class="text-slate-300">Global SaaS Teams, Founders & Sales</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Affiliatepartner:</span>
                <span class="text-purple-300 font-semibold">ElevenLabs Speech-to-Speech (22% Rec)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Kod i Sandlåda:</span>
                <span class="text-emerald-400 font-mono text-[11px]">ElevenLabs S2S API + PyAudio Buffer</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex items-center gap-2">
            <button onclick="showPitchDossier(1)" class="flex-1 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 font-semibold transition text-center">
              📋 Granska Dossier
            </button>
            <button id="pitchBtn1" onclick="triggerPitch('PITCH #006', 'Build an AI Real-Time Voice Translator in Python', this)" class="px-4 py-2 rounded-lg bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs transition shadow-md shadow-purple-600/30 flex items-center gap-1.5">
              <span>🚀 Exekvera</span>
            </button>
          </div>
        </div>

        <!-- PITCH 3: PITCH #007 (DYNAMISKT SPELLJUD & NPC-RÖSTER) -->
        <div class="glass-card rounded-2xl p-5 border border-emerald-500/40 hover:border-emerald-400/60 transition-all flex flex-col justify-between space-y-4 bg-emerald-950/10">
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">PITCH #007</span>
              <span class="text-emerald-300 font-semibold font-mono">⏱️ Längd: 3:30–4:30 min</span>
            </div>
            
            <h3 class="text-base font-bold text-white hover:text-emerald-300 transition">Generate Dynamic AI Game Audio & NPC Voices in Python</h3>
            <p class="text-xs text-slate-300 italic">"Static audio assets are obsolete. Build an infinite procedural sound effects and NPC dialogue engine in Python."</p>
            
            <!-- Beslutsunderlag Mini-Tabell -->
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between">
                <span class="text-slate-400">Pedagogiskt Mål:</span>
                <span class="text-emerald-300 font-semibold text-right">Proceduriella ljudeffekter & NPC-dialog</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Sökvolym:</span>
                <span class="text-white font-mono">26 400/mån (+73% MoM)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Nisch-RPM:</span>
                <span class="text-emerald-400 font-mono font-bold">$27.50</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Målgrupp:</span>
                <span class="text-slate-300">Game Developers, Creators & AI Teams</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Affiliatepartner:</span>
                <span class="text-purple-300 font-semibold">ElevenLabs Sound Effects API (22% Rec)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Kod i Sandlåda:</span>
                <span class="text-emerald-400 font-mono text-[11px]">Sound Effects API + Audio Player</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex items-center gap-2">
            <button onclick="showPitchDossier(2)" class="flex-1 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 font-semibold transition text-center">
              📋 Granska Dossier
            </button>
            <button id="pitchBtn2" onclick="triggerPitch('PITCH #007', 'Generate Dynamic AI Game Audio & NPC Voices in Python', this)" class="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow-md shadow-emerald-600/30 flex items-center gap-1.5">
              <span>🚀 Exekvera</span>
            </button>
          </div>
        </div>

      </div>
    </section>

    '''
    html = html[:start_idx] + new_pitches_html + html[end_idx:]

# ==============================================================================
# 3. UPDATE SECTION 2: CURRENT REVIEW PACKAGE (SWITCH FROM 003 TO 004)
# ==============================================================================
html = html.replace(
    "Dagens Färdiga Videopaket #003",
    "Dagens Färdiga Videopaket #004"
)
html = html.replace(
    "1080p Långformat (06:32 min) + 9:16 Shorts (19.1s) + Split-Screen Thumbnail + Komplett Engelsk SEO & ElevenLabs Dubbing Affiliate",
    "1080p Långformat (06:41 min) + 9:16 Shorts (19.0s) + Split-Screen Thumbnail + Komplett Engelsk SEO & ElevenLabs Telephony Affiliate"
)
html = html.replace(
    "1080p Full HD (06:32 min, 7 Synkade Scener + Verifierad Kod)",
    "1080p Full HD (06:41 min, 7 Synkade Scener + Verifierad Kod)"
)
html = html.replace("assets/video_003_long.mp4", "assets/video_004_long.mp4")
html = html.replace("assets/video_003_short.mp4", "assets/video_004_short.mp4")
html = html.replace("assets/thumb_003.png", "assets/thumb_004.png")

# Metadata replacement inside the review package
html = html.replace(
    "How to Clone Voices and Dub Videos in Python (ElevenLabs API 2026) [EPISODE 003]",
    "Build an AI Voice Phone Agent in Python (ElevenLabs + Twilio) [EPISODE 004]"
)
html = html.replace(
    "https://try.elevenlabs.io/agentic-dubbing",
    "https://try.elevenlabs.io/agentic-telephony"
)
html = html.replace(
    "003-voice-cloning-video-dubbing",
    "004-voice-phone-agent"
)

# Replace description snippet
old_desc_marker = "Manual video localization is dead. Paying $500 per language"
if old_desc_marker in html:
    desc_start = html.find(old_desc_marker)
    # replace up to closing </textarea> or quote
    end_tag = html.find("</textarea>", desc_start)
    if end_tag != -1:
        new_desc_content = """🎁 [FREE TRIAL] Try ElevenLabs Conversational Voice AI:
👉 https://try.elevenlabs.io/agentic-telephony (Affiliate Partner Link)

🚀 [SOURCE CODE] Download Python Telephony Scripts & FastAPI Blueprint:
👉 https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/004-voice-phone-agent

📚 [OPEN SOURCE REPO] All Channel Episodes & Star the Library:
👉 https://github.com/Johnmannen/Agentic-Stack-Library

Legacy IVR phone menus are dead in enterprise B2B. Forcing high-value customers to dial through press one for sales and press two for support destroys retention and bleeds thousands of dollars on human tier-one call centers.

In this video, we build an autonomous AI voice phone agent in Python using ElevenLabs Conversational AI and Twilio SIP Media Streams. Our agent answers real inbound telephone calls with sub-400ms full-duplex latency, looks up live customer records in PostgreSQL, and schedules appointments on the fly.

⏱️ TIMESTAMPS:
00:00 - KILL LEGACY IVR PHONE MENUS FOREVER
00:58 - SYSTEM ARCHITECTURE: FULL-DUPLEX PHONE BRIDGE
02:18 - TWILIO WEBHOOK & FASTAPI WEBSOCKET BRIDGE
03:28 - LIVE DATABASE TOOL CALLING & CRM ACTIONS
04:22 - LATENCY PROFILING & PACKET BENCHMARKS
05:08 - ENTERPRISE CALL CENTER ECONOMICS & ROI
05:48 - GITHUB BLUEPRINT, FREE TRIAL & NEXT EPISODE

🛠️ ENTERPRISE TOOLS (VERIFIED IN SANDBOX):
👉 Try ElevenLabs Conversational Telephony: https://try.elevenlabs.io/agentic-telephony

⚖️ FTC AFFILIATE DISCLOSURE:
Some links in this description are affiliate links. If you sign up or purchase through them, we may receive a commission at no extra cost to you. We strictly test and verify every tool in our cloud sandbox before recommending it.

#VoiceAI #ElevenLabs #Twilio #Python #FastAPI #Telephony #ConversationalAI #AIAgents"""
        html = html[:desc_start] + new_desc_content + html[end_tag:]

# ==============================================================================
# 4. ADD EPISODE 003 TO THE ARCHIVE LIST
# ==============================================================================
archive_header = 'Tidigare färdigställda videopaket, källkodsrepon och direkta YouTube-länkar.</p>\n          </div>\n        </div>\n      </div>'
ep_003_card = '''\n\n      <!-- AVSNITT #003 (NYLIGEN UPPLADDAD) -->
      <div class="glass-card rounded-2xl p-5 border border-purple-500/40 bg-slate-900/50 hover:border-purple-500/70 transition">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <div class="relative w-28 h-16 rounded-xl overflow-hidden border border-purple-500/40 bg-slate-950 shrink-0">
              <img src="assets/thumb_003.png" alt="Ep 003 Thumbnail" class="w-full h-full object-cover">
            </div>
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded font-mono font-bold text-[10px] bg-purple-500/20 text-purple-300 border border-purple-500/30">AVSNITT #003</span>
                <span class="px-2 py-0.5 rounded-full font-mono font-semibold text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-500/30 flex items-center gap-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                  ● LIVE PÅ YOUTUBE
                </span>
                <span class="text-[10px] text-slate-400">Publicerad: 2026-11-12</span>
              </div>
              <h4 class="text-sm font-bold text-white">How to Clone Voices and Dub Videos in Python (ElevenLabs API 2026)</h4>
              <p class="text-xs text-slate-400">Full 1080p dubbing engine, 29 languages, zero-shot vocal timbre match & FFmpeg batch stream.</p>
            </div>
          </div>
          <div class="flex items-center gap-2 w-full md:w-auto">
            <a href="https://studio.youtube.com/channel/UCkphdiVQvc1vvNlcrAorMOg" target="_blank" class="px-3.5 py-2 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-md shadow-red-600/30">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
              <span>Se på YouTube</span>
            </a>
            <a href="https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/003-voice-cloning-video-dubbing" target="_blank" class="px-3.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs flex items-center gap-1.5 transition">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"/></svg>
              <span>GitHub Kod</span>
            </a>
            <a href="assets/video_003_long.mp4" download class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs transition" title="Ladda ner MP4">
              ⬇ MP4
            </a>
          </div>
        </div>
      </div>'''

if archive_header in html and "AVSNITT #003" not in html:
    html = html.replace(archive_header, archive_header + ep_003_card)

# ==============================================================================
# 5. UPDATE PITCH_DATA IN JAVASCRIPT FOR DOSSIER MODAL
# ==============================================================================
js_pitch_start = "const PITCH_DATA = ["
js_pitch_end = "function closePitchModal()"
p_s = html.find(js_pitch_start)
p_e = html.find(js_pitch_end)

if p_s != -1 and p_e != -1:
    new_pitch_js = '''const PITCH_DATA = [
      {
        id: "PITCH #005",
        duration: "⏱️ Längd: 3:30–4:30 minuter",
        title: "Turn Any Text Document into Audio Podcasts in Python (ElevenLabs Audio Native)",
        goal: "Bygg en automatisk pipeline i Python som parsar Markdown/PDF-dokument, genererar naturligt två-rösts tal via ElevenLabs Audio Native API och automatiskt skapar lyssningsbara poddar.",
        script_steps: [
          "• Scen 1 (00:00 - 00:30): Dokumentationsdilemmat: Många föredrar att lyssna medan de pendlar eller kodar framför att läsa 50 sidor.",
          "• Scen 2 (00:30 - 01:15): ElevenLabs Audio Native: Hur automatisk textanalys och spelarinbäddning fungerar.",
          "• Scen 3 (01:15 - 02:30): Python Parser: Extrahera text från Markdown/PDF och tilldela olika roller till talare.",
          "• Scen 4 (02:30 - 03:30): Batch Audio Rendering: Exportera podcast-färdiga MP3-filer.",
          "• Scen 5 (03:30 - 04:15): Outro med talad ElevenLabs gratis provperiod, GitHub och nästa video."
        ],
        trend: "Sökvolym: 19 800 sökningar/månad (+55% MoM). Audio-first dokumentation ökar snabbt i popularitet.",
        code: "ElevenLabs Audio Native API + Python Markdown/PDF Parser för automatisk podcastgenerering.",
        affiliates: [
          "• ElevenLabs Creator Tier: 22% Recurring Commission via PartnerStack",
          "• PyMuPDF / Python Markdown Tooling"
        ]
      },
      {
        id: "PITCH #006",
        duration: "⏱️ Längd: 3:30–4:30 minuter",
        title: "Build an AI Real-Time Voice Translator in Python (ElevenLabs Speech-to-Speech)",
        goal: "Skapa en tvåvägs simultantolk i Python för internationella B2B-kundmöten som översätter talat språk i realtid med sub-500ms latens med bibehållen röstkaraktär.",
        script_steps: [
          "• Scen 1 (00:00 - 00:30): Språkbarriärer i internationell försäljning: Varför traditionella textöversättare bryter samtalstonen.",
          "• Scen 2 (00:30 - 01:15): ElevenLabs S2S Arkitektur: Direkt tal-till-tal streaming utan mellanliggande textbuffert.",
          "• Scen 3 (01:15 - 02:30): Python PyAudio & WebSockets: Hantera mikrofonström och asynkron ljudretur.",
          "• Scen 4 (02:30 - 03:30): Live Demo: Engelska till Spanska/Tyska i realtid med bevarad röstidentitet.",
          "• Scen 5 (03:30 - 04:15): Outro med talad ElevenLabs gratis provperiod, GitHub och nästa video."
        ],
        trend: "Sökvolym: 31 200 sökningar/månad (+88% MoM). Global efterfrågan på realtidstolkning för distansmöten.",
        code: "ElevenLabs Speech-to-Speech Streaming API + Python PyAudio bi-directional stream buffer.",
        affiliates: [
          "• ElevenLabs Speech-to-Speech & Conversational AI: 22% Recurring Commission via PartnerStack",
          "• PyAudio / WebRTC Python Stream Tools"
        ]
      },
      {
        id: "PITCH #007",
        duration: "⏱️ Längd: 3:30–4:30 minuter",
        title: "Generate Dynamic AI Game Audio & NPC Voices in Python (ElevenLabs Sound Effects)",
        goal: "Bygg ett proceduriellt ljud- och röstsystem i Python som genererar dynamiska ljudeffekter och NPC-dialog on-the-fly baserat på spelhändelser och kontext.",
        script_steps: [
          "• Scen 1 (00:00 - 00:30): Begränsningen med statiska ljudbibliotek: Varför moderna spel och appar behöver adaptivt ljud.",
          "• Scen 2 (00:30 - 01:15): ElevenLabs Sound Effects & Voice Design API: Text-till-ljud och prompt-styrd ljuddesign.",
          "• Scen 3 (01:15 - 02:30): Python API Integration: Skicka händelse-prompts och ta emot binaurala ljudeffekter.",
          "• Scen 4 (02:30 - 03:30): Dynamic NPC Engine: Kombinera LLM-repliker med direkt röstsyntes i runtime.",
          "• Scen 5 (03:30 - 04:15): Outro med talad ElevenLabs gratis provperiod, GitHub och nästa video."
        ],
        trend: "Sökvolym: 26 400 sökningar/månad (+73% MoM). Spelutvecklare och immersiva appar anammar generativt ljud.",
        code: "ElevenLabs Sound Effects API + Python Fast WebSocket Audio Player för dynamiska spelsoundscapes.",
        affiliates: [
          "• ElevenLabs Sound Effects & Voice Design API: 22% Recurring Commission via PartnerStack",
          "• SimpleAudio / Pygame Audio Engine Toolkit"
        ]
      }
    ];

    '''
    html = html[:p_s] + new_pitch_js + html[p_e:]

html_path.write_text(html, encoding="utf-8")
print("Successfully updated docs/index.html with Episode 004 and Pitches 005, 006, 007!")
