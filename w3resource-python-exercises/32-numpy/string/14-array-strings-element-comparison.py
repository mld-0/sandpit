import numpy as np

a = np.array(['Hello', 'PHP', 'JS', 'examples', 'html'])
b = np.array(['Hello', 'php', 'Java', 'examples', 'html'])
print(a)
print(b)

test_eq = np.char.equal(a, b)
test_neq = np.char.not_equal(a, b)
test_lesseq = np.char.less_equal(a, b)
test_gteq = np.char.greater_equal(a, b)
test_gt = np.char.greater(a, b)
test_less = np.char.less(a, b)

print("eq: ", test_eq)
print("neq: ", test_neq)
print("lesseq: ", test_lesseq)
print("gteq: ", test_gteq)
print("gt: ", test_gt)
print("less: ", test_less)

