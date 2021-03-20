
def check_parallel(A, B):
    """Given two lines represented as A=[a,b,c] where ax+by=c, determine whether A and B are parallel."""
    m1 = -1 * A[0] / A[1]
    m2 = -1 * B[0] / B[1]
    print( m1 == m2 )

check_parallel([2,3,4], [2,3,8])
check_parallel([2,3,4], [4,-3,8])
