import sdl2
import sdl2.sdlimage as sdlimage
import ctypes


class Image:
    def __int__(self, filename: str):
        self.__c_image = sdlimage.IMG_Load(filename.encode())

    
