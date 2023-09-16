import numpy as np
import matplotlib.pyplot as plt
import control
from scipy import signal

# Define the transfer function
#numerator = [1]
#denominator = [1, 0.9, 1]  # Represents: s^2 + 2s + 1
#denominator = [0.1, 0.9]  # Represents: s^2 + 2s + 1
#system = control.TransferFunction(numerator, denominator)

# Define filter parameters
cutoff_frequency = 1  # Cutoff frequency in Hz

# Design the first-order low-pass filter
a=0.01
numerator = [a]
denominator = [1, a-1]
filter_system = signal.TransferFunction(numerator, denominator)

# Generate time values for simulation
U0=1;
DU1=0.1;
DU2=0.1;
time = np.linspace(0, 10, 1000)
U=np.sin(time*2*np.pi)*DU1+np.sin(time*20*np.pi)*DU2+U0
U=np.concatenate([np.zeros_like(time[0:100]),np.ones_like(time[100:])])

# Simulate the step response
#time_response = control.step_response(system, time)
#time_response = control.forced_response(system, time, U, [U0,U0])
# Extract the time values and the system's response
#time_values = time_response[0]
#response = time_response[1]

response = signal.lfilter(numerator, denominator, U)

 
# Plot the step response
plt.plot(time, response)
plt.plot(time, U)
plt.xlabel('Temps')
plt.ylabel('Réponse')
plt.title('Temps de réponse d''un instrument')
plt.grid()
plt.show()
