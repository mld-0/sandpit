
def unicode_list_to_str_list(values):
    results = [str(x) for x in values]
    print(results)

values = [u'S001', u'S002', u'S003', u'S004']
unicode_list_to_str_list(values)

