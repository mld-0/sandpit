
def touching_circles(c1, r1, c2, r2):
    centre_distance = ((c1[1] - c2[1])**2 + (c1[0] - c2[0])**2)**0.5
    print(centre_distance)
    if (centre_distance > r2 - r1):
        print("C2 is in C1")
    elif (centre_distance > r1 - r2):
        print("C1 is in C2")
    elif (centre_distance > r1 + r2):
        print("C1 and C2 intersect")
    else:
        print("No Overlap")

touching_circles([5, 6], 4, [8, 7], 9)
