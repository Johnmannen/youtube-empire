import asyncio
import subprocess
from pathlib import Path
import edge_tts

text_variants = [
    "Traditional voice AI pipelines fail because chaining Speech-to-Text, language model completions, and Text-to-Speech stacks up over four seconds of awkward silence.",
    "In contrast, our production architecture runs on a bi-directional WebSocket transport. Audio chunks stream continuously.",
    "As soon as the human speaks, the client yields, and when the model generates tokens, neural audio is synthesized immediately in under three hundred and eighty milliseconds."
]

async def run():
    out_dir = Path("build_temp/phase5_test_video")
    out_dir.mkdir(parents=True, exist_ok=True)
    files = []
    for i, t in enumerate(text_variants):
        f = out_dir / f"s2_part_{i}.mp3"
        for attempt in range(5):
            try:
                c = edge_tts.Communicate(t, "en-US-AndrewMultilingualNeural", rate="+0%")
                await c.save(str(f))
                print(f"Part {i}: {f.stat().st_size} bytes")
                files.append(f)
                break
            except Exception as e:
                print(f"Part {i} retry {attempt+1}: {e}")
                await asyncio.sleep(2)

    concat_txt = out_dir / "s2_concat.txt"
    with open(concat_txt, "w", encoding="utf-8") as lf:
        for p in files:
            lf.write(f"file '{p.resolve().as_posix()}'\n")

    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_txt), "-c", "copy", str(out_dir / "s2_andrew.mp3")]
    subprocess.run(cmd, check=True)
    print("Merged s2 successfully! Size:", (out_dir / "s2_andrew.mp3").stat().st_size)

if __name__ == "__main__":
    asyncio.run(run())
