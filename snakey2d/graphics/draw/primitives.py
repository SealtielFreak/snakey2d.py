import ctypes
from typing import Tuple, List

import sdl2
import sdl2.sdlgfx as sdlgfx

from snakey2d.graphics.color import Color
from snakey2d.graphics.renderer import Renderer
from snakey2d.types.utilities import vertex_to_c


def pixel(renderer: Renderer, position: Tuple[int, int], color: int) -> None:
    sdlgfx.pixelColor(renderer.c_renderer, *position, int(color))


def line(renderer: Renderer, position: Tuple[int, int, int, int], color: int):
    sdlgfx.lineColor(renderer.c_renderer, *position, int(color))


def circle(renderer: Renderer, position, radius: int, color: int):
    sdlgfx.circleColor(renderer.c_renderer, *position, radius, int(color))


def line_rectangle(renderer: Renderer, position, size, color: int) -> None:
    sdlgfx.rectangleColor(renderer.c_renderer, *position, *size, int(color))


def filled_rectangle(renderer: Renderer, position, size, color: int) -> None:
    sdlgfx.boxColor(renderer.c_renderer, *position, *size, int(color))


def line_polygon(renderer: Renderer, vertex: List[Tuple[int, int]], color: int):
    vertex_x, vertex_y = vertex_to_c(vertex)

    sdlgfx.polygonColor(
        renderer.c_renderer,
        vertex_x,
        vertex_y,
        len(vertex),
        int(color)
    )


def filled_polygon(renderer: Renderer, vertex: List[Tuple[int, int]], color: int):
    vertex_x, vertex_y = vertex_to_c(vertex)

    sdlgfx.filledPolygonColor(
        renderer.c_renderer,
        vertex_x,
        vertex_y,
        len(vertex),
        int(color)
    )
