from typing import List

import ctypes
import sdl2


def get_keyboard_state() -> List[str]:
    keydecode = lambda k: sdl2.SDL_GetKeyName(sdl2.SDL_GetKeyFromScancode(k)).decode()

    numkeys = ctypes.c_int()
    keystate = sdl2.keyboard.SDL_GetKeyboardState(ctypes.byref(numkeys))
    ptr_t = ctypes.POINTER(ctypes.c_uint8 * numkeys.value)

    return [keydecode(k) for k, s in enumerate(ctypes.cast(keystate, ptr_t)[0]) if s == 1]