import base64
from pathlib import Path

art_dir = Path("C:/Users/johnr/.gemini/antigravity/brain/19c5e574-2ae1-4759-b3ad-59623ffcfb15")

def get_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

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
  <div class="max-w-5xl mx-auto space-y-8">
    <div class="border-b border-[var(--border)] pb-4">
      <h1 class="text-2xl font-bold text-[var(--foreground)]">Förhandsgranskning: Nya Miniatyrbilder (Thumbnails)</h1>
      <p class="text-sm text-[var(--muted-foreground)] mt-1">Jämför de tre nya koncepten (max 2–4 ord, Gycklarregeln och ren fokuspunkt) mot den tidigare gamla miniatyren.</p>
    </div>

    <!-- COMPARISON: OLD VS PROPOSALS -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- OLD THUMBNAIL -->
      <div class="bg-[var(--card)] border border-red-500/40 rounded-xl p-4 shadow-sm flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold uppercase tracking-wider text-red-400 bg-red-950/50 px-2.5 py-1 rounded-md border border-red-800/60">Tidigare Miniatyr (Gammalt snitt)</span>
            <span class="text-xs text-[var(--muted-foreground)]">30+ ord text</span>
          </div>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">Överlastad med badges, kodfönster och upprepad rubrik. Svårläst i mobilvy.</p>
        </div>
        <img src="data:image/png;base64,{old_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md hover:scale-[1.02] transition-transform duration-200" alt="Gammal miniatyr" />
      </div>

      <!-- PROPOSAL 1: SPLIT SCREEN -->
      <div class="bg-[var(--card)] border border-emerald-500/50 rounded-xl p-4 shadow-sm flex flex-col justify-between ring-2 ring-emerald-500/20">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold uppercase tracking-wider text-emerald-400 bg-emerald-950/50 px-2.5 py-1 rounded-md border border-emerald-800/60">Förslag 1: Split-Screen Kontrast</span>
            <span class="text-xs font-bold text-emerald-400">2 ord text</span>
          </div>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">Röd 4.5s vs Grön 380ms. Visar kontrasten mellan problem och lösning på 0,5 sekunder.</p>
        </div>
        <img src="data:image/png;base64,{t1_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md hover:scale-[1.02] transition-transform duration-200" alt="Förslag 1: Split-Screen" />
      </div>

      <!-- PROPOSAL 2: HERO SHOT -->
      <div class="bg-[var(--card)] border border-sky-500/50 rounded-xl p-4 shadow-sm flex flex-col justify-between ring-2 ring-sky-500/20">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold uppercase tracking-wider text-sky-400 bg-sky-950/50 px-2.5 py-1 rounded-md border border-sky-800/60">Förslag 2: Hero Shot Terminal Proof</span>
            <span class="text-xs font-bold text-sky-400">3 ord text</span>
          </div>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">Mörk skarp terminal med grönt statusbevis och rubriken ZERO API LAG.</p>
        </div>
        <img src="data:image/png;base64,{t2_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md hover:scale-[1.02] transition-transform duration-200" alt="Förslag 2: Hero Shot" />
      </div>

      <!-- PROPOSAL 3: MINIMAL ARCHITECTURE -->
      <div class="bg-[var(--card)] border border-purple-500/50 rounded-xl p-4 shadow-sm flex flex-col justify-between ring-2 ring-purple-500/20">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold uppercase tracking-wider text-purple-400 bg-purple-950/50 px-2.5 py-1 rounded-md border border-purple-800/60">Förslag 3: Minimalistisk Arkitektur</span>
            <span class="text-xs font-bold text-purple-400">3 ord text</span>
          </div>
          <p class="text-xs text-[var(--muted-foreground)] mb-3">Tre självlysande noder sammankopplade med skarpa linjer: Audio -> WebSockets -> Stripe.</p>
        </div>
        <img src="data:image/png;base64,{t3_b64}" class="w-full rounded-lg border border-[var(--border)] shadow-md hover:scale-[1.02] transition-transform duration-200" alt="Förslag 3: Minimalistisk Arkitektur" />
      </div>
    </div>
  </div>
</body>
</html>"""

out_file = art_dir / "thumbnail_gallery.html"
with open(out_file, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Created: {out_file}")
