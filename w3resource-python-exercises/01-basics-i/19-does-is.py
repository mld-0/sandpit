def DoesIs(arg_str):
    start_str = arg_str[0:2]
    start_str = start_str.lower()
    if (start_str == "is"):
        print(arg_str)
    else:
        print("Is" + arg_str)

strs_list = ["Array", "IsEmpty"]

for n in strs_list:
    DoesIs(n)
