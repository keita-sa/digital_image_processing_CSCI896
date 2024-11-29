import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
PI = np.pi

# Define the input signal: can be single or composite signal
def input_signal(time, freq=1):
    """
    Generates the input signal to be sampled and reconstructed.
    :param time: array, time values
    :param freq: float, frequency of the signal
    :return: array, signal values
    """
    # Example: single sine wave at given frequency
    return np.sin(2 * PI * freq * time)

# Sampling and reconstruction using sinc interpolation
def reconstruct_signal(time, sampled_time, sampled_values, fs):
    """
    Reconstructs the signal using sinc interpolation.
    :param time: array, time values for reconstruction
    :param sampled_time: array, sampled time points
    :param sampled_values: array, sampled signal values
    :param fs: int, sampling frequency
    :return: array, reconstructed signal values
    """
    reconstructed_signal = np.zeros_like(time)
    for k in range(len(sampled_time)):
        reconstructed_signal += sampled_values[k] * np.sinc(fs * (time - sampled_time[k]))
    return reconstructed_signal

# Main visualization and testing function
def sampling_theorem_demo(signal_freq=1, sampling_freq=4, duration=1, num_points=1000):
    """
    Demonstrates the Sampling Theorem and aliasing effects.
    :param signal_freq: float, frequency of the input signal
    :param sampling_freq: int, sampling frequency
    :param duration: float, duration of the signal in seconds
    :param num_points: int, number of points for continuous signal
    """
    time_continuous = np.linspace(0, duration, num_points)  # High-resolution time
    original_signal = input_signal(time_continuous, freq=signal_freq)  # Original signal

    # Sampling
    sampled_time = np.linspace(0, duration, sampling_freq + 1)  # Sampling time points
    sampled_signal = input_signal(sampled_time, freq=signal_freq)  # Sampled values

    # Reconstruction
    reconstructed_signal = reconstruct_signal(time_continuous, sampled_time, sampled_signal, fs=sampling_freq)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(time_continuous, original_signal, label="Original Signal (Continuous)", color="blue", lw=2)
    ax.stem(sampled_time, sampled_signal, label="Sampled Points", linefmt="r-", markerfmt="ro", basefmt=" ")
    ax.plot(time_continuous, reconstructed_signal, label="Reconstructed Signal", color="green", lw=1.5, linestyle="--")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Sampling Theorem Demonstration\nSignal Frequency = {signal_freq} Hz, Sampling Frequency = {sampling_freq} Hz")
    ax.legend()
    ax.grid(True)
    plt.show()

# Optional: Animated version to visualize improvements in reconstruction
def animate_reconstruction(signal_freq=1, max_sampling_freq=16, duration=1, num_points=1000):
    """
    Animates the signal reconstruction process as sampling frequency increases.
    :param signal_freq: float, frequency of the input signal
    :param max_sampling_freq: int, maximum sampling frequency for animation
    :param duration: float, duration of the signal in seconds
    :param num_points: int, number of points for continuous signal
    """
    time_continuous = np.linspace(0, duration, num_points)
    original_signal = input_signal(time_continuous, freq=signal_freq)

    fig, ax = plt.subplots(figsize=(10, 6))
    line_original, = ax.plot(time_continuous, original_signal, label="Original Signal (Continuous)", color="blue", lw=2)
    line_reconstructed, = ax.plot([], [], label="Reconstructed Signal", color="green", lw=1.5, linestyle="--")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(f"Signal Reconstruction Animation\nSignal Frequency = {signal_freq} Hz")
    ax.legend()
    ax.grid(True)

    def update(frame):
        sampling_freq = frame + 1
        sampled_time = np.linspace(0, duration, sampling_freq + 1)
        sampled_signal = input_signal(sampled_time, freq=signal_freq)
        reconstructed_signal = reconstruct_signal(time_continuous, sampled_time, sampled_signal, fs=sampling_freq)

        line_reconstructed.set_data(time_continuous, reconstructed_signal)
        ax.stem(sampled_time, sampled_signal, linefmt="r-", markerfmt="ro", basefmt=" ")
        ax.set_title(f"Signal Reconstruction Animation\nSignal Frequency = {signal_freq} Hz, Sampling Frequency = {sampling_freq} Hz")

    ani = FuncAnimation(fig, update, frames=max_sampling_freq, repeat=False, interval=500)
    plt.show()

# Run the demonstration
sampling_theorem_demo(signal_freq=2, sampling_freq=6)
animate_reconstruction(signal_freq=2, max_sampling_freq=10)
