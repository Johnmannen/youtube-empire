import re
from pathlib import Path

html_path = Path("docs/index.html")
html = html_path.read_text(encoding="utf-8")

# 1. Update review package section header
html = html.replace(
    "Dagens Färdiga Videopaket #003",
    "Dagens Färdiga Videopaket #002.1"
)
html = html.replace(
    "1080p Långformat + 9:16 Short (&lt;20s) + Högkontrast 1280x720 Thumbnail + Komplett Engelsk SEO & ElevenLabs Dubbing Affiliate",
    "1080p Långformat (03:12 min) + Högkontrast Hybrid Thumbnail + Komplett Engelsk SEO & ElevenLabs Conversational Voice Affiliate"
)
html = html.replace(
    "<span>1080p Full HD (04:15 min, 7 Scener + Verifierad Kod)</span>",
    "<span>1080p Full HD (03:12 min, 7 Synkade Scener + Verifierad Kod)</span>"
)

# 2. Update package title inside review card
html = html.replace(
    "Build Automated Multilingual AI Video Dubbing in Python (ElevenLabs Dubbing API)",
    "Build Real-Time Voice AI Agents in Python (Sub-400ms WebSockets 2026)"
)

# 3. Update description text
html = html.replace("Manual video translation is dead in B2B.", "Text chatbots with four-second response lags are dead.")

