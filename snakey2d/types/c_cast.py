from typing import Any


def c_array(t: Any):
    def inner(size: int, points: list):
        return (t * size)(*points)

    return inner