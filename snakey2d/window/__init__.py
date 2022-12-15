from enum import Enum
from typing import Tuple, Union

import sdl2
import ctypes

from snakey2d.graphics.renderer import Renderer


class WindowFlags(Enum):
    FULLSCREEN = sdl2.SDL_WINDOW_FULLSCREEN
    FULLSCREEN_DESKTOP = sdl2.SDL_WINDOW_FULLSCREEN_DESKTOP
    OPENGL = sdl2.SDL_WINDOW_OPENGL
    VULKAN = sdl2.SDL_WINDOW_VULKAN
    SHOWN = sdl2.SDL_WINDOW_SHOWN
    HIDDEN = sdl2.SDL_WINDOW_HIDDEN
    BORDERLESS = sdl2.SDL_WINDOW_BORDERLESS
    RESIZABLE = sdl2.SDL_WINDOW_RESIZABLE
    MINIMIZED = sdl2.SDL_WINDOW_MINIMIZED
    MAXIMIZED = sdl2.SDL_WINDOW_MAXIMIZED
    INPUT_GRABBED = sdl2.SDL_WINDOW_INPUT_GRABBED
    INPUT_FOCUS = sdl2.SDL_WINDOW_INPUT_FOCUS
    MOUSE_FOCUS = sdl2.SDL_WINDOW_MOUSE_FOCUS
    FOREIGN = sdl2.SDL_WINDOW_FOREIGN
    ALLOW_HIGHDPI = sdl2.SDL_WINDOW_ALLOW_HIGHDPI
    MOUSE_CAPTURE = sdl2.SDL_WINDOW_MOUSE_CAPTURE
    ALWAYS_ON_TOP = sdl2.SDL_WINDOW_ALWAYS_ON_TOP
    SKIP_TASKBAR = sdl2.SDL_WINDOW_SKIP_TASKBAR
    UTILITY = sdl2.SDL_WINDOW_UTILITY
    TOOLTIP = sdl2.SDL_WINDOW_TOOLTIP
    POPUP_MENU = sdl2.SDL_WINDOW_POPUP_MENU


class WindowPosition(Enum):
    CENTERED = sdl2.SDL_WINDOWPOS_CENTERED
    UNDEFINED = sdl2.SDL_WINDOWPOS_UNDEFINED


WindowFlagsArgument = Union[WindowFlags, int]


class Window:
    def __init__(self, title: str, size: Tuple[int, int], window_flags: WindowFlagsArgument = 0):
        position = WindowPosition.UNDEFINED.value, WindowPosition.UNDEFINED.value
        self.__c_window = sdl2.SDL_CreateWindow(title.encode(), *position, *size, window_flags)
        self.__renderer = None

    def __del__(self):
        sdl2.SDL_DestroyWindow(self.c_window)

    @staticmethod
    def create_with_renderer(title: str, size: Tuple[int, int], window_flags: WindowFlagsArgument = 0, renderer_flags=0):
        window = Window(title, size, window_flags)
        renderer = Renderer.create_from_window(window, -1, renderer_flags)
        window.renderer = renderer
        return window, renderer

    @property
    def c_window(self):
        return self.__c_window

    @property
    def renderer(self) -> Renderer:
        if self.__renderer is None:
            self.__renderer = Renderer.create_from_window(self, -1, 0)

        return self.__renderer

    @renderer.setter
    def renderer(self, renderer: Renderer):
        self.__renderer = renderer
