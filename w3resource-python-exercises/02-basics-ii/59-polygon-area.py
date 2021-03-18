
def polygon_area(verticies):
    result = 0
    for i in range(0, len(verticies)):
        j = i + 1 if i + 1 < len(verticies) else 0
        #print("%i, %i" % (i, j))
        #print("%s, %s, %s, %s" % (verticies[i][0] , verticies[j][1] , verticies[i][1] , verticies[j][0]))
        result += verticies[i][0] * verticies[j][1] - verticies[i][1] * verticies[j][0]
    result = abs(result / 2)
    print(result)



verticies = [[1,0], [0,0], [1,1], [2,0], [-1,1]]
polygon_area(verticies)
