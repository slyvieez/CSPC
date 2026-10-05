"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

def gradient_descent(df,x0,lr=0.1,tol=1e-8,max_iteration=10000):
    #   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny
    x=x0
    for i in range(max_iteration):
        step=lr*df(x)
        x=x-step
        if abs(step)<tol:
            break
    return x

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:

#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")
print("Gradient descent:", gradient_descent(df, 0.0))
print("Newton          :", newton(df, 0.0, fprime=d2f))
print("SLSQP           :", minimize(f, 0.0, method="SLSQP").x[0])

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

for x0 in (0.0, 2.0):
    print(f"\n=== 2B: g(x) = x^4 - 3x^2 + x + 5, start x0 = {x0} ===")
    x_g = gradient_descent(dg, x0, lr=0.01)
    x_n = newton(dg, x0, fprime=d2g)
    x_s = minimize(g, x0, method="SLSQP").x[0]
    kind = "MINIMUM" if d2g(x_n) > 0 else "MAXIMUM"
    print(f"Gradient descent: x = {x_g:.4f}, g = {g(x_g):.4f}")
    print(f"Newton          : x = {x_n:.4f}, g = {g(x_n):.4f}, g'' = {d2g(x_n):.3f} -> {kind}")
    print(f"SLSQP           : x = {x_s:.4f}, g = {g(x_s):.4f}")

#will add to readme