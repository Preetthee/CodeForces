import math
from math import fabs
def f(x):
    return math.exp(-x) - x
def secant(f, x0, x1, max_iter=500, eps=0.0001):
    iteration = 1
    while True:
        f0 = f(x0)
        f1 = f(x1)
        if f1 - f0 == 0:
            print("Denominator became zero. Try different initial guesses.")
            return None
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        ae = fabs(x2 - x1)
        x0 = x1
        x1 = x2
        iteration += 1
        if ae < eps or iteration > max_iter:
            break
    return x1
x0 = 0
x1 = 1
xr = secant(f, x0, x1)
if xr is not None:
    print(f"root at x = {xr:.4f}")
    print(f"f(xr) = {f(xr):.4f}")
