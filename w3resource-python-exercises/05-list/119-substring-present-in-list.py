
def substring_present_in_list(values, substr):
    result = any([substr in x for x in values])
    print(result)

values = ['red', 'black', 'white', 'green', 'orange']
substr = 'ack'
substring_present_in_list(values, substr)

substr='abc'
substring_present_in_list(values, substr) 
