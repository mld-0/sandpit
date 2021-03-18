import statistics

def list_median(values):
    values_sorted = sorted(values)
    median = statistics.median(values_sorted)
    print(median)

list_median([1,2,3,4,5])
list_median([1,2,3,4,5,6])
list_median([6,1,2,4,5,3])
list_median([1.0,2.11,3.3,4.2,5.22,6.55])
list_median([1.0,2.11,3.3,4.2,5.22])
list_median([2.0,12.11,22.3,24.12,55.22])
