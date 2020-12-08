import numpy
from numba import jit
import matplotlib.pyplot as plt


@jit()
def mandelbrot(Re, In, max_iter):
    c = complex(Re, In)
    z = 0.0j

    for i in range(max_iter):
        z = z * z + c
        if(z.real*z.real + z.imag*z.imag) >= 5:
            return 1
    return max_iter


columns =5000
rows = 5000

result = numpy.zeros([rows, columns])
for row_index, Rc in enumerate(numpy.linspace(-2, 1, num=rows)):
    for columns_index, Im in enumerate(numpy.linspace(-1, 1, num=columns)):
        res = mandelbrot(Rc, Im, 200)
        result[row_index, columns_index] = res
plt.figure(dpi=1000)
plt.imshow(result.T, cmap='hot', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.xlabel('Re')
plt.ylabel('In')
plt.savefig("Ejemplo3-dpi1000.png")
plt.show()
