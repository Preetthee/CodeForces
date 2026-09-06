from math import fabs
def f(x):
    return x**3 - x*2 - 5
def root_falsepos(f, xl, xu, max_itr=500, eps=0.05):
    if f(xl) * f(xu) > 0:
        print("Wrong guess")
        return None
    if f(xl) * f(xu) == 0:
        if f(xl) == 0:
            return xl
        else:
            return xu
    iter = 1
    xr_old = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))
    while True:
        xr = xr_old

        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            return xr

        xr_new = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))
        ae = fabs(xr_new - xr_old)
        xr_old = xr_new
        iter = iter + 1

        if ae <= eps or iter > max_itr:
            break
    return xr_old
xl, xu = 1, 3
xr = root_falsepos(f, xl, xu)
if xr is not None:
    print(f"root is at {xr:.2f}")
    print(f"f(xr) = {f(xr):.2f}")