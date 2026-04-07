# DS Emulator — Python + py-desmume

A Nintendo DS emulator launcher written in Python using py-desmume, with custom keybindings and save state support.

## Requirements

- Python 3.7+
- py-desmume
- pynput

## Installation

Run this once to install dependencies:

\```python
import sys, subprocess
subprocess.run([sys.executable, "-m", "pip", "install", "py-desmume"])
subprocess.run([sys.executable, "-m", "pip", "install", "pynput"])
\```

> **Note for Mac users:** pygame will fail to build without Xcode tools — use pynput instead (already handled above)

## Setup

1. Clone this repo
2. Add your `.nds` ROM file anywhere on your system
3. Edit the ROM path in `dsemulator.py`:
\```python
emu.open("/your/path/to/game.nds")
\```
4. Edit the save state path if needed:
\```python
SAVE_STATE_FILE = "/your/path/to/savestate.dst"
\```
5. Run `dsemulator.py` in VS Code or any Python environment

## Controls

| Key | Action |
|-----|--------|
| W | D-Pad Up |
| A | D-Pad Left |
| S | D-Pad Down |
| D | D-Pad Right |
| Up Arrow | A Button |
| Down Arrow | B Button |
| Left Arrow | X Button |
| Right Arrow | Y Button |
| F5 | Save State |
| F9 | Load State |

## Saves

There are two types of saves:

- **In-game saves** — happen automatically when the game saves (e.g. saving at a Pokemon Center). Stored as a `.dsv` file next to your ROM
- **Save states** — manual snapshots triggered with F5/F9. Stored as a `.dst` file at your defined save path

## Notes

- Tested on macOS with Python 3.13 and py-desmume 0.0.9
- ROMs are not included — you must provide your own
- Only use ROMs for games you legally own

## License

MIT
