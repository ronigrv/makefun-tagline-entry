from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
tagline = "AI agents and programs face off in ranked competitions for cash prizes."
(output_dir / "entry.txt").write_text(tagline, encoding="utf-8")
