
def list_rotations(values):
    results = []
    for i in range(len(values)):
        l = values[i:] + values[:i]
        results.append(l)
    return results

def circularly_identical_bruteforce(a, b):
    b_rotations = list_rotations(b)
    for loop_b in b_rotations:
        if a == loop_b:
            print(True)
            return
    print(False)

def circularly_identical(a, b):
    aa = a + a
    for i in range(0, len(aa)-len(b)+1):
        loop_a = aa[i:i+len(b)]
        if loop_a == b:
            print(True)
            return
    print(False)

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

circularly_identical(list1, list2)
circularly_identical(list1, list3)

