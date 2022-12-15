import ctypes
from dataclasses import dataclass
from enum import Enum
from typing import Union, Any

import sdl2


class WindowEventID(Enum):
    NONE = sdl2.SDL_WINDOWEVENT_NONE
    SHOWN = sdl2.SDL_WINDOWEVENT_SHOWN
    HIDDEN = sdl2.SDL_WINDOWEVENT_HIDDEN
    EXPOSED = sdl2.SDL_WINDOWEVENT_EXPOSED
    MOVED = sdl2.SDL_WINDOWEVENT_MOVED
    RESIZED = sdl2.SDL_WINDOWEVENT_RESIZED
    SIZE_CHANGED = sdl2.SDL_WINDOWEVENT_SIZE_CHANGED
    MINIMIZED = sdl2.SDL_WINDOWEVENT_MINIMIZED
    MAXIMIZED = sdl2.SDL_WINDOWEVENT_MAXIMIZED
    RESTORED = sdl2.SDL_WINDOWEVENT_RESTORED
    ENTER = sdl2.SDL_WINDOWEVENT_ENTER
    LEAVE = sdl2.SDL_WINDOWEVENT_LEAVE
    FOUS_GAINED = sdl2.SDL_WINDOWEVENT_FOCUS_GAINED
    FOCUST_LOST = sdl2.SDL_WINDOWEVENT_FOCUS_LOST
    CLOSE = sdl2.SDL_WINDOWEVENT_CLOSE
    TAKE_FOCUS = sdl2.SDL_WINDOWEVENT_TAKE_FOCUS
    HIT_TEST = sdl2.SDL_WINDOWEVENT_HIT_TEST
    ICCPROF_CHANGED = sdl2.SDL_WINDOWEVENT_ICCPROF_CHANGED
    CCPROF_CHANGED = sdl2.SDL_WINDOWEVENT_ICCPROF_CHANGED


@dataclass
class WindowEvent:

    type: int
    timestamp: int
    window_id: WindowEventID
    event: int
    data1: int
    data2: int


@dataclass
class KeySym:
    scancode: int
    sym: int
    mod: int


@dataclass
class KeyboardEvent:
    type: int
    timestamp: int
    window_id: WindowEventID
    state: int
    repeat: int
    keysym: KeySym


class EventType(Enum):
    QUIT = sdl2.SDL_QUIT
    WINDOW = sdl2.SDL_WINDOWEVENT
    USER = sdl2.SDL_USEREVENT
    TEXT_EDITING = sdl2.SDL_TEXTEDITING
    SYSWMEVENT = sdl2.SDL_SYSWMEVENT
    MULTIGESTURE = sdl2.SDL_MULTIGESTURE
    MOUSEWHEEL = sdl2.SDL_MOUSEWHEEL
    MOUSEBUTTONUP = sdl2.SDL_MOUSEBUTTONUP
    MOUSEBUTTONDOWN = sdl2.SDL_MOUSEBUTTONDOWN
    MOUSEMOTION = sdl2.SDL_MOUSEMOTION
    JOYDEVICEREMOVED = sdl2.SDL_JOYDEVICEREMOVED
    JOYDEVICEADDED = sdl2.SDL_JOYDEVICEADDED
    JOYBUTTONUP = sdl2.SDL_JOYBUTTONUP
    JOYBUTTONDOWN = sdl2.SDL_JOYBUTTONDOWN
    JOYHATMOTION = sdl2.SDL_JOYHATMOTION
    JOYBALLMOTION = sdl2.SDL_JOYBALLMOTION
    JOYAXISMOTION = sdl2.SDL_JOYAXISMOTION
    KEYDOWN = sdl2.SDL_KEYDOWN
    KEYUP = sdl2.SDL_KEYUP
    FINGERUP = sdl2.SDL_FINGERUP
    FINGERDOWN = sdl2.SDL_FINGERDOWN
    FINGERMOTION = sdl2.SDL_FINGERMOTION
    DROPCOMPLETE = sdl2.SDL_DROPCOMPLETE
    DROPBEGIN = sdl2.SDL_DROPBEGIN
    DROPTEXT = sdl2.SDL_DROPTEXT
    DROPFILE = sdl2.SDL_DROPFILE
    DOLLARRECORD = sdl2.SDL_DOLLARRECORD
    DOLLARGESTURE = sdl2.SDL_DOLLARGESTURE
    CONTROLLERDEVICEREMAPPED = sdl2.SDL_CONTROLLERDEVICEREMAPPED
    CONTROLLERDEVICEREMOVED = sdl2.SDL_CONTROLLERDEVICEREMOVED
    CONTROLLERDEVICEADDED = sdl2.SDL_CONTROLLERDEVICEADDED
    CONTROLLERBUTTONUP = sdl2.SDL_CONTROLLERBUTTONUP
    CONTROLLERBUTTONDOWN = sdl2.SDL_CONTROLLERBUTTONDOWN
    CONTROLLERAXISMOTION = sdl2.SDL_CONTROLLERAXISMOTION
    AUDIODEVICEREMOVED = sdl2.SDL_AUDIODEVICEREMOVED
    AUDIODEVICEADDED = sdl2.SDL_AUDIODEVICEADDED


class Event:
    def __init__(self):
        self.__c_event = sdl2.SDL_Event()

    @property
    def c_event(self):
        return self.__c_event

    @property
    def type(self) -> Union[EventType, int]:
        try:
            return EventType(self.__c_event.type)
        except ValueError:
            return -1

    @property
    def window(self) -> WindowEvent:
        return WindowEvent(
            self.c_event.window.type,
            self.c_event.window.timestamp,
            WindowEventID(self.c_event.window.windowID),
            self.c_event.window.event,
            self.c_event.window.data1,
            self.c_event.window.data2
        )

    @property
    def key(self) -> KeyboardEvent:
        return KeyboardEvent(
            self.c_event.key.type,
            self.c_event.key.timestamp,
            self.c_event.key.windowID,
            self.c_event.key.state,
            self.c_event.key.repeat,
            KeySym(
                self.c_event.key.keysym.scancode,
                self.c_event.key.keysym.sym,
                self.c_event.key.keysym.mod,
            )
        )


def peep_events(event: Event, numevents: int, action: Any, minType: Any, maxType: Any):
    raise NotImplementedError()


def push_event(event: Event):
    sdl2.SDL_PushEvent(event.c_event)


def wait_event(event: Event):
    sdl2.SDL_WaitEvent(event.c_event)


def wait_event_timeout(event: Event, timeout: int):
    sdl2.SDL_WaitEventTimeout(event.c_event, timeout)


def poll_events(event: Union[Event, None] = None):
    if event is None:
        event = Event()

    while sdl2.SDL_PollEvent(ctypes.byref(event.c_event)) != 0:
        yield event


def is_running():
    c_events = sdl2.SDL_Event()

    while sdl2.SDL_PollEvent(ctypes.byref(c_events)) != 0:
        if c_events.type == sdl2.SDL_QUIT:
            return False

    return True
