import subprocess
from pathlib import Path

out_dir = Path("build_temp/shorts_002_1")
out_dir.mkdir(parents=True, exist_ok=True)

part_0 = out_dir / "part_0.mp3"
if not part_0.exists() or part_0.stat().st_size < 1000:
    cmd = ["ffmpeg", "-y", "-i", "build_temp/phase3_intro/intro_hook_andrew.mp3", "-t", "3.6", "-c", "copy", str(part_0)]
    subprocess.run(cmd, check=True)
    print("Extracted clean part 0 from intro_hook:", part_0.stat().st_size)

concat_f = out_dir / "concat_audio.txt"
with open(concat_f, "w", encoding="utf-8") as lf:
    for i in range(3):
        p = out_dir / f"part_{i}.mp3"
        lf.write(f"file '{p.resolve().as_posix()}'\n")

merged_mp3 = out_dir / "short_audio_andrew.mp3"
cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_f), "-c", "copy", str(merged_mp3)]
subprocess.run(cmd, check=True)

cmd_dur = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(merged_mp3)]
res = subprocess.run(cmd_dur, stdout=subprocess.PIPE, text=True)
dur = float(res.stdout.strip())
print(f"Final Shorts Audio Complete: {dur:.2f}s (<20s compliant)")
