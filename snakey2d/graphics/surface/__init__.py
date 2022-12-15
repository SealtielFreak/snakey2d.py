import sdl2
import ctypes


class PixelFormat:
    pass


class Surface:
    def __init__(self):
        self.__c_surface = sdl2.SDL_Surface()

    @property
    def c_surface(self):
        return self.__c_surface

    @property
    def format(self):
        # return self.__c_surface.format
        return PixelFormat()

    @property
    def size(self):
        return self.c_surface.w, self.c_surface.h
    
    @property
    def pitch(self):
        return self.c_surface.pitch

    @property
    def pixels(self):
        return self.c_surface.pixels
    
    @property
    def userdata(self):
        return self.c_surface.userdata

    @property
    def rect(self):
        return (0, 0, 0, 0)

    @property
    def refcount(self):
        return self.c_surface.refcount