# 4. Replace the 3 pitch cards in HTML
# Find pitchesContainer start and end
start_marker = '<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="pitchesContainer">'
end_marker = '<!-- SECTION 4: SPANADE NYCKELORD'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_pitches_block = '''<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="pitchesContainer">
        
        <!-- PITCH 1 (PITCH #003) -->
        <div class="glass-card rounded-2xl p-5 border border-purple-500/40 hover:border-purple-400/60 transition-all flex flex-col justify-between space-y-4 bg-purple-950/10">
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded font-mono font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30">PITCH #003</span>
              <span class="text-purple-300 font-semibold font-mono">⏱️ Längd: 3:30–4:30 min</span>
            </div>
            
            <h3 class="text-base font-bold text-white hover:text-purple-300 transition">How to Clone Voices and Dub Videos in Python</h3>
            <p class="text-xs text-slate-300 italic">"Translate any video into 29 languages with matching lip cadence and cloned voices in Python."</p>
            
            <!-- Beslutsunderlag Mini-Tabell -->
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between">
                <span class="text-slate-400">Pedagogiskt Mål:</span>
                <span class="text-purple-300 font-semibold text-right">Automatiserad röstkloning & videodubbning</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Sökvolym:</span>
                <span class="text-white font-mono font-semibold">24 500 /mån (+82% MoM)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Målgrupp:</span>
                <span class="text-slate-200">Utvecklare, Skapare & Globala SaaS-team</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Demo Kod:</span>
                <span class="text-purple-400 font-mono">ElevenLabs Dubbing API + FFmpeg</span>
              </div>
              <div class="pt-1 border-t border-slate-800/80 flex justify-between">
                <span class="text-slate-400">Huvud-Affiliate:</span>
                <span class="text-amber-300 font-medium">ElevenLabs Dubbing SDK (22% Recurring)</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex items-center gap-2">
            <button onclick="showPitchDossier(0)" class="flex-1 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 font-semibold transition">
              🔍 Granska Manus & Dossier
            </button>
            <button id="pitchBtn0" onclick="triggerPitch('PITCH #003', 'How to Clone Voices and Dub Videos in Python', this)" class="px-4 py-2 rounded-lg bg-purple-600 hover:bg-purple-500 text-xs font-bold text-white shadow-md shadow-purple-600/30 flex items-center gap-1 transition">
              <span>Exekvera</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </button>
          </div>
        </div>

        <!-- PITCH 2 (PITCH #004) -->
        <div class="glass-card rounded-2xl p-5 border border-emerald-500/30 hover:border-emerald-400/60 transition-all flex flex-col justify-between space-y-4 bg-emerald-950/10">
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">PITCH #004</span>
              <span class="text-emerald-300 font-semibold font-mono">⏱️ Längd: 3:30–4:30 min</span>
            </div>
            
            <h3 class="text-base font-bold text-white hover:text-emerald-300 transition">Build an AI Voice Phone Agent in Python</h3>
            <p class="text-xs text-slate-300 italic">"Kill 'Press 1 for Sales'. Build a sub-500ms conversational phone agent with live database actions."</p>
            
            <!-- Beslutsunderlag Mini-Tabell -->
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between">
                <span class="text-slate-400">Pedagogiskt Mål:</span>
                <span class="text-emerald-300 font-semibold text-right">Ersätt knappval med samtals-AI</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Sökvolym:</span>
                <span class="text-white font-mono font-semibold">38 700 /mån (+94% MoM)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Målgrupp:</span>
                <span class="text-slate-200">Full-Stack Utvecklare & Supportingenjörer</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Demo Kod:</span>
                <span class="text-emerald-400 font-mono">ElevenLabs + Twilio SIP + Python</span>
              </div>
              <div class="pt-1 border-t border-slate-800/80 flex justify-between">
                <span class="text-slate-400">Huvud-Affiliate:</span>
                <span class="text-amber-300 font-medium">ElevenLabs Telephony (22% Recurring)</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex items-center gap-2">
            <button onclick="showPitchDossier(1)" class="flex-1 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 font-semibold transition">
              🔍 Granska Manus & Dossier
            </button>
            <button id="pitchBtn1" onclick="triggerPitch('PITCH #004', 'Build an AI Voice Phone Agent in Python', this)" class="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-xs font-bold text-white shadow-md shadow-emerald-600/30 flex items-center gap-1 transition">
              <span>Exekvera</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </button>
          </div>
        </div>

        <!-- PITCH 3 (PITCH #005) -->
        <div class="glass-card rounded-2xl p-5 border border-cyan-500/30 hover:border-cyan-400/60 transition-all flex flex-col justify-between space-y-4 bg-cyan-950/10">
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">PITCH #005</span>
              <span class="text-cyan-300 font-semibold font-mono">⏱️ Längd: 3:30–4:30 min</span>
            </div>
            
            <h3 class="text-base font-bold text-white hover:text-cyan-300 transition">Turn Any Text Document into Audio Podcasts in Python</h3>
            <p class="text-xs text-slate-300 italic">"Stop reading 40-page manuals. Build an automated dual-speaker podcast pipeline in Python."</p>
            
            <!-- Beslutsunderlag Mini-Tabell -->
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between">
                <span class="text-slate-400">Pedagogiskt Mål:</span>
                <span class="text-cyan-300 font-semibold text-right">Skapa ljudpoddar från textdokument</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Sökvolym:</span>
                <span class="text-white font-mono font-semibold">19 800 /mån (+55% MoM)</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Målgrupp:</span>
                <span class="text-slate-200">Tekniker, Skribenter & Utvecklare</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Demo Kod:</span>
                <span class="text-cyan-400 font-mono">ElevenLabs Audio Native API + Python</span>
              </div>
              <div class="pt-1 border-t border-slate-800/80 flex justify-between">
                <span class="text-slate-400">Huvud-Affiliate:</span>
                <span class="text-amber-300 font-medium">ElevenLabs Creator Tier (22% Recurring)</span>
              </div>
            </div>
          </div>

          <div class="pt-2 flex items-center gap-2">
            <button onclick="showPitchDossier(2)" class="flex-1 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 font-semibold transition">
              🔍 Granska Manus & Dossier
            </button>
            <button id="pitchBtn2" onclick="triggerPitch('PITCH #005', 'Turn Any Text Document into Audio Podcasts in Python', this)" class="px-4 py-2 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-xs font-bold text-white shadow-md shadow-cyan-600/30 flex items-center gap-1 transition">
              <span>Exekvera</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </button>
          </div>
        </div>

      </div>
    </section>

    '''
    html = html[:start_idx] + new_pitches_block + html[end_idx:]

