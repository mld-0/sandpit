import time

def exe_time():
    starttime = time.time()
    for i in range(1000000):
        a = i + i
    endtime = time.time()
    elapsed = endtime - starttime
    print(elapsed)

exe_time()

