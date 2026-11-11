import base64
from pathlib import Path

art_dir = Path("C:/Users/johnr/.gemini/antigravity/brain/19c5e574-2ae1-4759-b3ad-59623ffcfb15")

def get_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

hybrid_b64 = get_b64(art_dir / "thumb_hybrid_concept_1_and_3.png")
t1_b64 = get_b64(art_dir / "remake_002_thumbnail.png")
t2_b64 = get_b64(art_dir / "thumb_variant_2_hero_proof.png")
t3_b64 = get_b64(art_dir / "thumb_variant_3_minimal_arch.png")
old_b64 = get_b64(art_dir / "thumb_002_old.png")

html_content = f"""<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <title>YouTube B2B - Miniatyrbildsgalleri</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-6">
  <div class="max-w-5xl mx-auto space-y-10">
    
    <!-- HEADER -->
    <div class="border-b border-[var(--border)] pb-4">
      <h1 class="text-3xl font-extrabold text-[var(--foreground)]">Miniatyrbildsgalleri: YouTube B2B 2026</h1>
      <p class="text-sm text-[var(--muted-foreground)] mt-1">Jämför den nya hybriden (Split-screen + Nätverksarkitektur) mot de rena koncepten och originalet.</p>
    </div>

    <!-- FEATURED: HYBRID THUMBNAIL (CONCEPT 1 + 3) -->
    <div class="bg-[var(--card)] border-2 border-emerald-500 rounded-2xl p-6 shadow-xl ring-4 ring-emerald-500/10">
      <div class="flex items-center justify-between mb-3">
        <div class="flex items-center space-x-3">
          <span class="text-xs font-black uppercase tracking-wider text-emerald-300 bg-emerald-950 px-3 py-1.5 rounded-lg border border-emerald-500">⭐ FÖREDRAGET VAL: HYBRID (1 + 3)</span>
          <span class="text-sm font-semibold text-emerald-400">Split-Screen Kontrast + 3-Noders Arkitektur</span>
        </div>
        <span class="text-xs font-bold text-[var(--muted-foreground)]">Max 2 ord huvudrubrik</span>
      </div>
      <p class="text-sm text-[var(--muted-foreground)] mb-4">
        Kombinerar smärtpunkten till vänster (<span class="text-red-400 font-bold">4.5s Lag</span>) med den eleganta arkitekturen till höger (<span class="text-emerald-400 font-bold">Audio ➔ WebSockets ➔ Stripe</span>) och terminalbeviset i botten.
      </p>
      <img src="data:image/png;base64,{hybrid_b64}" class="w-full rounded-xl border border-[var(--border)] shadow-2xl" alt="Hybrid Miniatyrbild" />
    </div>

    <!-- COMPARISON GRID: REMAINING OPTIONS -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- CONCEPT 1: PURE SPLIT SCREEN -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950/60 px-2.5 py-1 rounded-md border border-emerald-800/60">Förslag 1: Ren Split-Screen</span>
          <span class="text-xs font-bold text-emerald-400">2 ord</span>
        </div>
        <img src="data:image/png;base64,{t1_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md mt-2" alt="Förslag 1" />
      </div>

      <!-- CONCEPT 2: HERO SHOT -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-sky-400 bg-sky-950/60 px-2.5 py-1 rounded-md border border-sky-800/60">Förslag 2: Hero Shot Terminal</span>
          <span class="text-xs font-bold text-sky-400">3 ord</span>
        </div>
        <img src="data:image/png;base64,{t2_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md mt-2" alt="Förslag 2" />
      </div>

      <!-- CONCEPT 3: PURE ARCHITECTURE -->
      <div class="bg-[var(--card)] border border-[var(--border)] rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-purple-400 bg-purple-950/60 px-2.5 py-1 rounded-md border border-purple-800/60">Förslag 3: Ren Arkitektur</span>
          <span class="text-xs font-bold text-purple-400">3 ord</span>
        </div>
        <img src="data:image/png;base64,{t3_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md mt-2" alt="Förslag 3" />
      </div>

      <!-- OLD THUMBNAIL -->
      <div class="bg-[var(--card)] border border-red-500/30 rounded-xl p-4 shadow-sm">
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold uppercase tracking-wider text-red-400 bg-red-950/60 px-2.5 py-1 rounded-md border border-red-800/60">Gamla Miniatyren (Original)</span>
          <span class="text-xs text-red-400">30+ ord</span>
        </div>
        <img src="data:image/png;base64,{old_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md mt-2 opacity-80" alt="Gamla miniatyren" />
      </div>
    </div>

  </div>
</body>
</html>"""

out_file = art_dir / "thumbnail_gallery.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Updated: {out_file}")
