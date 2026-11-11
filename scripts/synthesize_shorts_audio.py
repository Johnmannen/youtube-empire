import asyncio
import subprocess
from pathlib import Path
import edge_tts

text_p1 = "Text chatbots with four-second response lags are dead."
text_p2 = "Here is how to build a real-time conversational voice agent in Python with sub-four-hundred millisecond latency using ElevenLabs WebSockets."
text_p3 = "Grab the free trial and full Python code in the description!"

out_dir = Path("build_temp/shorts_002_1")
out_dir.mkdir(parents=True, exist_ok=True)

async def run():
    parts = []
    for i, t in enumerate([text_p1, text_p2, text_p3]):
        f = out_dir / f"part_{i}.mp3"
        for attempt in range(5):
            try:
                c = edge_tts.Communicate(t, "en-US-AndrewMultilingualNeural", rate="+6%")
                await c.save(str(f))
                print(f"Part {i}: {f.stat().st_size} bytes")
                parts.append(f)
                break
            except Exception as e:
                print(f"Retry {attempt+1} for part {i}: {e}")
                await asyncio.sleep(2)

    concat_file = out_dir / "concat_audio.txt"
    with open(concat_file, "w", encoding="utf-8") as lf:
        for p in parts:
            lf.write(f"file '{p.resolve().as_posix()}'\n")

    out_merged = out_dir / "short_audio_andrew.mp3"
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file), "-c", "copy", str(out_merged)]
    subprocess.run(cmd, check=True)
    print("Merged shorts voice! Size:", out_merged.stat().st_size)

if __name__ == "__main__":
    asyncio.run(run())
