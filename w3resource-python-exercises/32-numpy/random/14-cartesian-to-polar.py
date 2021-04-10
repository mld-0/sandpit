import numpy as np

coords = np.random.random((10,2))
coords_x, coords_y = coords[:, 0], coords[:, 1]
print(coords_x)
print(coords_y)

coords_r = np.sqrt(coords_x**2 + coords_y**2)
coords_t = np.arctan2(coords_y, coords_x)
print(coords_r)
print(coords_t)

