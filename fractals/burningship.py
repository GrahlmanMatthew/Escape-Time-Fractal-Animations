import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from fractals.mandelbrot import Mandelbrot

GIF_OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'burningship2.gif'))

class BurningShip(Mandelbrot):  
    def __init__(self, startX= -2, startY= -1.5, WIDTH= 3, HEIGHT= 3, DPU= 250, FRAMES=35):
        """ Constructor for the Burning Ship fractal, which is a child of the Mandelbrot set.
            This constructor will initialize the parameters to defaults if none are provided.
        
            :opt_param startX: x coordinate to start at on the x-axis
            :opt_param startY: y coordinate to start at on the y-axis
            :opt_param WIDTH: length of the x-axis, as a positive int
            :opt_param HEIGHT:  length of the y-axis, as a positive int
            :opt_param DPU: pixel density per unit
            :opt_param FRAMES: number of frames to generate in the gif
        """

        super().__init__(startX=startX, startY=startY, WIDTH=WIDTH, HEIGHT=HEIGHT, DPU=DPU, FRAMES=FRAMES)

    def __str__(self):
        return "Burning Ship set parameters;\n\tStart X: %d,\n\tStart Y: %d,\n\tWidth: %d,\n\tHeight: %d,\n\tDPU: %d,\n\tNUM FRAMES: %d" % (self.start_x, self.start_y, self.width, self.height, self.dpu, self.num_frames)

    def create_animation(self, OUTPUT_PATH=GIF_OUTPUT_PATH):
        """ Passes the output path for the Burning SHip .gif to the parent's create_animation function in order to begin generating the animation.
            
            :opt_param OUTPATH_PATH: path to save the animated .gif of the Burning Ship set. Defaults to ./output/burningship.gif
        """
        super().create_animation(OUTPUT_PATH=OUTPUT_PATH)

    def mandelbrot(self, x, y, num_iterations):
        """ Calculates whether the number c (c = x + iy) belongs to the modified version of the Mandelbrot set known as the Burning Ship fractal.
            In order to belong to the Burning Ship fractal, the sequence z[i+1] = (abs(Real z[i]) + abs(Imaginary z[i]))**2 + c must NOT diverage after num_iterations.
            The sequence diverges if the absolute value of z[i+1] > 4

            :param float x: x component of init complex #
            :param float y: y component of init complex #
            :param int num_iterations: the # of iterations to determine whether the sequence converges
        """ 

        c = complex(-0.8, -0.8)
        zx = x
        zy = y
        
        for i in range(num_iterations):
            next_zx = zx**2 - zy**2 + x
            zy = 2 * abs(zx*zy) + y
            zx = next_zx
            z = complex(zx, zy)**2 + c
            if abs(z) > 4:
               return i
        return num_iterations-1