from fractals.mandelbrot import Mandelbrot
from fractals.julia import Julia

m = Mandelbrot()
print(m)
m.create_animation()

j = Julia()
print(j)
j.create_animation()