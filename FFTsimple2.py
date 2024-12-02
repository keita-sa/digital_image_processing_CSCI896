import numpy as np
import matplotlib.pyplot as plt
N = 2**8 # Number of sample points
fs = 100 #  sampling frequency[Hz]
T = 1/fs # Sampling period[sec]
PI = np.pi
# Frequencies[Hz]
f1 = 10; f2 = 20; f3 = 70
# Amplitudes
A1 = 1.2; A2 = 0.2; A3 = 0.7
# time
t = np.arange(0, N*T, T)
# signal
x = A1*np.sin(2*PI*f1*t)+A2*np.sin(2*PI*f2*t)+A3*np.sin(2*PI*f3*t)

fig = plt.figure(figsize=(10, 5))
plt.xlabel('time t[sec]', fontsize=15)
plt.ylabel('signal', fontsize=15)
plt.xlim(0, 0.5)
plt.plot(t, x)

# FFT
F = np.fft.fft(x)

# amplitude
amp = 2*np.abs(F)/N
# frequency
freq = np.linspace(0, fs, N)

fig = plt.figure(figsize=(10, 5))
plt.xlabel('frequency f[Hz]', fontsize=15)
plt.ylabel('amplitude spectrum', fontsize=15)
plt.grid()  # Add grid lines
#plt.plot(freq, amp)
plt.plot(freq[:int(N/2)+1], amp[:int(N/2)+1])
# Find peaks
peaks = np.argsort(amp[:int(N/2)+1])[-3:]  # Get indices of the 3 largest peaks
for peak in peaks:
    plt.annotate(f'{freq[peak]:.1f} Hz',  # Annotate frequency value
                 xy=(freq[peak], amp[peak]),
                 xytext=(freq[peak]+5, amp[peak]+0.1),
                 arrowprops=dict(facecolor='red', arrowstyle='->'),
                 fontsize=12)
plt.show()
