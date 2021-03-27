import re

extract_and_sort_nums = lambda x: sorted([int(n) for n in re.findall('\d+', x) if int(n) > len(re.findall('\d+', x))])

print(extract_and_sort_nums('sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5'))


