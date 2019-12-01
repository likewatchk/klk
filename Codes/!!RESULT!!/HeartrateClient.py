import socket
from pulsesensor import Pulsesensor
import time
import RPi.GPIO as GPIO
import RPi.GPIO as GPIO
import time
#import threading
p = Pulsesensor()
p.startAsyncBPM()
#Pick an open Port (1000+ recommended), must match the server port
HOST = '10.27.6.29' 
# Enter IP or Hostname of your server
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("connected")

#Lets loop awaiting for your input
while True:
    bpm = p.BPM
    print(bpm)
    command = str(bpm)
    command = command.encode(encoding='UTF-8')
    time.sleep(1)
    s.send(command)
    
#daslkdjwl;adkal;dkal;skfjl;dsl;kjgdsfl;kgfdl;kgdfl;kgdfl;kgdfl;kgdfl;kfgdlkgfl;kgdfl;kbfvl;kdfbmdl;bm
#daml;dsal;ksadl;kdasl;kdsal;kdsal;ksadl;kdsalk;dsal;kvcml;kxdfvml;fvl;dskfdl;sfklwefm
    
