import math
import heapq

def show_tree(tree, total_width=60, fill=' '):
    output = ""
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))  # which row of tree contains i-th element
        else:
            row = 0
        if row != last_row:
            output += '\n'

        columns = 2**row 
        col_width = int(math.floor((total_width*1.0)/columns))

        output += str(n).center(col_width, fill)
        last_row = row

    print(output)
    print('-' * total_width)

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
heapq.heappush(heap, 7)
heapq.heappush(heap, 9)
heapq.heappush(heap, 10)
heapq.heappush(heap, 8)
heapq.heappush(heap, 16)
heapq.heappush(heap, 14)
show_tree(heap)
