import socket
import spidev
import RPi.GPIO as GPIO
import time
#import threading
def read_spi_adc(adcChannel):
    adcValue=0
    buff=spi.xfer2([6|(adcChannel&4)>>2,(adcChannel&3)<<6,0])
    adcValue=((buff[1]&15)<<8)+buff[2]
    return adcValue


spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000
# Pick an open Port (1000+ recommended), must match the server port
HOST = '10.27.0.50' 
# Enter IP or Hostname of your server
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("connected")

#Lets loop awaiting for your input
while True:
    adcValue=read_spi_adc(0)
    print(adcValue)
    time.sleep(1)
    command = str(adcValue)
    command = command.encode(encoding='UTF-8')
    s.send(command)
    reply = s.recv(1024)
    reply = reply.decode("UTF-8")
    #print(type(reply))
    if reply == 'Terminate':
        break
    print (reply)
