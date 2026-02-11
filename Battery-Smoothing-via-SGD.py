import numpy as np
import matplotlib.pyplot as plt

# 1. Setup simulated noisy battery data
# Actual battery is slowly dropping from 4.2V to 3.5V
time_steps = 200
true_voltage = np.linspace(4.2, 3.5, time_steps)
# Add "spikes" from a motor or LED turning on/off
noise = np.random.normal(0, 0.05, time_steps)
noisy_readings = true_voltage + noise

# 2. Simple Gradient Descent Smoothing
current_estimate = noisy_readings[0] # Initial guess
learning_rate = 0.1  # This controls the "smoothness"
smoothed_history = []

for reading in noisy_readings:
    # Prediction: our current estimate
    # Error: how far our estimate is from the new noisy reading
    error = current_estimate - reading
    
    # Gradient of the Square Error (Error^2) is 2 * error
    # We update our estimate to move closer to the new reading
    current_estimate -= learning_rate * error
    
    smoothed_history.append(current_estimate)

# 3. Visualization
plt.figure(figsize=(10, 5))
plt.plot(noisy_readings, color='lightgray', label='Raw Noisy Sensor (ADC)')
plt.plot(smoothed_history, color='blue', linewidth=2, label='SGD Smoothed Output')
plt.plot(true_voltage, color='red', linestyle='--', label='Actual Battery Level')
plt.title("Embedded System: Battery Level Smoothing using SGD")
plt.xlabel("Time (Samples)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.show()