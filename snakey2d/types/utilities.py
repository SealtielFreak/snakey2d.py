import ctypes

from snakey2d.types.c_cast import c_array


def vertex_to_c(vertex):
    c_int16_array = c_array(ctypes.c_int16)
    to_c = lambda points: c_int16_array(len(points), points)

    vertex_x, vertex_y = [], []
    for vec in vertex:
        vertex_x.append(int(vec[0]))
        vertex_y.append(int(vec[1]))

    return to_c(vertex_x), to_c(vertex_y)