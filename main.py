from fractals.mandelbrot import Mandelbrot
from fractals.julia import Julia
from fractals.burningship import BurningShip

m = Mandelbrot()
print(m)
m.create_animation()

j = Julia()
print(j)
j.create_animation()

b = BurningShip()
print(b)
b.create_animation()