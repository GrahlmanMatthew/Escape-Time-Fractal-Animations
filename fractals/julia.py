import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GIF_OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'julia.gif'))

class Julia:
    def __init__(self):
        """ Constructor for the Julioa set class which initializes the required parameters to defaults if none are provided.
        
            :opt_param startX: x coordinate to start at on the x-axis
            :opt_param startY: y coordinate to start at on the y-axis
            :opt_param WIDTH: length of the x-axis, as a positive int
            :opt_param HEIGHT:  length of the y-axis, as a positive int
            :opt_param DPU: pixel density per unit
            :opt_param THRESHOLD: max # of iterations
            :opt_param FRAMES: number of frames to generate in the gif
        """

        self.start_x = -2
        self.start_y = -2
        self.width = 4
        self.height = 4
        self.dpu = 200
        self.threshold = 20
        self.num_frames = 100
        self.real_axis = np.linspace(self.start_x, self.start_x + self.width, self.width * self.dpu)
        self.imag_axis = np.linspace(self.start_y, self.start_y + self.height, self.height * self.dpu)

    def __str__(self):
        return "Julia set parameters;\n\tStart X: %d,\n\tStart Y: %d,\n\tWidth: %d,\n\tHeight: %d,\n\tDPU: %d,\n\tThreshold: %d, NUM FRAMES: %d" % (self.start_x, self.start_y, self.width, self.height, self.dpu, self.threshold, self.num_frames)

    def create_animation(self, OUTPUT_PATH=GIF_OUTPUT_PATH):
        """ Creates a figSize_x by figSize_y figure, calls the animate function to plot the Julia set, then saves the resulting animation as a .gif file.

            :opt_param OUTPUT_PATH: path to save the animated .gif of the Julia set. Defaults to ./output/julia.gif
        """
        if not os.path.isfile(OUTPUT_PATH):
            figSize_x = 10
            figSize_y = 10
            fig = plt.figure(figsize=(figSize_x, figSize_y))

            anim = animation.FuncAnimation(fig, self.animate, frames= self.num_frames, interval=50, blit=True)
            anim.save(OUTPUT_PATH, writer='ImageMagickWriter') 

    def animate(self, i):
        """ The animate function is called by matplotlib.animation librarys FuncAnimation to generate each frame in the output .gif file.
            :param int i: the frame number, starting from 0, to animate.
        """

        r = 0.7885
        a = np.linspace(0, 2*np.pi, self.num_frames)
        
        ax = plt.axes()  # create an axes object
        ax.clear()  # clear axes object
        ax.set_xticks([], minor=False)   # clear x ticks
        ax.set_yticks([], minor=False)   # clear y ticks
        
        x = np.empty((len(self.real_axis), len(self.imag_axis)))
        cx = r * np.cos(a[i])
        cy = r * np.sin(a[i])
        
        for i in range(len(self.real_axis)):
            for j in range(len(self.imag_axis)):
                x[i, j] = self.julia_quadratic(self.real_axis[i], self.imag_axis[j], cx, cy, self.threshold)
        
        img = ax.imshow(x.T, interpolation="bicubic", cmap='viridis')
        return [img]

    def julia_quadratic(self, zx, zy, cx, cy, threshold):
        """ Calculates whether the number z[0] = zx + izy with a constant c = x + iy belongs to the Julia set.
            In order to belong to the Julia set, the sequence z[i+1] = z[i]**2 + c must NOT diverse after 'threshold' number of iterations. 
            The sequence diverges if the absolute value of z[i+1] > 4

            :param float zx: x component of z[0]
            :param float zy: y component of z[0]
            :param float cx: x component of the constant c
            :param float cy: y component of the constant c
            :param int threshold: the # of iterations to determine whether the sequence converges
        """

        z = complex(zx, zy)
        c = complex(cx, cy)
        
        for i in range(threshold):
            z = z**2 + c
            if abs(z) > 4.:  # it diverged
                return i
            
        return threshold - 1  # it didn't diverge