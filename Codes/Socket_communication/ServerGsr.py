import socket
import spidev
import RPi.GPIO as GPIO
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.legend as legend
import time
import threading

def read_spi_adc(adcChannel):
    adcValue=0
    buff=spi.xfer2([6|(adcChannel&4)>>2,(adcChannel&3)<<6,0])
    adcValue=((buff[1]&15)<<8)+buff[2]
    return adcValue
#---

HOST = '10.27.6.29' 
# Server IP or Hostname
PORT = 12345 
# Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
#managing error exception
try:
    s.bind((HOST, PORT))
except socket.error:
    print ('Bind failed ')
s.listen(5)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print ('Connected')

#---

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000
line_max = 10
empty_value=4095
lstx=[]
lst_gsr=[]
lst_pul=[]
matplotlib.use("TKAgg")
fig=plt.gcf()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
fig.show()
fig.canvas.draw()
plt.pause(0.01)
time.sleep(0.5)
i=0
count=0
while True:
    data = conn.recv(1024)
    data = float(data.decode(encoding='UTF-8'))
    adcValue=read_spi_adc(0)
    print(adcValue,data)
    lst_gsr.append(adcValue)
    lst_pul.append(data)
    lstx.append(i)
    #lstx2.append(i)
    
    i=i+1
    lst_len=len(lstx)
    sum=0
    st_num=0
    data_count=1
    ed_num=lst_len
    if lst_len >10:
        st_num=lst_len-10
        data_count=10
    else:
        st_num=0
        data_count=lst_len
    for i in range(st_num,ed_num):
        sum=sum+lst_gsr[i]
    avg= sum/data_count
    plt.ylim(0,4096)
    ax1.plot(lstx,lst_gsr,'r.-')
    plt.ylim(0,300)
    ax2.plot(lstx,lst_pul,'r.-')
    fig.canvas.draw()
    plt.pause(0.01)
    time.sleep(0.2)
    
GPIO.cleanup()
exit()
