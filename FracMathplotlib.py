import tkinter
import numpy
from numba import jit
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt


root = tkinter.Tk()
root.wm_title("Embedding in Tk")


@jit()
def mandelbrot(Re, In, max_iter):
    c = complex(Re, In)
    z = 0.0j

    for i in range(max_iter):
        z = z * z + c
        if(z.real*z.real + z.imag*z.imag) >= 5:
            return 1
    return max_iter


columns =1000
rows = 1000

result = numpy.zeros([rows, columns])
for row_index, Rc in enumerate(numpy.linspace(-2, 1, num=rows)):
    for columns_index, Im in enumerate(numpy.linspace(-1, 1, num=columns)):
        res = mandelbrot(Rc, Im, 200)
        result[row_index, columns_index] = res
fig = plt.figure(dpi=100)
plt.imshow(result.T, cmap='hot', interpolation='bilinear', extent=[-2, 1, -1, 1])

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
tkinter.mainloop()