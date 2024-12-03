**▪️ Fourier transform formula**\
<br>
Here, *ƒ* is the frequency.

![Screenshot 2024-12-02 at 18 58 33](https://github.com/user-attachments/assets/ac50ba85-2a15-4dd3-8146-05a11b0e1a0c)

When this integral exists, it is called the Fourier transform of 𝑥(𝑡).
</br>
<br>
</br>
**▪️ Cardinal Sine (sinc) Function**\
<br>
The sinc function is frequently encountered in signal processing. It is defined as:

![Screenshot 2024-12-02 at 22 07 33](https://github.com/user-attachments/assets/a72ef406-1bb1-4bec-b2a8-e90b9c6abca6)


**▪️ Definition**: A real-valued function $x(t)$ is said to be bandlimited to the frequency range $[-f_N, f_N ](f_N > 0)$ if its Fourier transform $$\hat{x}(f）$$ is $0$ for $$|f|> f_N$$.
<br>
</br>
**▪️ Sampling Theorem**: If a real-valued function $𝑥(𝑡)$ is bandlimited to the frequency
range $[−𝑓_𝑁, 𝑓_𝑁]$ and satisfies:
![Screenshot 2024-12-03 at 10 46 12](https://github.com/user-attachments/assets/00178384-e776-4b25-b03b-4b55156ea869)

with $∆t=  1/(2f_N )$ and $t_n=n∆t, then x(t)$ can be reconstructed as:

![Screenshot 2024-12-03 at 10 47 47](https://github.com/user-attachments/assets/b0624309-6972-4e09-9c6d-6808337b36c9)


## References
Masahiro Kaminaga. 2020. *Fourier Analysis and Signal Processing with Python*. CORONA PUBLISHING CO., LTD.
