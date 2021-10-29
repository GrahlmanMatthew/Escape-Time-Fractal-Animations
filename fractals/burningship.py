import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GIF_OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'burningship.gif'))

class BurningShip:  
    def __init__(self, startX= -2, startY= -1.5, WIDTH= 3, HEIGHT= 3, DPU= 250, FRAMES=35):
        """ Constructor for the Burning Ship set class which initializes the required parameters to defaults if none are provided.
        
            :opt_param startX: x coordinate to start at on the x-axis
            :opt_param startY: y coordinate to start at on the y-axis
            :opt_param WIDTH: length of the x-axis, as a positive int
            :opt_param HEIGHT:  length of the y-axis, as a positive int
            :opt_param DPU: pixel density per unit
            :opt_param FRAMES: number of frames to generate in the gif
        """

        self.start_x = startX
        self.start_y = startY
        self.width = WIDTH
        self.height = HEIGHT
        self.dpu = DPU
        self.num_frames = FRAMES
        self.real_axis = np.linspace(self.start_x, self.start_x + self.width, self.width * self.dpu)
        self.imag_axis = np.linspace(self.start_y, self.start_y + self.height, self.height * self.dpu)

    def __str__(self):
        return "Burning Ship set parameters;\n\tStart X: %d,\n\tStart Y: %d,\n\tWidth: %d,\n\tHeight: %d,\n\tDPU: %d,\n\tNUM FRAMES: %d" % (self.start_x, self.start_y, self.width, self.height, self.dpu, self.num_frames)

    def create_animation(self, OUTPUT_PATH=GIF_OUTPUT_PATH):
        """ Creates a figSize_x by figSize_y figure, calls the animate function to plot the Burning Ship set on it, the save the resulting animation as a .gif file.
            
            :opt_param OUTPATH_PATH: path to save the animated .gif of the Burning Ship set. Defaults to ./output/burningship.gif
        """
        if not os.path.isfile(OUTPUT_PATH):
            figSize_x = 10
            figSize_y = 10
            fig = plt.figure(figsize=(figSize_x, figSize_y))

            anim = animation.FuncAnimation(fig, self.animate, frames=self.num_frames, interval=120, blit=True)
            anim.save(OUTPUT_PATH, writer='ImageMagickWriter')
    
    def animate(self, i):
        """ The animate function is called by matplotlib.animation librarys FuncAnimation to generate each frame in the output .gif file.
            :param int i: the frame number, starting from 0, to animate.
        """

        ax = plt.axes() # axes obj
        ax.clear()  # clear axes object
        ax.set_xticks([], minor=False)   # clear x ticks
        ax.set_yticks([], minor=False)   # clear y ticks

        x = np.empty((len(self.real_axis), len(self.imag_axis)))    # re-initialize the array-like image
        max_iterations = 256     # calculate the current threhold
        num_iterations = round(1.15**(i+1)) 

        for i in range(len(self.real_axis)):
            for j in range(len(self.imag_axis)):
                x[i, j] = self.burningship(self.real_axis[i], self.imag_axis[j], num_iterations)

        # associate colours with iterations
        img = ax.imshow(x.T, interpolation='bicubic', cmap='magma')
        return [img]

    def burningship(self, x, y, num_iterations):
        """ Calculates whether the number c (c = x + iy) belongs to the Mandelbrot set.
            In order to belong to the Mandelbrot set, the sequence z[i+1] = z[i]**2 + c must NOT diverage after num_iterations.
            The sequence diverges if the absolute value of z[i+1] > 4

            :param float x: x component of init complex #
            :param float y: y component of init complex #
            :param int num_iterations: the # of iterations to determine whether the sequence converges
        """ 

        c = complex(-0.8, -0.8)
        
        for i in range(num_iterations):
            zx = x**2 - y**2 + x
            zy = 2 * abs(x*y) + y
            z = complex(zx, zy)
            z = z**2 + c
            if abs(z) > 4:
               return i
        return num_iterations-1

