import threading
import socket
import tkinter
import spidev
import RPi.GPIO as GPIO
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.legend as legend
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import time


def read_spi_adc(adcChannel):
    adcValue=0
    buff=spi.xfer2([6|(adcChannel&4)>>2,(adcChannel&3)<<6,0])
    adcValue=((buff[1]&15)<<8)+buff[2]
    return adcValue


def lie_detector_core():
    global conn, spi, line_max, empty_value, lstx, lst_gsr, lst_pul,
            fig, ax1, ax2, idx, count, data, adcValue, avg_gsr, avg_pul,flag
    
    data = conn.recv(1024)
    data = float(data.decode(encoding='UTF-8')[:11])
    adcValue=read_spi_adc(0)
    print(adcValue,data)
    lst_gsr.append(adcValue)
    lst_pul.append(data)
    lstx.append(idx)
    #lstx2.append(i)
    
    idx=idx+1
    lst_len=len(lstx)
    sum_gsr = 0
    sum_pul = 0
    st_num=0
    data_count = 1
    ed_num=lst_len
    if lst_len >30 :
        st_num=lst_len-30
        data_count=30
        del lstx[0]
        del lst_gsr[0]
        del lst_pul[0]
    else:
        st_num=0
        data_count=lst_len
    for i in range(st_num,ed_num):
        sum_gsr = sum(lst_gsr)
        sum_pul = sum(lst_pul)
    avg_gsr = sum_gsr/data_count
    avg_pul = sum_pul/data_count
    if flag:
        ax1.cla()
        ax2.cla()
        limit_gsr = avg_gsr*0.9
        limit_pul = avg_pul*1.1
        if adcValue < limit_gsr and data > limit_pul:
            pass
        ax1.plot(lstx,lst_gsr,'r.-')
        ax2.plot(lstx,lst_pul,'b.-')
        fig.canvas.draw()
    else:
        ax1.cla()
        ax2.cla()
        ax1.plot(lstx,lst_gsr,'r.-')
        ax2.plot(lstx,lst_pul,'b.-')
        fig.canvas.draw()
    lie_detector.after(200, lie_detector_core)
    

def flagset(tf):
    global flag
    flag = tf
    lie_detector.after(30000, flagset, True)

    
    

#---

lie_detector = tkinter.Tk()
lie_detector.title("Lie Detector")
lie_detector.geometry("400x400+40+40")
lie_detector.resizable(False, False)


HOST = '10.27.7.17' 
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


#------

flag = 0
idx = 0
count=0
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

detector_canvas = FigureCanvasTkAgg(fig, master=lie_detector)
detector_canvas.draw()
detector_canvas.get_tk_widget().pack(expand=True, fill="both")

lie_detector.after(200, lie_detector_core)
lie_detector.mainloop()

print("?????????")

GPIO.cleanup()
exit()
