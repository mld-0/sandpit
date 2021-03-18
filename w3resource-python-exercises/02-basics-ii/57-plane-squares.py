#   Rudimentary blob-extraction algorithm

#   Print array character by character, as a grid
def print_island_array(island_array):
    for i in range(0, len(islands_array)):
        for j in range(0, len(islands_array[0])):
            print(islands_array[i][j], end='')
        print()

#   Convert string to list of lists (of characters)
def read_islands_array(islands_str):
    results_list = []
    for loop_line in islands_str.splitlines():
        loop_line_array = [x for x in loop_line]
        results_list.append(loop_line_array)
    return results_list

#   Once a region is identified, set to value all 4-connected regions which are also 'a'
def remove_4connected(island_array, i, j, value):
    if (0 <= i < len(island_array)) and (0 <= j < len(island_array[0])) and (island_array[i][j] == 'a'):
        island_array[i][j] = str(value)
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            remove_4connected(islands_array, i + di, j + dj, value)

#   Get number of 4-connected regions, and label each region with region number
def island_count(island_array):
    island_count = 0
    for i in range(0, len(islands_array)):
        for j in range(0, len(islands_array[0])):
            if (islands_array[i][j] == 'a'):
                remove_4connected(island_array, i, j, island_count + 1)
                island_count += 1
    return island_count

islands_str = """aa00000aaa
a000000aaa
0000000aaa
00a000a000
00000aaa00
0000aaaaa0
000aaaaaaa
a000aaaaa0
aa000aaa00
aaa000a000"""

islands_array = read_islands_array(islands_str)
count = island_count(islands_array)
print_island_array(islands_array)
print(count)

