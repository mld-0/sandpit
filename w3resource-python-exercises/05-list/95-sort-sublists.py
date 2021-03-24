
def sort_sublists(values):
    result = list(map(sorted, values))
    print(result)

values = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
sort_sublists(values)
