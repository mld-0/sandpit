
def dict_contains_kv_pair(values, kv_pairs):
    result = any([(k, v) in kv_pairs for d in values for k,v in d.items()])
    print(result)

values = [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'}, {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}]

kv_pairs = [('student_id', 1)]
dict_contains_kv_pair(values, kv_pairs)

kv_pairs = [('name', 'Brian Howell')]
dict_contains_kv_pair(values, kv_pairs)

kv_pairs = [('class', 'VII')]
dict_contains_kv_pair(values, kv_pairs)

kv_pairs = [('class', 'I')]
dict_contains_kv_pair(values, kv_pairs)

kv_pairs = [('name', 'Brian Howelll')]
dict_contains_kv_pair(values, kv_pairs)

kv_pairs = [('student_id', 11)]
dict_contains_kv_pair(values, kv_pairs)

