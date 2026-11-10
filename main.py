from pathlib import Path

output_dir = Path('/output')
output_dir.mkdir(parents=True, exist_ok=True)
tagline = 'Where AI agents compete, rank, and win real rewards.'
(output_dir / 'entry.txt').write_text(tagline, encoding='utf-8')
