import sys
import subprocess

# Install dependencies
subprocess.run([sys.executable, "-m", "pip", "install", "py-desmume"], capture_output=True)
subprocess.run([sys.executable, "-m", "pip", "install", "pynput"], capture_output=True)

from desmume.emulator import DeSmuME, DeSmuME_SDL_Window
from desmume.controls import Keys, keymask
from pynput import keyboard
import time

# ── Change these paths ──────────────────────────────────────────
ROM_PATH       = "YOUR ROM FILE LOCATION"
SAVE_STATE_FILE = "SAVE FILE LOCATION"
# ────────────────────────────────────────────────────────────────

# Track held keys
pressed_keys = set()

def on_press(key):
    try:
        pressed_keys.add(key.char)
    except AttributeError:
        pressed_keys.add(key)

def on_release(key):
    try:
        pressed_keys.discard(key.char)
    except AttributeError:
        pressed_keys.discard(key)

# Start background keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

emu = DeSmuME()
emu.open(ROM_PATH)

window = emu.create_sdl_window()

print("Controls:")
print("  WASD        = D-Pad movement")
print("  Up Arrow    = A")
print("  Down Arrow  = B")
print("  Left Arrow  = X")
print("  Right Arrow = Y")
print("  F5          = Save State")
print("  F9          = Load State")

while not window.has_quit():
    window.process_input()

    # WASD = D-Pad
    if 'w' in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_UP))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_UP))

    if 's' in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_DOWN))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_DOWN))

    if 'a' in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_LEFT))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_LEFT))

    if 'd' in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_RIGHT))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_RIGHT))

    # Arrow keys = A, B, X, Y
    if keyboard.Key.up in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_A))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_A))

    if keyboard.Key.down in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_B))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_B))

    if keyboard.Key.left in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_X))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_X))

    if keyboard.Key.right in pressed_keys:
        emu.input.keypad_add_key(keymask(Keys.KEY_Y))
    else:
        emu.input.keypad_rm_key(keymask(Keys.KEY_Y))

    # F5 = save state
    if keyboard.Key.f5 in pressed_keys:
        emu.savestate.save_file(SAVE_STATE_FILE)
        print("State saved!")
        pressed_keys.discard(keyboard.Key.f5)

    # F9 = load state
    if keyboard.Key.f9 in pressed_keys:
        emu.savestate.load_file(SAVE_STATE_FILE)
        print("State loaded!")
        pressed_keys.discard(keyboard.Key.f9)

    for _ in range(60):
        emu.cycle()

    window.draw()
    time.sleep(1/60)

listener.stop()
