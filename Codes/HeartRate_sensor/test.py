from pulsesensor import Pulsesensor
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import matplotlib.legend as legend


p = Pulsesensor()
p.startAsyncBPM()

lstx=[]
lst_gsr=[]
fig=plt.gcf()
fig.show()
fig.canvas.draw()
plt.pause(0.01)
time.sleep(0.5)
i=0
count=0

while True:
    bpm = p.BPM
    adcValue=bpm
    print(adcValue)
    lst_gsr.append(adcValue)
    lstx.append(i)
    plt.ylim(0,300)
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
    plt.plot(lstx,lst_gsr,'r.-')
    fig.canvas.draw()
    plt.pause(0.01)
    time.sleep(0.2)

p.stopAsyncBPM()

