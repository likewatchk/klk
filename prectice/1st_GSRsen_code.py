import spidev
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.legend as legend
import time
import threading
spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=500000
line_max=10
BUZ=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZ,GPIO.OUT)
BUZ_PWM = GPIO.PWM(BUZ, 900)
empty_value=4095
def read_spi_adc(adcChannel):
   adcValue=0
   buff =spi.xfer2([ 6 | (adcChannel&4) >> 2, (adcChannel&3)<<6,0])
   adcValue = ((buff[1]&15)<<8)+buff[2]
   return adcValue
def buz():
   BUZ_PWM.start(50)
   for i in range(0,5) :
         BUZ_PWM.ChangeFrequency(300)
         time.sleep(0.1)
   BUZ_PWM.stop()
try :
   lstx=[]
   lst_gsr=[]
   fig=plt.gcf()
   fig.show()
   fig.canvas.draw()
   plt.pause(0.01)
   time.sleep(0.5)
   i=0
   count=0
   while True :
     adcValue= read_spi_adc(0)
     print(adcValue)
     lst_gsr.append(adcValue)
     lstx.append(i)
     plt.ylim(0,4096)
     i=i+1
     lst_len=len(lstx)
     sum=0
     st_num=0
     data_count=1
     ed_num=lst_len
     if lst_len > 10 :
          st_num=lst_len-10
          data_count=10
     else :
          st_num=0
          data_count=lst_len
     for i in range(st_num,ed_num) :
            sum=sum+lst_gsr[i]
     avg=sum/data_count
     limit=avg+avg*0.2
     if adcValue > limit :
          thread = threading.Thread(target=buz)
          thread.start()
     plt.plot(lstx,lst_gsr,'r.-')
     fig.canvas.draw()
     plt.pause(0.01)
     time.sleep(0.2)

finally :
   GPIO.cleanup()
   exit()
