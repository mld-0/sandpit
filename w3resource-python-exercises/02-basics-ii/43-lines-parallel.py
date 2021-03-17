
def lines_parallel(P, Q, R, S):
    m1 = (P[1]-Q[1]) / (P[0]-Q[0])
    m2 = (R[1]-S[1]) / (R[0]-S[0])
    print(m1)
    print(m2)
    if (m1 == m2):
        print("Parallel")
    else:
        print("Not Parallel")

lines_parallel([2,5], [6,4], [4,8], [3,9])

