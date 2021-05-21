import multiprocessing

def chunks(l, n):
    """Yield n number of sequential chunks from l."""
    d, r = divmod(len(l), n)
    for i in range(n):
        si = (d+1)*(i if i < r else r) + d*(0 if i < r else i - r)
        yield l[si:si+(d+1 if i < r else d)]

def worker(procnum, return_dict, squares_sublist):
    result_squares_sublist = []
    for loop_val in squares_sublist:
        result_squares_sublist.append(loop_val ** 2)
    return_dict[procnum] = result_squares_sublist


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    threads_num = 8

    num_vals = 50
    x_vals = [ x for x in range(num_vals) ]
    y_vals = []

    x_sublists = list(chunks(x_vals, threads_num))
    print(x_sublists)

    for i, loop_sublist in enumerate(x_sublists):
        p = multiprocessing.Process(target=worker, args=(i, return_dict, loop_sublist))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()

    for i in range(threads_num):
        y_vals += return_dict[i]

    print(y_vals)

