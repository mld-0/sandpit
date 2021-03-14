def remove_nums(values):
    while (len(values) > 0):
        print(values)
        if (len(values) < 3): 
            print(f"delete {values[-1]}")
            del values[-1]
        else:
            to_remove = []
            for i in range(len(values)):
                if ((i+1) % 3 == 0):
                    to_remove.append(i)
            #print(to_remove)
            for n in reversed(to_remove):
                print(f"delete {values[n]}")
                del values[n]
    
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)
