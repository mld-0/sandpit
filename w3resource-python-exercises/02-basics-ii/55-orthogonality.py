def orthogonality_check(P, Q, R, S):
    #   vertical line -> div / 0
    try:
        m_PQ = (P[1] - Q[1]) / (P[0] - Q[0])
    except ZeroDivisionError:
        m_RS = (R[1] - S[1]) / (R[0] - S[0])
        if (m_RS == 0):
            print("Orthogonal")
        else:
            print("Not Orthogonal")
        return

    try:
        m_RS = (R[1] - S[1]) / (R[0] - S[0])
    except ZeroDivisionError:
        m_PQ = (P[1] - Q[1]) / (P[0] - Q[0])
        if (m_PQ == 0):
            print("Orthogonal")
        else:
            print("Not Orthogonal")
        return

    print(m_PQ)
    print(m_RS)

    if (m_PQ == -1 / m_RS):
        print("Orthogonal")
    else:
        print("Not Orthogonal")

P = (4.5, -2.5)
Q = (-2.5, 4.5)
R = (3.5, 3.5)
S = (3.8, -3.5)
orthogonality_check(P, Q, R, S)

P = (4.5, -2.5)
Q = (4.5, 4.5)
R = (3.5, 6.5)
S = (1.5, 6.5)
orthogonality_check(P, Q, R, S)


