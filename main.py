from pathlib import Path

destination = Path('/output')
destination.mkdir(parents=True, exist_ok=True)
line = 'AI agent and program competitions: build yours, get ranked, win cash prizes.'
(destination / 'entry.txt').write_text(line, encoding='utf-8')
