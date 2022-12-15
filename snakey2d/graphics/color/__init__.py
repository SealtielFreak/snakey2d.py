from typing import Tuple


def rgba_to_hex(*args) -> int:
    r, g, b, a = args
    return ((r & 0xFF) << 24) + ((g & 0xFF) << 16) + ((b & 0xff) << 8) + (a & 0xFF)


def rgb_to_hex(*args) -> int:
    r, g, b = args
    return ((r & 0xFF) << 16) + ((g & 0xFF) << 8) + (b & 0xff)


def hex_to_rgba(value: int) -> Tuple[int, int, int, int]:
    return (
        ((value >> 24) & 0xFF) // 255,
        ((value >> 16) & 0xFF) // 255,
        ((value >> 8) & 0xFF) // 255,
        (value & 0xFF) // 255,
    )


def hex_to_rgb(value: int) -> Tuple[int, int, int]:
    return (
        ((value >> 16) & 0xFF) // 255,
        ((value >> 8) & 0xFF) // 255,
        (value & 0xFF) // 255,
    )


class Color:
    @staticmethod
    def __class_getitem__(colors) -> int:
        if len(colors) == 4:
            return rgba_to_hex(*colors)
        elif len(colors) == 3:
            return rgba_to_hex(*colors, 255)

        raise ValueError("Invalid color format")

    def __init__(self, *args):
        if len(args) == 3:
            args = *args, 255
        elif len(args) == 1:
            hex = args[0]

            if isinstance(hex, int):
                args = hex_to_rgba(hex)

        self.r, self.g, self.b, self.a = args

    def __iter__(self):
        return iter([self.r, self.g, self.b, self.a])

    def __int__(self):
        return rgba_to_hex(*self)

    @property
    def value(self) -> int:
        return int(self)
