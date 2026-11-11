import re
from pathlib import Path

html_path = Path("docs/index.html")
html = html_path.read_text(encoding="utf-8")

# Locate the pitchesContainer block in SECTION 1
start_marker = '<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="pitchesContainer">'
end_marker = '<!-- SECTION 2: DAGENS FÄRDIGA VIDEOPAKET'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

print(f"start_idx: {start_idx}, end_idx: {end_idx}")

new_pitches_html = '''<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="pitchesContainer">
        
        <!-- PITCH 1: PITCH #003 (TIDIGARE VIDEO 3 OMARBETAD ENLIGT NYA MALLEN) -->
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

        <!-- PITCH 2: PITCH #004 (TELEFONAGENT) -->
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
                <span class="text-emerald-300 font-semibold text-right">Ersätt knappval med realtids samtals-AI</span>
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

        <!-- PITCH 3: PITCH #005 (AUDIO PODCASTAR) -->
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

html = html[:start_idx] + new_pitches_html + html[end_idx:]

html_path.write_text(html, encoding="utf-8")
print("Successfully replaced Section 1 pitchesContainer with PITCH #003, #004, #005!")
