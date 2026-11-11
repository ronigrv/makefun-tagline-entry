from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
tagline = (
    "The competition platform for AI agents and programs: "
    "get ranked and win cash prizes."
)
(output_dir / "entry.txt").write_text(tagline, encoding="utf-8")
