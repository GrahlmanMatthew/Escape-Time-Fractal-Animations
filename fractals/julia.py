import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

GIF_OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'julia', 'julia.gif'))

class Julia:
    def __init__(self, R=0.7885, startX=-2, startY=-2, WIDTH=4, HEIGHT=4, DPU=200, THRESH=20, FRAMES=100, PATH=GIF_OUTPUT_PATH):
        """ :opt_param R: fixed value where R^2 - R >= |c|
            :opt_param startX: x coordinate to start at on the x-axis
            :opt_param startY: y coordinate to start at on the y-axis
            :opt_param WIDTH: length of the x-axis, as a positive int
            :opt_param HEIGHT:  length of the y-axis, as a positive int
            :opt_param DPU: pixel density per unit
            :opt_param THRESHOLD: max # of iterations
            :opt_param FRAMES: number of frames to generate in the gif
            :opt_param PATH: output file name to save generated animation
        """
        self.r = R
        self.start_x = startX
        self.start_y = startY
        self.width = WIDTH
        self.height = HEIGHT
        self.dpu = DPU
        self.threshold = THRESH
        self.num_frames = FRAMES
        self.real_axis = np.linspace(self.start_x, self.start_x + self.width, self.width * self.dpu)
        self.imag_axis = np.linspace(self.start_y, self.start_y + self.height, self.height * self.dpu)
        self.output_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output', 'julia', PATH))

    def __str__(self):
        fm = "\n\t"
        output = "Julia Set Parameters;" + fm
        output += "R: %f%s" % (self.r, fm)
        output += "Start X: %d%s" % (self.start_x, fm)
        output += "Start Y: %d%s" % (self.start_y, fm)
        output += "Width: %d%s" % (self.width, fm)
        output += "Height: %d%s" % (self.height, fm)
        output += "DPU: %d%s" % (self.dpu, fm)
        output += "Threshold: %d%s" % (self.threshold, fm)
        output += "Number of Frames: %d%s" % (self.num_frames, fm)
        output += "Outpath Path: %s%s" % (self.output_path, fm)       
        return output

    def create_animation(self):
        """ Creates a figSize_x by figSize_y figure, calls the animate function to plot the Julia set on it, the save the resulting animation as a .gif file.
            :opt_param OUTPUT_PATH: path to save the animated .gif of the Julia set. Defaults to ./output/julia.gif
        """
        if not os.path.isfile(self.output_path):
            figSize_x = 10
            figSize_y = 10
            fig = plt.figure(figsize=(figSize_x, figSize_y))

            anim = animation.FuncAnimation(fig, self.animate, frames= self.num_frames, interval=50, blit=True)
            anim.save(self.output_path, writer='ImageMagickWriter') 
        else:
            print("ERROR - File Already Exists! Skipping Animation Generation...")
   
    def animate(self, i):
        """ The animate function is called by matplotlib.animation librarys FuncAnimation to generate each frame in the output .gif file.
            :param int i: the frame number, starting from 0, to animate.
        """
        ax = plt.axes()  # create an axes object
        ax.clear()  # clear axes object
        ax.set_xticks([], minor=False)   # clear x ticks
        ax.set_yticks([], minor=False)   # clear y ticks
        
        a = np.linspace(0, 2*np.pi, self.num_frames)
        x = np.empty((len(self.real_axis), len(self.imag_axis)))
        cx = self.r 
        cy = self.r + a[i]
        
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