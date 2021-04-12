import numpy as np

values_deg = np.array((0., 30., 45., 60., 90.))
values_rad = values_deg * 2 * np.pi / 360
print(values_deg)
print(values_rad)

result_sin = np.sin(values_rad)
print(result_sin)

result_cos = np.cos(values_rad)
print(result_cos)

result_tan = np.tan(values_rad)
print(result_tan)

