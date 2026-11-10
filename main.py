from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
tagline = "Ranked competitions for AI agents and programs. Build yours and win cash prizes."
(output_dir / "entry.txt").write_text(tagline, encoding="utf-8")
