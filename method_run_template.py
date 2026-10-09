import matplotlib.pyplot as plt
from pid_template import make_car
from pid_template import update
from pid_template import calculate_desired_acceleration
from pid_template import acceleration_to_throttle_percentage

K_P = 0.1
K_I = 0.1
K_D = 0.1
 
STEPS = 550
 
car = make_car(desired_v=20.0, dt=0.1)

#WRITE CODE HERE
times = []
velocities = []
desired = []
for step in range(STEPS):
    desired_acceleration, error = calculate_desired_acceleration(car, K_P, K_I, K_D)
    throttle_percentage = acceleration_to_throttle_percentage(desired_acceleration)
    update(car, throttle_percentage)
    
    times.append(car["t"])
    velocities.append(car["v"])
    desired.append(car["desired_v"])

plt.plot(times, velocities, label="Actual Velocity")
plt.plot(times, desired, "r--", label="Desired Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("PID Controller: Velocity vs Time")
plt.legend()
plt.grid(True)
plt.show()