import numpy as np
import matplotlib.pyplot as plt

PI = np.pi
fs = 4 # sampling frequency = 2*NyquistFreq
time = np.linspace(0, 1, 100)

def SF(time):
    ps = 0 # initialize
    t = np.linspace(0, 1, fs+1) # sampling points
    for k in range(0,len(t)):
        ps += np.sin(2*PI*t[k])*np.sinc(fs*(time-t[k]))
    return ps

plt.plot(time,SF(time))
plt.plot(time,np.sin(2*PI*time))
plt.xlabel("time")
plt.ylabel("signal & partial sum")
plt.show()