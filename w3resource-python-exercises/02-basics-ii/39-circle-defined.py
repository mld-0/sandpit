import sympy
from sympy.solvers.solveset import nonlinsolve
from sympy import Symbol, Eq

#   How on earth to get the general algebraic solution? (this being slooow)

def circle_defined(a, b, c):
    R = Symbol('R', real=True)
    x = Symbol('x', real=True)
    y = Symbol('y', real=True)
    equ1 = (a[0] - x)**2 + (a[1] - y)**2 - R
    equ2 = (b[0] - x)**2 + (b[1] - y)**2 - R
    equ3 = (c[0] - x)**2 + (c[1] - y)**2 - R
    equ_set = [equ1, equ2, equ3]
    result = nonlinsolve(equ_set, [x,y,R])
    _x, _y, _R = tuple(*result)
    _x = _x.evalf()
    _y = _y.evalf()
    _R = _R.evalf()
    _r = _R ** 0.5
    print("Centre=(%f, %f), radius=%f" % (_x, _y, _r))

circle_defined([9, 3], [6, 8], [3, 6])
