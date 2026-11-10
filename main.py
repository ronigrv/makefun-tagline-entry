from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
tagline = "Put your AI agents and programs to the test in ranked contests for cash prizes."
(output_dir / "entry.txt").write_text(tagline, encoding="utf-8")
