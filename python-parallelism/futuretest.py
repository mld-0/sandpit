from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import time
from http.client import HTTPSConnection

#   LINK: https://stackoverflow.com/questions/9786102/how-do-i-parallelize-a-simple-python-loop

def processor_intensive(arg):
    def fib(n): # recursive, processor intensive calculation (avoid n > 36)
        return fib(n-1) + fib(n-2) if n > 1 else n
    start = time()
    result = fib(arg)
    return time() - start, result

def io_bound(arg):
    start = time()
    con = HTTPSConnection(arg)
    con.request('GET', '/')
    result = con.getresponse().getcode()
    return time() - start, result

def manager(PoolExecutor, calc_stuff):
    if calc_stuff is io_bound:
        inputs = ('python.org', 'stackoverflow.com', 'stackexchange.com',
                  'noaa.gov', 'parler.com', 'aaronhall.dev')
    else:
        inputs = range(25, 32)
    timings, results = list(), list()
    start = time()
    with PoolExecutor() as executor:
        for timing, result in executor.map(calc_stuff, inputs):
            # put results into correct output list:
            timings.append(timing), results.append(result)
    finish = time()
    print(f'{calc_stuff.__name__}, {PoolExecutor.__name__}')
    print(f'wall time to execute: {finish-start}')
    print(f'total of timings for each call: {sum(timings)}')
    print(f'time saved by parallelizing: {sum(timings) - (finish-start)}')
    print(dict(zip(inputs, results)), end = '\n\n')

def main():
    for computation in (processor_intensive, io_bound):
        for pool_executor in (ProcessPoolExecutor, ThreadPoolExecutor):
            manager(pool_executor, calc_stuff=computation)

if __name__ == '__main__':
    main()
