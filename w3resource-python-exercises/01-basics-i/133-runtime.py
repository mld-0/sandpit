import time

def calc_squares(n):
    for x in range(n):
        y = x ** 2

starttime = time.time()
calc_squares(1000)
endtime = time.time()

elapsed = endtime - starttime 
print(elapsed)
