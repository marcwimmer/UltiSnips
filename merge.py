#!/usr/bin/env python3
# https://github.com/erietz/ultisnips-vscode
import subprocess
from pathlib import Path
import sys
import os
import inspect
import os
from pathlib import Path
import inspect
import os
from pathlib import Path
import inspect
import os
from pathlib import Path
import json

current_dir = Path(
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
)
conf_file = Path(os.path.expanduser("~/.vscode/ultisnips-vscode.json"))
if not conf_file.exists():
    conf_file.parent.mkdir(parents=True, exist_ok=True)
    print("Uses configuration file in {conf_file}")
    SAMPLE_CONTENT = json.dumps(
        {
            "ultisnips-snippets": str(current_dir),
            "vscode-snippets": "~/Library/Application Support/Code/User/snippets/",
        },
        indent=4,
    )
    conf_file.write_text(SAMPLE_CONTENT)

collected = {}

for file in current_dir.glob("*.snippets"):
    if "_" not in file.name:
        continue
    base = file.name.split("_")[0]
    collected.setdefault(base, [])
    collected[base].append(file)

for base, paths in collected.items():
    content = ""
    for file in paths:
        content += file.read_text() + "\n"
    file = current_dir / f"{base}.snippets"
    file.write_text(content)

# use https://github.com/erietz/ultisnips-vscode to convert to vscode
subprocess.check_call("ultisnips2vscode")
