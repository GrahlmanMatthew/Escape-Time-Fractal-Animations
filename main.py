from fractals.mandelbrot import Mandelbrot
from fractals.julia import Julia
from fractals.burningship import BurningShip
from fractals.newton import Newton

m = Mandelbrot()
print(m)
m.create_animation()

j = Julia()
print(j)
j.create_animation()

b = BurningShip()
print(b)
b.create_animation()

n = Newton(COLOUR_BY="iterations")
print(n)
n.create_animation()