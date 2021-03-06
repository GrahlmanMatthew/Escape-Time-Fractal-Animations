# Escape-Time Fractal Animations
## What are Escape-Time Fractals?
First and foremost, fractals are geometric shapes which display a unique property known as self-similarity. This means that they have the same pattern(s) embedded within themselves at different scales, which remains true at arbitrarily small scales.

While many distinct types of fractals exist, this project only focuses on animating the subset known as escape-time (or orbit) fractals. These fractals can be generated by iterating through a formula on each point within a given space. If a point begins to diverge as the formula iterates, it *escapes*; otherwise, it remains bounded. Four of the most well-known escape-time fractals are the Mandelbrot set, Julia set, Burning Ship fractal, and the Newton fractal. 

## The Mandelbrot Set
The Mandelbrot set is the set of complex numbers c for which the function f<sub>c</sub>(z) = z<sup>2</sup> + c does not diverge to infinity when iterated from z<sub>0</sub> = 0.

<img src="./output/mandelbrot/sample-mandelbrot.gif" width="300" height="300" title="Mandelbrot Set; X=-2, Y=-1.5, Width=3, Height=3, and DPU=250">

## The Julia Set
The Julia set, defined by the function f<sub>c</sub>(z) = z<sup>2</sup> + c, consists of values such that an arbitrarily small perturbation can cause chaotic, changes in the sequence of iterated function values. For a fixed parameter c, the Julia set is found by iterating the function on each point z.

<img src="./output/julia/sample-julia.gif" width="300" height="300" title="Julia Set; R=0.7885, X=-2, Y=-2, Width=4, Height=4, Threshold = 20, and DPU=200">
<img src="./output/julia/sample-julia-2.gif" width="300" height="300" title="Julia Set; R=0.285, X=-2, Y=-2, Width=4, Height=4, Threshold = 20, and DPU=200">

## The Burning Ship Fractal
The Burning Ship Fractal is a variant of the Mandelbrot set. This fractal can be generated by iterating the function z<sub>n+1</sub> = (|Real(z<sub>n</sub>)| + i|Imaginary(z<sub>n</sub>)|)<sup>2</sup> + c, z<sub>0</sub> = 0 in the complex plane c, which will either escape or remain bounded. The difference between it and the Mandelbrot set is that we take the absolute values of both the real and imaginary components before squaring at each iteration.

<img src="./output/burningship/sample-burningship.gif" width="300" height="300" title="Burning Ship Fractal; X=-2, Y=-1.5, Width=3, Height=3, and DPU=250">

## The Newton Fractal
A generalization of Newton's iteration can be defined by z<sub>n+1</sub> = z<sub>n</sub> - a(f(z<sub>n</sub>) / f'(z<sub>n</sub>)) where the special choice a = 1 corresponds to the Newton Fractal. This fractal differs from the previous ones in the sense that it applies Newton’s method to a fixed function then checks whether a point converges to a root. 

### Output for f(z) = z<sup>3</sup> - 1
<img src="./output/newton/sample-newton-cbRoot.gif" width="300" height="300" title="The Newton Fractal, coloured by root.">
<img src="./output/newton/sample-newton-cbIteration.gif" width="300" height="300" title="The Newton Fractal, coloured by itration #.">

### Newton Fractal for f(z) = z<sup>5</sup> + z<sup>3</sup> + z - 1
<img src="./output/newton/sample-newton2-cbRoot.gif" width="300" height="300" title="The Newton Fractal 2, coloured by root.">
<img src="./output/newton/sample-newton2-cbIteration.gif" width="300" height="300" title="The Newton Fractal 2, coloured by itration #.">

### Newton Fractal for f(z) = z<sup>9</sup> + z<sup>6</sup> + z<sup>3</sup> - 1
<img src="./output/newton/sample-newton3-cbRoot.gif" width="300" height="300" title="The Newton Fractal 3, coloured by root.">
<img src="./output/newton/sample-newton3-cbIteration.gif" width="300" height="300" title="The Newton Fractal 3, coloured by itration #.">

## References
1. [Wikipedia - Fractals](https://en.wikipedia.org/wiki/Fractal)
2. [Maplesoft - Escape Time Fracatals](https://www.maplesoft.com/support/help/maple/view.aspx?path=MathApps/EscapeTimeFractals)
3. [Matplotlib - Animate Your Own Fractals in Python with Matplotlib](https://matplotlib.org/matplotblog/posts/animated-fractals/)
4. [Wikipedia - Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set)
5. [Complex Analysis - The Mandelbrot Set](https://complex-analysis.com/content/mandelbrot_set.html)
6. [Wikipedia - Julia Set](https://en.wikipedia.org/wiki/Julia_set)
7. [Wikipedia - Burning Ship Fractal](https://en.wikipedia.org/wiki/Burning_Ship_fractal)
8. [Wikipedia - Newton Fractal](https://en.wikipedia.org/wiki/Newton_fractal)
9. [Learning Scientific Programming with Python - The Newton Fractal](https://scipython.com/book2/chapter-8-scipy/examples/the-newton-fractal/)