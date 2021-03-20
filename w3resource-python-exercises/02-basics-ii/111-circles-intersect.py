import math

def circles_intersect(c1, c2):
    """Determine whether two given circles (x,y,radius) intersect"""
    centre_distance = math.hypot(c1[0] - c2[0], c1[1] - c2[1])
    radius_sum = c1[2] + c2[2]
    print(centre_distance < radius_sum)

circles_intersect([1,2, 4], [1,2, 8])
circles_intersect([0,0, 2], [10,10, 5])
