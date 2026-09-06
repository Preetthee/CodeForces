from math import fabs
def f(x):
    return x*x*x - 2*x - 5
def f_deriv(x):
    return 3*x*x - 2
def newton_rapson(f, f_deriv, x0, max_iter=500, eps=0.005):
    if (f_deriv(x0) == 0):
        print("Change the initial guess")
        return
    iter = 1
    xr_old = x0
    while True:
        if (f_deriv(xr_old) == 0):
            print("Change the initial guess")
            return
        xr_new = xr_old - (f(xr_old) / f_deriv(xr_old))
        ae = fabs(xr_new - xr_old)
        xr_old = xr_new
        iter = iter + 1
        if ae <= eps or iter > max_iter:
            break
    return xr_old
x0 = 2
xr = newton_rapson(f, f_deriv, x0)
print(f"Root is at {xr:.4f}")
print(f"f(xr)= {f(xr):.4f}")