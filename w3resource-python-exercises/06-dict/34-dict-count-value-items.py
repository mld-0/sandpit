
def dict_count_value_items(d):
    result_lens = [{k: len(v)} for k, v in d.items()]
    result_lens_sum = sum([a for x in result_lens for a in x.values()])
    #print(result_lens)
    print(result_lens_sum)

d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
dict_count_value_items(d)
