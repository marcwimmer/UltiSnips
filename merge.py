#!/usr/bin/env python3
#https://github.com/erietz/ultisnips-vscode
from pathlib import Path
import sys
import os
import inspect
import os
from pathlib import Path
import inspect
import os
from pathlib import Path
current_dir = Path(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

collected = {}

for file in Path(current_dir).glob("*.snippets"):
    if '_' not in file.name:
        continue
    base = file.name.split("_")[0]
    collected.setdefault(base, [])
    collected[base].append(file)

for base, paths in collected.items():
    content = ""
    for file in paths:
        content += file.read_text() + '\n'
    file = Path(current_dir) / f"{base}.snippets"
    file.write_text(content)

# use https://github.com/erietz/ultisnips-vscode to convert to vscode
os.system("ultisnips_to_vscode")
