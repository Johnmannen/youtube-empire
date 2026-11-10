# Affiliate-strategi & Partnerprogram för AI & Agentic Stack B2B

Detta dokument är en komplett, verifierad guide för att monetarisera din kanal **Agentic Stack B2B** (`johnmannen.github.io/youtube-empire`) från Dag 1 via 4 kontrollerade affiliate-lösningar med PayPal-utbetalning.

---

## 1. Jämförelsetabell: Verifierade Partnerprogram

| Program & Verktyg | Kategori & Relevans | Ersättningsmodell | Utbetalning | Verifierad Huvudlänk | Direkt Portal / Ansökan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Make.com** | Visual AI Automation & API-kopplingar | **20 % löpande (recurring)** i upp till 24 mån | **PayPal** (via PartnerStack) | [make.com/en/affiliate](https://www.make.com/en/affiliate) | PartnerStack Portal |
| **2. Voiceflow** | Visual AI Agent Builder | **20 % löpande (recurring)** så länge kunden abonnerar | **PayPal** (via FirstPromoter) | [voiceflow.com/partners](https://www.voiceflow.com/partners) | [voiceflow.firstpromoter.com](https://voiceflow.firstpromoter.com/) |
| **3. ElevenLabs** | AI Voice Generation & Audio API | **30 % – 40 % löpande (recurring)** per prenumerant | **PayPal** (via FirstPromoter) | [elevenlabs.io/affiliates](https://elevenlabs.io/affiliates) | [elevenlabs.firstpromoter.com](https://elevenlabs.firstpromoter.com/) |
| **4. Hostinger (VPS)** | 24/7 Python & Docker Server Hosting | **40 % – 60 % engångsbelopp** ($40–$120 per kund) | **PayPal** (Min. $100) | [hostinger.com/affiliates](https://www.hostinger.com/affiliates) | Direct Affiliate Portal |

---

## 2. Detaljerad Genomgång av Ersättning & Villkor

### 1. Make.com (Huvudpartner för Automatisering)
- **Varför den passar:** Tittare som ser videor om AI-agenter vill koppla ihop sina skript med Slack, Google Sheets, Notion och LLM-API:er. Make är branschstandarden.
- **Ersättning:** 20 % av månadsavgiften för varje betalande användare (Core $9/mån, Pro $16/mån, Teams $29/mån).
- **Utbetalning:** Betalas ut via **PayPal** eller Stripe via nätverket PartnerStack (minsta utbetalningsgräns $25).
- **Landningssida:** `https://www.make.com/en/affiliate`
- **Registrering:** Ansök direkt på sidan så skapas ett konto i PartnerStack.

---

### 2. Voiceflow (Huvudpartner för Visuella AI-agenter)
- **Varför den passar:** Voiceflow är det ledande verktyget för att rita och bygga autonoma conversational agents.
- **Ersättning:** 20 % livslång löpande provision på alla betalda planer (Pro-planer startar på $50/mån, vilket ger dig $10/mån per aktiv kund).
- **Utbetalning:** Betalas ut månadsvis till ditt **PayPal-konto** via FirstPromoter (minsta utbetalning $50).
- **Landningssida:** `https://www.voiceflow.com/partners`
- **Direkt registreringslänk för affiliatenätverket:** `https://voiceflow.firstpromoter.com/`

---

### 3. ElevenLabs (Huvudpartner för AI-Röst & Ljud-API)
- **Varför den passar:** Du använder själv `edge-tts` gratis, men visar i videorna hur tittarna kan skala upp till ElevenLabs API för professionella röstagenter.
- **Ersättning:** 30 % till 40 % löpande månadsprovision på alla abonnemang (Creator/Independent/Business).
- **Utbetalning:** Betalas ut varje månad direkt till ditt **PayPal-konto** via FirstPromoter.
- **Landningssida:** `https://elevenlabs.io/affiliates`
- **Direkt registreringslänk:** `https://elevenlabs.firstpromoter.com/`

---

### 4. Hostinger VPS (Huvudpartner för 24/7 Python & Cloud Host)
- **Varför den passar:** När du bygger en AI-agent i Python (`CrewAI`, `LangChain`, `AutoGen`) behöver tittarna en billig Linux VPS-server i molnet som kör koden dygnet runt.
- **Ersättning:** Hög engångsprovision på **40 % till 60 %** per sålt VPS-paket (ger direkt ca $40–$100 per köp).
- **Utbetalning:** Betalas ut via **PayPal** eller direkt banköverföring (minsta utbetalningsgräns $100, 45 dagars godkännandeperiod).
- **Landningssida:** `https://www.hostinger.com/affiliates`

---

## 3. Steg-för-Steg: Registrera konton på 10 minuter

1. **Voiceflow & ElevenLabs (Snabbalternativ via FirstPromoter):**
   - Gå direkt till [voiceflow.firstpromoter.com](https://voiceflow.firstpromoter.com/) och fyll i namn, e-post och ditt PayPal-konto.
   - Gå direkt till [elevenlabs.firstpromoter.com](https://elevenlabs.firstpromoter.com/) och fyll i samma uppgifter.

2. **Make.com (PartnerStack):**
   - Gå till [make.com/en/affiliate](https://www.make.com/en/affiliate) -> Klicka på *Apply Now*.
   - Ange din YouTube-URL eller din GitHub Pages-länk (`https://johnmannen.github.io/youtube-empire/`).
   - Lägg in din PayPal-adress under *Payout Settings* i PartnerStack-profilen.

3. **Hostinger (Affiliate Portal):**
   - Gå till [hostinger.com/affiliates](https://www.hostinger.com/affiliates) -> Klicka på *Access Affiliate Portal*.
   - Välj "Technology / YouTube" som din huvudsakliga trafikkälla.

---

## 4. Uppdaterad JSON-konfiguration för din Kontrollpanel

När du fått dina koder klistrar du in dem i `docs/dashboard_state.json` eller ber Antigravity klistra in dem åt dig:

```json
{
  "affiliate_links": {
    "make_automation": {
      "name": "Make.com (AI Workflows)",
      "url": "https://www.make.com/en/register?pc=DIN_KOD",
      "call_to_action": "Build AI Workflows & Connect APIs with Make (Free Trial):"
    },
    "voiceflow_agents": {
      "name": "Voiceflow (AI Agent Builder)",
      "url": "https://voiceflow.firstpromoter.com/ref/DIN_KOD",
      "call_to_action": "Build Visual Autonomous AI Agents with Voiceflow:"
    },
    "elevenlabs_voice": {
      "name": "ElevenLabs (AI Voice API)",
      "url": "https://elevenlabs.firstpromoter.com/ref/DIN_KOD",
      "call_to_action": "Get Hyper-Realistic AI Voices & Audio APIs:"
    },
    "hostinger_vps": {
      "name": "Hostinger VPS (24/7 Python Server)",
      "url": "https://www.hostinger.com/vps?REFERRAL_CODE",
      "call_to_action": "Host your Python AI Agents 24/7 on cheap VPS:"
    }
  }
}
```

---

## 5. Slutgiltigt utseende i din Videobeskrivning

```text
🚀 LINKS & RESOURCES MENTIONED IN THIS VIDEO:

🔹 Build AI Workflows & Connect APIs with Make (Free Trial):
https://www.make.com/en/register?pc=YOUR_CODE

🔹 Build Visual Autonomous AI Agents with Voiceflow:
https://voiceflow.firstpromoter.com/ref/YOUR_CODE

🔹 Hyper-Realistic AI Voices & Audio APIs with ElevenLabs:
https://elevenlabs.firstpromoter.com/ref/YOUR_CODE

🔹 Deploy your Python AI Agents 24/7 on a VPS:
https://www.hostinger.com/vps?REFERRAL_CODE

---------------------------------------------------
💻 SOURCE CODE & AGENT BLUEPRINTS:
Download all Python scripts & blueprints: https://johnmannen.github.io/youtube-empire/

DISCLOSURE: Some links above are affiliate links. If you purchase a paid plan through them, this channel receives a small commission at no extra cost to you.
```