#   In a matrix if the value of an element is the maximum in its column and minimum in its row then the number is called lucky number.

def lucky_numbers(values):
    result = set()
    for i in range(len(values)):
        for j in range(len(values[0])):
            #   Are we still a magic number if there is another element equal to max/min value?
            loop_value = values[i][j]
            loop_row = values[i][:]
            loop_column = [x[j] for x in values[:]]
            if (loop_value == min(loop_row) and loop_value == max(loop_column)):
                #   is there a second occurence of loop_value in loop_column or loop_row?
                result.add(loop_value)
    print(result)

#   or

def lucky_Numbers(matrix):
    result = set(map(min, matrix)) & set(map(max, zip(*matrix)))
    print(list(result))


lucky_numbers([[1, 2], [2, 3]])
lucky_numbers([[1, 2, 3], [3, 4, 5]])
lucky_numbers([[7, 5, 6], [3, 4, 4], [6, 5, 7]])

lucky_Numbers([[1, 2], [2, 3]])
lucky_Numbers([[1, 2, 3], [3, 4, 5]])
lucky_Numbers([[7, 5, 6], [3, 4, 4], [6, 5, 7]])


