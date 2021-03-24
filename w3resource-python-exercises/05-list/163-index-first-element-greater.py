
def index_first_element_greater(values, n):
    for i, x in enumerate(values):
        if x > n:
            print(i)
            return


values = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]

index_first_element_greater(values, 73)
index_first_element_greater(values, 21)
index_first_element_greater(values, 80)
index_first_element_greater(values, 55)

