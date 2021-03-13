num_list = [45, 55, 60, 37, 100, 105, 220]
print(num_list)
#   anonymous function, or lambda
is_div_15 = lambda x: x % 15 == 0 
div_list = [ x for x in num_list if is_div_15(x) ]
print(div_list)
