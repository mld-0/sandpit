import numpy as np

rng = np.random.default_rng()

values = np.arange(10)

#   With replacement
values_choice = rng.choice(values, 5)
print(values_choice)

#   Without replacement
values_choice = rng.choice(values, 5, replace=False)
print(values_choice)

