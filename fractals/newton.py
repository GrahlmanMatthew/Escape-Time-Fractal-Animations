import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GIF_OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'newton', 'newton.gif'))
TOL = 1.e-8

class Newton():
    def __init__(self, f=lambda z:z**3 - 1, fprime=lambda z:3*z**2,startX=-1, startY=-1, WIDTH=2, HEIGHT=2, FRAMES=80, PATH=GIF_OUTPUT_PATH, COLOUR_BY="iteration"):
        """ :opt_param f: function whose shape to model
            :opt_param fprime: derivative of f
            :opt_param startX: x coordinate to start at on the x-axis
            :opt_param startY: y coordinate to start at on the y-axis
            :opt_param WIDTH: length of the x-axis, as a positive int
            :opt_param HEIGHT:  length of the y-axis, as a positive int
            :opt_param DPU: pixel density per unit
            :opt_param FRAMES: number of frames to generate in the gif
            :opt_param COLOUR_BY: use "iteratios" to colour the animation by iteration # or "root" to colour by root.
        """
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
        self.output_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'newton', PATH))
        self.cb = COLOUR_BY

    def __str__(self):
        fm = "\n\t"
        output = "The Newton Fracatal Parameters;" + fm
        output += "Function F: %s%s" % (self.f, fm)
        output += "Function F's Derivative: %s%s" % (self.fprime, fm)
        output += "Start X: %d%s" % (self.start_x, fm)
        output += "Start Y: %d%s" % (self.start_y, fm)
        output += "Width: %d%s" % (self.width, fm)
        output += "Height: %d%s" % (self.height, fm)
        output += "DPU: %d%s" % (self.dpu, fm)
        output += "Number of Frames: %d%s" % (self.frames, fm)
        output += "Outpath Path: %s%s" % (self.output_path, fm)       
        return output

    def newton(self, z0, MAX_IT=1000):
        """ The Newton-Raphson method applied to f(z). Returns the root found or False if no convergence was found. """
        z = z0
        for i in range(MAX_IT):
            dz = self.f(z)/self.fprime(z)
            if abs(dz) < TOL:
                if self.cb == "iteration":
                    return i
                return z
            z -= dz
        if self.cb == "iteration":
            return MAX_IT-1
        return False

    def create_animation(self):
        """ Creates a figSize_x by figSize_y figure, calls the animate function to plot the Mandelbrot set on it, the save the resulting animation as a .gif file.
            :opt_param OUTPATH_PATH: path to save the animated .gif of the Mandelbrot set. Defaults to ./output/mandelbrot.gif
        """
        if not os.path.isfile(self.output_path):
            figSize_x = 10
            figSize_y = 10
            fig = plt.figure(figsize=(figSize_x, figSize_y))

            anim = animation.FuncAnimation(fig, self.animate, frames= self.frames, interval=60, blit=True)
            anim.save(self.output_path, writer='ImageMagickWriter') 
        else:
            print("ERROR - File Already Exists! Skipping Animation Generation...")
                
    def animate(self, i):
        """ The animate function is called by matplotlib.animation librarys FuncAnimation to generate each frame in the output .gif file.
            :param int i: the frame number, starting from 0, to animate.
        """
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