import threading
import socket
import tkinter
import tkinter.font
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
    global conn, spi, line_max, empty_value, lstx, lst_gsr, lst_pul
    global fig, ax1, ax2, idx, count, data, adcValue, avg_gsr, avg_pul
    
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
    ax1.cla()
    ax2.cla()
    ax1.plot(lstx,lst_gsr,'r.-')
    ax2.plot(lstx,lst_pul,'b.-')
    fig.canvas.draw()
    lie_detector.after(200, lie_detector_core)
    

def detecting_window():
    global data, adcValue, avg_gsr, avg_pul
    TF_window = tkinter.Tk()
    TF_window.title("Lie? or Truth?")
    TF_window.geometry("800x800+300+300")
    TF_window.resizable(False, False)
    font = tkinter.font.Font(size=1000)
    TF_label = tkinter.Label(TF_window, text="???", font=font)
    TF_label.pack()
    
    
    def detection():
        global data, adcValue, avg_gsr, avg_pul
        count_lier=0
        for i in range(10):
            if data > avg_pul*1.1 and adcValue < avg_gsr*0.9:
                count_lier += 1
                #print("in if")
            time.sleep(0.2)
    
        if count_lier > 8:
            TF_label.config(text="You Lier~!", fg='red')
        else:
            TF_label.config(text="Truth!", fg='blue')
    
    TF_window.after(200, detection)
    TF_window.mainloop()
    

#---

lie_detector = tkinter.Tk()
lie_detector.title("Lie Detector")
lie_detector.geometry("400x400+40+40")
lie_detector.resizable(False, False)

detect_button = tkinter.Button(lie_detector, text='you lier?', command=detecting_window)
detect_button.pack(side='bottom')

HOST = '10.27.6.16' 
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

flag = False
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
