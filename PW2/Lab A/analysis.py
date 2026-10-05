"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

# TODO 2: compute velocity v = derivative of y w.r.t. t (np.gradient)
#         and acceleration a = derivative of v w.r.t. t (np.gradient again)
v = np.gradient(y, t)
a = np.gradient(v, t)

mean_acceleration = np.mean(a)
print(f"Mean acceleration: {mean_acceleration:.2f} m/s^2")

# TODO 3: integrate a back up to recover velocity and position
print(f"Std of acceleration: {a.std():.3f} m/s^2")
print(f"Std of velocity:     {v.std():.3f} m/s")

v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

print(f"Max |recovered y - original y|: {np.max(np.abs(y_rec - y)):.3f} m")

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# Panel 1: Position
axs[0].plot(t, y, 'b-', label='Measured Position')
axs[0].plot(t, y_rec, 'r--', label='Recovered Position')
axs[0].set_ylabel('Position (m)')
axs[0].legend()
axs[0].grid(True)

# Panel 2: Velocity
axs[1].plot(t, v, 'g-', label='Calculated Velocity')
axs[1].plot(t, v_rec, 'r--', label='Recovered Velocity')
axs[1].set_ylabel('Velocity (m/s)')
axs[1].legend()
axs[1].grid(True)

# Panel 3: Acceleration
axs[2].plot(t, a, 'orange', label='Calculated Acceleration')
axs[2].axhline(-9.81, color='black', linestyle='--', label='True g (-9.81 m/s²)')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Acceleration (m/s²)')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png')
plt.show()

#bonus: 2d trajectory
d = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
tt, x2, y2 = d[:, 0], d[:, 1], d[:, 2]
vx, vy = np.gradient(x2, tt), np.gradient(y2, tt)
speed = np.sqrt(vx**2 + vy**2)
print(f"Speed: mean {speed.mean():.2f}, std {speed.std():.2f}")

fig2, (p1, p2) = plt.subplots(1, 2, figsize=(11, 4.5))
p1.plot(x2, y2); p1.set_aspect("equal")
p1.set_xlabel("x (m)"); p1.set_ylabel("y (m)"); p1.set_title("Path")
p2.plot(tt, speed); p2.set_xlabel("Time (s)"); p2.set_ylabel("Speed")
p2.set_title("Speed over time")
fig2.tight_layout()
fig2.savefig("trajectory.png", dpi=150)