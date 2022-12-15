from snakey2d.events import poll_events, EventType
from snakey2d.graphics.color import Color
from snakey2d.graphics.draw.primitives import filled_rectangle, filled_polygon
from snakey2d.graphics.surface import Surface
from snakey2d.window import Window


if __name__ == '__main__':
    window = Window("Hello world", (640, 480))
    renderer = window.renderer

    surface = Surface()
    print(surface.size)

    r, g, b = 0, 0, 0

    while True:
        for event in poll_events():
            if event.type == EventType.QUIT:
                exit(0)

        # r = (r + 50) % 255
        # g = (g + 1) % 255
        # b = (b + 1) % 255

        renderer.color = (r, g, b)
        renderer.clear()

        filled_rectangle(renderer, (0, 0), (100, 100), Color(255, 0, 255 // 2).value)
        filled_polygon(renderer, [
            (0, 0),
            (0, 100),
            (100, 0),
        ], Color(255, 0, 0).value)

        renderer.present()
