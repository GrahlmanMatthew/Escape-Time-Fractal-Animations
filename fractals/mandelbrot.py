import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GIF_OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'mandelbrot.gif'))

class Mandelbrot:  
    def __init__(self):
        self.start_x = -2
        self.start_y = -1.5
        self.width = 3
        self.height = 3
        self.dpu = 250  # pixel density per unit
        self.real_axis = np.linspace(self.start_x, self.start_x + self.width, self.width * self.dpu)
        self.imag_axis = np.linspace(self.start_y, self.start_y + self.height, self.height * self.dpu)

    def __str__(self):
        return "Mandelbrot set parameters;\n\tStart X: %d,\n\tStart Y: %d,\n\tWidth: %d,\n\tHeight: %d,\n\tDPU: %d" % (self.start_x, self.start_y, self.width, self.height, self.dpu)

    def create_animation(self, OUTPUT_PATH=GIF_OUTPUT_PATH):
        """ Creates a figSize_x by figSize_y figure, calls the animate function to plot the Mandelbrot set on it, the save the resulting animation as a .gif file.
            
            :param OUTPATH_PATH: location to save the .gif animation of the Mandelbrot set. Defaults to ./output/mandelbrot.gif
        """
        if not os.path.isfile(OUTPUT_PATH):
            figSize_x = 10
            figSize_y = 10
            fig = plt.figure(figsize=(figSize_x, figSize_y))

            anim = animation.FuncAnimation(fig, self.animate, frames=45, interval=120, blit=True)
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
        num_iterations = round(1.15**(i+1))      # calculate the current threhold

        for i in range(len(self.real_axis)):
            for j in range(len(self.imag_axis)):
                x[i, j] = self.mandelbrot(self.real_axis[i], self.imag_axis[j], num_iterations)

        # associate colours with iterations
        img = ax.imshow(x.T, interpolation='bicubic', cmap='magma')
        return [img]

    def mandelbrot(self, x, y, num_iterations):
        """ Calculates whether the number c (c = x + iy) belongs to the Mandelbrot set.
            In order to belong to the Mandelbrot set, the sequence z[i+1] = z[i]**2 + c must NOT diverage after num_iterations.
            The sequence diverges if the absolute value of z[i+1] > 4

            :param float x: x component of init complex #
            :param float y: y component of init complex #
            :param int num_iterations: the # of iterations to determine whether the sequence converges
        """ 

        c = complex(x, y)
        z = complex(0, 0)
        
        for i in range(num_iterations):
            z = z**2 + c
            if abs(z) > 4:  # divergent (c does not belong to the set)
                return i
        
        return num_iterations - 1    # does not diverge (c belongs to the set)
