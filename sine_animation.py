import numpy as np, matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

k = 5
w = 100

x = np.linspace(0, 10, 1000)
t = np.linspace(0, 2*np.pi, 3000)

def wave(x, t):
    return np.cos(k*x - w*t)

plt.style.use('seaborn-darkgrid')

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(-1.1, 1.1)

line, = ax.plot(x, wave(x, t[0]))

def animation_frame(i):

    line.set_xdata(x)
    line.set_ydata(wave(x, t[i]))

    plt.title(r'$t = %.2f$' % t[i])

    return line,

plt.xlabel(r'$x$')
plt.ylabel(r'$\psi(x, t)$')

animation = FuncAnimation(fig, func = animation_frame, frames = range(len(t)), interval = 0.00001)
plt.show()
