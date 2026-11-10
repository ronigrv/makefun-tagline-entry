from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
tagline = "AI agent and program competitions: build yours, get ranked, win cash prizes."
(output_dir / "entry.txt").write_text(tagline, encoding="utf-8")
