import numpy as np
import scipy

def solver(a, b, c, d, e, f):
    A = np.matrix([[a, b], [d, e]])
    B = np.matrix([[c], [f]])

    #   Using numpy matrix pseudoinverse
    A_inv = np.linalg.pinv(A)
    ans = (A_inv * B)
    x = ans[0,0]
    y = ans[1,0]
    print("%f, %f" % (x, y))

    #   Using numpy solve()
    ans = np.linalg.solve(A, B)
    x = ans[0,0]
    y = ans[1,0]
    print("%f, %f" % (x, y))

    #   Using matrix inversion formula
    A_inv = 1/(e*a - b*d) * np.matrix([[e, -b], [-d, a]])
    ans = (A_inv * B)
    x = ans[0,0]
    y = ans[1,0]
    print("%f, %f" % (x, y))

solver(5, 8, 6, 7, 9, 4)

