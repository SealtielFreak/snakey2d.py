from enum import Enum
from typing import Any, Union, Tuple

import sdl2


class RendererFlags(Enum):
    SOFTWARE = sdl2.SDL_RENDERER_SOFTWARE
    HARDWARE = sdl2.SDL_RENDERER_ACCELERATED
    PRESENT_VSYNC = sdl2.SDL_RENDERER_PRESENTVSYNC
    TARGET_TEXTURE = sdl2.SDL_RENDERER_TARGETTEXTURE


RendererFlagsArgument = Union[RendererFlags, int]


class Renderer:
    def __init__(self, c_renderer: Any):
        self.__c_renderer = c_renderer
        self.__color = 0, 0, 0, 255

    def __del__(self):
        sdl2.SDL_DestroyRenderer(self.c_renderer)

    @staticmethod
    def create_from_window(window: Any, index: int = -1, flags: RendererFlagsArgument = 0):
        return Renderer(
            c_renderer=sdl2.SDL_CreateRenderer(window.c_window, index, flags)
        )

    @property
    def c_renderer(self):
        return self.__c_renderer

    @property
    def color(self) -> Tuple[int, int, int, int]:
        return self.__color

    @color.setter
    def color(self, color: Union[Tuple[int, int, int], Tuple[int, int, int, int]]):
        if len(color) == 3:
            color = (*color, 255)

        self.__color = color
        sdl2.SDL_SetRenderDrawColor(self.c_renderer, *tuple(color))

    def clear(self) -> None:
        sdl2.SDL_RenderClear(self.c_renderer)

    def present(self) -> None:
        sdl2.SDL_RenderPresent(self.c_renderer)