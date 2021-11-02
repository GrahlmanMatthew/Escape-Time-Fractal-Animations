import os
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GIF_OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'newton.gif'))
TOL = 1.e-8

class Newton():
    def __init__(self, f=lambda z:z**3 - 1, fprime=lambda z:3*z**2,startX=-1, startY=-1, WIDTH=2, HEIGHT=2, FRAMES=20):
        self.f = f
        self.fprime =fprime
        self.start_x = startX
        self.start_y = startY
        self.width = WIDTH
        self.height = HEIGHT
        self.max_num_iterations = 1000
        self.dpu = 250
        self.frames = FRAMES
        self.real_axis = np.linspace(self.start_x, self.start_x + self.width, self.width * self.dpu)
        self.imag_axis = np.linspace(self.start_y, self.start_y + self.height, self.height * self.dpu)

    def newton(self, z0, MAX_IT=1000):
        z = z0
        for i in range(MAX_IT):
            dz = self.f(z)/self.fprime(z)
            if abs(dz) < TOL:
                return i
            z -= dz
        return MAX_IT-1

    def animate(self, i):
        roots = []
        m = np.zeros((self.width * self.dpu, self.height * self.dpu))
        num_iterations = round(1.15**(i+1)) 
        def get_root_index(roots, r):
            try:
                return np.where(np.isclose(roots, r, atol=TOL))[0][0]
            except IndexError:
                roots.append(r)
                return len(roots) - 1  

        ax = plt.axes()  # create an axes object
        ax.clear()  # clear axes object
        ax.set_xticks([], minor=False)   # clear x ticks
        ax.set_yticks([], minor=False)   # clear y ticks

        for ix, x in enumerate(self.real_axis):
            for iy, y in enumerate(self.imag_axis):
                z0 = x + y*1j
                r = self.newton(z0, MAX_IT=num_iterations)
                if r is not False:
                    ir = get_root_index(roots, r)
                    m[iy, ix] = ir

        img = ax.imshow(m.T, interpolation="bicubic", cmap='viridis')    
        return [img]

    def create_animation(self, OUTPUT_PATH=GIF_OUTPUT_PATH):
        if not os.path.isfile(OUTPUT_PATH):
            figSize_x = 10
            figSize_y = 10
            fig = plt.figure(figsize=(figSize_x, figSize_y))

            anim = animation.FuncAnimation(fig, self.animate, frames= self.frames, interval=60, blit=True)
            anim.save(OUTPUT_PATH, writer='ImageMagickWriter') 

# ------------------------------------
# ORIGINAL UNMODIFIED AND WORKING
# ------------------------------------

# def newton(z0, f, fprime, MAX_IT=1000):
#     z = z0
#     for i in range(MAX_IT):
#         dz = f(z)/fprime(z)
#         if abs(dz) < TOL:
#             return i
#         z -= dz
#     return MAX_IT-1

# def animate(i, f=lambda z: z**9 - 1, fprime= lambda z: 9*z**8, n=500, domain=(-1, 1, -1, 1)):
#     roots = []
#     m = np.zeros((n, n))
#     num_iterations = round(1.15**(i+1)) 
#     def get_root_index(roots, r):
#         try:
#             return np.where(np.isclose(roots, r, atol=TOL))[0][0]
#         except IndexError:
#             roots.append(r)
#             return len(roots) - 1  

#     ax = plt.axes()  # create an axes object
#     ax.clear()  # clear axes object
#     ax.set_xticks([], minor=False)   # clear x ticks
#     ax.set_yticks([], minor=False)   # clear y ticks

#     xmin, xmax, ymin, ymax = domain
#     for ix, x in enumerate(np.linspace(xmin, xmax, n)):
#         for iy, y in enumerate(np.linspace(ymin, ymax, n)):
#             z0 = x + y*1j
#             r = newton(z0, f, fprime, MAX_IT=num_iterations)
#             if r is not False:
#                 ir = get_root_index(roots, r)
#                 m[iy, ix] = ir
#     nroots = len(roots)

#     img = ax.imshow(m.T, interpolation="bicubic", cmap='viridis')    
#     return [img]

# def create_animation(OUTPUT_PATH=GIF_OUTPUT_PATH):
#     if not os.path.isfile(OUTPUT_PATH):
#         figSize_x = 10
#         figSize_y = 10
#         fig = plt.figure(figsize=(figSize_x, figSize_y))

#         anim = animation.FuncAnimation(fig, animate, frames= 90, interval=60, blit=True)
#         anim.save(OUTPUT_PATH, writer='ImageMagickWriter') 

# create_animation()

# f = lambda z: z**3 - 1
# fprime = lambda z: 3*z**2
# plot_newton_fractal(f, fprime, n=500)
