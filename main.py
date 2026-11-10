from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
tagline = "Enter AI agents and programs in contests, climb the ranks, and win cash prizes."
(output_dir / "entry.txt").write_text(tagline, encoding="utf-8")
