from pulsesensor import Pulsesensor
import time

p = Pulsesensor()
p.startAsyncBPM()

try:
    while True:
        bpm = p.BPM
        if bpm > 0:
            print("BPM: %d" % bpm)
        else:
            print("BPM: %d" %bpm)
            print("No Heartbeat found")
        time.sleep(1)
except:
    p.stopAsyncBPM()
