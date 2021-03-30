import numpy as np

values = np.arange(0, 21)
print(values)

#   Set values between [9,15] negative
values[(values >= 9) & (values <= 15)] *= -1
print(values)

