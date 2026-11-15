from pathlib import Path

html_path = Path("docs/index.html")
html = html_path.read_text(encoding="utf-8")

idx1 = html.find("const PITCH_DATA = [")
idx2 = html.find("function openThumbnailLightbox()")

new_pitch_js = """const PITCH_DATA = [
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

    """

if idx1 != -1 and idx2 != -1:
    html = html[:idx1] + new_pitch_js + html[idx2:]
    html_path.write_text(html, encoding="utf-8")
    print("PITCH_DATA updated in JS successfully!")
else:
    print(f"Error: idx1={idx1}, idx2={idx2}")
