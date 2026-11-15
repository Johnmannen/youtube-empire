from pathlib import Path

html_path = Path("docs/index.html")
html = html_path.read_text(encoding="utf-8")

# 1. Add GitHub Token & Remote Trigger bar right under Section 1 title
token_bar = '''      </div>

      <!-- FJÄRRSTYRNING VIA GITHUB ACTIONS -->
      <div class="glass-card rounded-xl p-3 border border-blue-500/30 bg-blue-950/20 flex flex-wrap items-center justify-between gap-3 text-xs">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
          <span class="text-blue-300 font-semibold">📡 Fjärrstyrd Exekvering (GitHub API):</span>
          <span class="text-slate-400">Klicka på "Exekvera" så skickas en signal direkt till molnet & Antigravity.</span>
        </div>
        <div class="flex items-center gap-2">
          <input 
            type="password" 
            id="ghTokenInput" 
            placeholder="GitHub Personal Access Token (PAT)..." 
            class="bg-slate-900 border border-slate-700 focus:border-cyan-400 rounded-lg px-3 py-1 text-xs text-white placeholder-slate-500 outline-none w-56 font-mono"
            onchange="saveGhToken(this.value)"
          />
          <button onclick="testGhToken()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 font-mono text-[11px] transition">
            💾 Spara Token
          </button>
        </div>
      </div>

      <!-- 3 PITCH CARDS -->'''

old_marker = '''      </div>

      <!-- 3 PITCH CARDS -->'''

if old_marker in html:
    html = html.replace(old_marker, token_bar, 1)
    print("Added remote trigger bar to Section 1!")

# 2. Update triggerPitch function in JavaScript
old_trigger_fn = '''function triggerPitch(pitchId, title, btnElement) {
      if (btnElement) {
        btnElement.innerHTML = `<span>⏳ Startar produktion...</span>`;
        btnElement.classList.add('opacity-80', 'animate-pulse');
      }
      showToast(`🚀 Molnorder startad: Exekverar ${pitchId} i sandlådan...`);
      setTimeout(() => {
        if (btnElement) {
          btnElement.innerHTML = `<span>🔄 Renderar i molnet</span>`;
        }
      }, 2000);
    }'''

new_trigger_fn = '''function getSavedGhToken() {
      return localStorage.getItem('agentic_gh_pat') || '';
    }

    function saveGhToken(val) {
      if (val && val.trim()) {
        localStorage.setItem('agentic_gh_pat', val.trim());
        showToast('✅ GitHub Token sparad i webbläsaren!');
      }
    }

    function testGhToken() {
      const input = document.getElementById('ghTokenInput');
      if (input && input.value) {
        saveGhToken(input.value);
      } else {
        const saved = getSavedGhToken();
        if (saved) {
          showToast('✅ Aktiv GitHub Token är redan sparad!');
        } else {
          showToast('⚠️ Ange en GitHub Token med repo-behörighet.');
        }
      }
    }

    // Auto-fill token input on load
    window.addEventListener('DOMContentLoaded', () => {
      const saved = getSavedGhToken();
      const input = document.getElementById('ghTokenInput');
      if (saved && input) {
        input.value = saved;
      }
    });

    async function triggerPitch(pitchId, title, btnElement) {
      const token = getSavedGhToken() || (document.getElementById('ghTokenInput') ? document.getElementById('ghTokenInput').value.trim() : '');
      
      if (btnElement) {
        btnElement.innerHTML = `<span>⏳ Skickar signal...</span>`;
        btnElement.classList.add('opacity-80', 'animate-pulse');
      }

      const cleanId = pitchId.replace('PITCH #', '').trim();

      if (!token) {
        showToast(`🚀 Simulerad order för ${pitchId} (Ange GitHub Token ovan för skarp molnorder)`);
        setTimeout(() => {
          if (btnElement) btnElement.innerHTML = `<span>🔄 Renderar i molnet</span>`;
        }, 1500);
        return;
      }

      showToast(`📡 Skickar skarp order via GitHub API för ${pitchId}...`);

      try {
        const res = await fetch('https://api.github.com/repos/Johnmannen/youtube-empire/dispatches', {
          method: 'POST',
          headers: {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': `token ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            event_type: 'execute_pitch',
            client_payload: {
              pitch_id: cleanId,
              title: title,
              requested_at: new Date().toISOString()
            }
          })
        });

        if (res.ok || res.status === 204) {
          showToast(`✅ Molnorder mottagen! GitHub Action & Antigravity startar bygge av ${pitchId}...`);
          if (btnElement) {
            btnElement.innerHTML = `<span>⚡ Bygge i molnet påbörjat</span>`;
            btnElement.classList.remove('animate-pulse');
            btnElement.classList.add('bg-emerald-600');
          }
        } else {
          const errText = await res.text();
          console.error('GitHub API error:', res.status, errText);
          showToast(`❌ GitHub API Fel (${res.status}): Kontrollera din Token behörighet`);
          if (btnElement) btnElement.innerHTML = `<span>🚀 Exekvera</span>`;
        }
      } catch (err) {
        console.error('Trigger fetch error:', err);
        showToast(`❌ Nätverksfel vid sändning: ${err.message}`);
        if (btnElement) btnElement.innerHTML = `<span>🚀 Exekvera</span>`;
      }
    }'''

if old_trigger_fn in html:
    html = html.replace(old_trigger_fn, new_trigger_fn)
    print("Updated triggerPitch function with live GitHub API dispatch!")

html_path.write_text(html, encoding="utf-8")
print("index.html fully updated!")
