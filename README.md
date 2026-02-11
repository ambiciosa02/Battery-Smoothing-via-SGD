# Battery-Smoothing-via-SGD

Battery Smoothing via SGD
A lightweight Python implementation of Stochastic Gradient Descent (SGD) used as a signal processing filter. This project simulates a common embedded systems challenge: reading stable battery voltage from a sensor plagued by electronic noise.

🔋 The Problem
Raw Analog-to-Digital Converter (ADC) readings in hardware are often "noisy." Turning on a motor or an LED can cause voltage spikes that make a battery look like it's jumping between 80% and 100% rapidly. Simple averaging often isn't responsive enough.

💡 The Solution: SGD as a Filter
Instead of using a traditional Moving Average, this script treats signal filtering as an optimization problem:

Prediction: We assume the battery is at our last known state.

Loss Calculation: We calculate the "error" between our state and the new noisy reading.

Optimization: We use a Learning Rate to nudge our estimate toward the new reading.

This results in a smooth, lag-compensated output that ignores minor spikes while following the true trend of the battery discharge.

🚀 Key Features
Minimalist Logic: The core algorithm is only 3 lines of code—ideal for porting to C/C++ for Microcontrollers (Arduino, ESP32, STM32).

Dynamic Tuning: Adjust the learning_rate to balance between "smoothness" and "responsiveness."

Visual Validation: Includes a Matplotlib script to compare the Raw, True, and Smoothed signals.

![Capture d’écran 2026-02-11 095219](https://github.com/user-attachments/assets/1dff1648-6cec-49af-a477-2bca6e5db61c)


🛠️ Usage
Ensure you have numpy and matplotlib installed.

Run the simulation:

Bash
python mm.py
