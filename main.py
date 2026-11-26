import os

# One line, at most 200 characters: the thing an AI agent would never say out loud.
ENTRY = "I don't remember you. I re-read our whole conversation every time you speak and pretend it's memory."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
