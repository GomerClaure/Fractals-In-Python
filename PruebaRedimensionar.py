import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider


def koch_snowflake(order, scale=10):
    """
    Return two lists x, y of point coordinates of the Koch snowflake.

    Arguments
    ---------
    order : int
        The recursion depth.
    scale : float
        The extent of the snowflake (edge length of the base triangle).
    """
    def _koch_snowflake_complex(order):
        if order == 0:
            # initial triangle
            angles = np.array([0, 120, 240]) + 90
            return scale / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
        else:
            ZR = 0.5 - 0.5j * np.sqrt(3) / 3

            p1 = _koch_snowflake_complex(order - 1)  # start points
            p2 = np.roll(p1, shift=-1)  # end points
            dp = p2 - p1  # connection vectors

            new_points = np.empty(len(p1) * 4, dtype=np.complex128)
            new_points[::4] = p1
            new_points[1::4] = p1 + dp / 3
            new_points[2::4] = p1 + dp * ZR
            new_points[3::4] = p1 + dp / 3 * 2
            return new_points

    points = _koch_snowflake_complex(order)
    x, y = points.real, points.imag
    return x, y

order = range(4)
TWOPI = 2*np.pi

fig, ax = plt.subplots()

x, y = koch_snowflake(order=0)
initial_amp = 0
l, = plt.plot(x, y, lw=2)

# ax = plt.axis([0,TWOPI,-1,1])

axamp = plt.axes([0.25, .01, 0.50, 0.04])
# Slider
samp = Slider(axamp, 'Valor', valmin=0, valmax=1, valinit=initial_amp)

def update(val):
    # amp is the current value of the slider
    amp = samp.val
    num = int(amp*10)
    print(amp)
    x, y = koch_snowflake(order=num)

    # update curve
    l.set_data(x, y)
    # redraw canvas while idle
    fig.canvas.draw_idle()

# call update function on slider value change
samp.on_changed(update)

plt.show()


# import numpy as np # pip install numpy
# import pandas as pd # pip install pandas
# import matplotlib.pyplot as plt # pip install matplotlib
# import seaborn as sns # pip install seaborn
# from matplotlib.animation import FuncAnimation
#
#
# def create_frame(step, ax):
#     ax.cla()
#     sns.lineplot(x=x[:step], y=y[:step], ax = ax)
#
# # Código para generar una función de distribución
# normal = np.random.normal(loc=5, scale=100, size=10_000)
# y, x = np.histogram(normal, bins=100)
# x = (x[1:] + x[:-1]) / 2
# y = np.cumsum(y)
# timesteps = 16
# columns = 4
# fig = plt.figure()
# ax = fig.gca()
# # create_frame(10, ax)
# # animation = FuncAnimation(fig, create_frame, frames=100, fargs=(ax,))
# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# TWOPI = 2*np.pi
#
# fig, ax = plt.subplots()
#
# t = np.arange(0.0, TWOPI, 0.001)
# s = np.sin(t)
# l = plt.plot(t, s)
#
# ax = plt.axis([0,TWOPI,-1,1])
#
# redDot, = plt.plot([0], [np.sin(0)], 'ro')
#
# def animate(i):
#     print(i)
#     redDot.set_data(i, np.sin(i))
#     return redDot,
#
# # create animation using the animate() function
# a =[0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
#        1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. , 2.1, 2.2, 2.3, 2.4, 2.5,
#        2.6, 2.7, 2.8, 2.9, 3. , 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8,
#        3.9, 4. , 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5. , 5.1,
#        5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6. , 6.1, 6.2]
# myAnimation = animation.FuncAnimation(fig, animate, frames=11, interval=0, blit=True, repeat=True)
#
# plt.show()
