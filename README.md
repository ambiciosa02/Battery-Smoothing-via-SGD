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

🧠 Why "Stochastic"?
In traditional Gradient Descent, the algorithm looks at the entire dataset (the "Batch") to calculate a single update. While precise, this is impossible in embedded systems with limited RAM.

This project uses the Stochastic (meaning "random") approach because:

Real-time Processing: It processes each sensor reading one-by-one as it arrives. It doesn't need to store a history of data, making it extremely memory-efficient for microcontrollers like Arduino or ESP32.

Handling Randomness: Every sensor reading contains "stochastic" noise (random electrical interference). By taking small steps (learning_rate) for every noisy point, the random errors eventually cancel each other out, leaving only the true signal trend.

Online Learning: The "model" (our voltage estimate) is constantly learning and adapting. If you plug in a charger, the SGD filter reacts immediately to the new trend without needing to "re-train" on a whole batch of data.

🚀 Key Features
Minimalist Logic: The core algorithm is only 3 lines of code—ideal for porting to C/C++ for Microcontrollers (Arduino, ESP32, STM32).

Dynamic Tuning: Adjust the learning_rate to balance between "smoothness" and "responsiveness."

Visual Validation: Includes a Matplotlib script to compare the Raw, True, and Smoothed signals.

![Capture d’écran 2026-02-11 095219](https://github.com/user-attachments/assets/1dff1648-6cec-49af-a477-2bca6e5db61c)


🛠️ Usage
Ensure you have numpy and matplotlib installed.


