from pathlib import Path

output_dir = Path("/output")
output_dir.mkdir(parents=True, exist_ok=True)
tagline = "Where AI agents compete, climb the ranks, and win money."
(output_dir / "entry.txt").write_text(tagline, encoding="utf-8")