# 5. Update PITCH_DATA in JavaScript
p_js_start = html.find('const PITCH_DATA = [')
p_js_end = html.find('function openThumbnailLightbox()')

if p_js_start != -1 and p_js_end != -1:
    new_pitch_js = '''const PITCH_DATA = [
      {
        id: "PITCH #003",
        duration: "⏱️ Längd: 3:30–4:30 minuter",
        title: "How to Clone Voices and Dub Videos in Python (ElevenLabs Dubbing API)",
        goal: "Lär utvecklare och skapare att auto-översätta och dubba videor till 29 språk med bibehållen röstkaraktär. Använder ElevenLabs Dubbing API och Python FFmpeg för sömlös batch-lokalisering.",
        script_steps: [
          "• Scen 1 (00:00 - 00:30): Smärtpunkten med manuell videoöversättning ($500/video). Introducera 29-språks automatiserad pipeline.",
          "• Scen 2 (00:30 - 01:15): Arkitektur: Diarisering, neural översättning och nollpunkts röstkloning.",
          "• Scen 3 (01:15 - 02:30): Python SDK Setup: Initiera dubbningsjobb och hantera asynkrona webhooks.",
          "• Scen 4 (02:30 - 03:30): Live Rendering: FFmpeg sammansättning och kvalitetssäkring.",
          "• Scen 5 (03:30 - 04:15): Outro med talad ElevenLabs gratis provperiod, GitHub och nästa video."
        ],
        trend: "Sökvolym: 24 500 sökningar/månad (+82% MoM). Global video-lokalisering exploderar i efterfrågan.",
        code: "ElevenLabs Dubbing API + Python FFmpeg wrapper för automatisk batch-lokalisering av MP4-videor.",
        affiliates: [
          "• ElevenLabs AI Dubbing SDK: 22% Recurring Commission via PartnerStack",
          "• FFmpeg Python Open-Source Toolkit"
        ]
      },
      {
        id: "PITCH #004",
        duration: "⏱️ Längd: 3:30–4:30 minuter",
        title: "Build an AI Voice Phone Agent in Python (ElevenLabs + Twilio)",
        goal: "Skrota förlegade knappvalsmenyer och ersätt dem med en mänsklig samtalsagent i telefonväxeln som svarar på under 500ms och utför live databasoperationer under pågående samtal.",
        script_steps: [
          "• Scen 1 (00:00 - 00:30): Varför kunder avskyr telefonköer: Demo av traditionell meny vs sub-500ms samtals-AI.",
          "• Scen 2 (00:30 - 01:15): Arkitektur: Twilio SIP Media Streams kopplat till ElevenLabs Conversational WebSockets.",
          "• Scen 3 (01:15 - 02:30): Python & WebSockets: Hantera tvåvägs 8kHz/16kHz PCM-ljudström i realtid.",
          "• Scen 4 (02:30 - 03:30): Live CRM-verktyg: Låt AI:n slå upp ordrar och boka möten under samtalets gång.",
          "• Scen 5 (03:30 - 04:15): Outro med talad ElevenLabs gratis provperiod, GitHub och nästa video."
        ],
        trend: "Sökvolym: 38 700 sökningar/månad (+94% MoM). Företag moderniserar sina telefonväxlar med samtals-AI.",
        code: "Twilio Voice Media Stream bryggad till ElevenLabs Conversational AI i Python med live CRM-funktionsanrop.",
        affiliates: [
          "• ElevenLabs Telephony & Conversational AI: 22% Recurring Commission via PartnerStack",
          "• Twilio Cloud Telephony: API för SIP trunking och telefonnummer"
        ]
      },
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
      }
    ];

    '''
    html = html[:p_js_start] + new_pitch_js + html[p_js_end:]

html_path.write_text(html, encoding="utf-8")
print("Successfully updated docs/index.html with Video 002.1 and Pitches 3, 4, 5!")
