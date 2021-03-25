
def dict_remove_duplicates(d):
    result = dict()
    for k, v in d.items():
        if v not in result.values():
            result.update({k: v})
            #   or
            result[k] = v
    print(result)

student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science'] },
 'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science'] },
 'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science'] },
 'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science'] },
}
dict_remove_duplicates(student_data)
