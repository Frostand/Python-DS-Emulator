import ctypes
from desmume.emulator import DeSmuME, Keys

window = emu.create_sdl_window()

while not window.has_quit():
    window.process_input()

    # Manual save/load with keyboard
    keys = window.get_keys()
    if keys.get(Keys.F5):
        emu.savestate.save_file("slot1.dst")
        print("Game saved!")
    if keys.get(Keys.F9):
        emu.savestate.load_file("slot1.dst")
        print("Game loaded!")

    for _ in range(60):
        emu.cycle()
    window.draw()
