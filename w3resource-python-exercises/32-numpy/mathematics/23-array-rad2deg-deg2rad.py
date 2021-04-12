import numpy as np

values = np.array([-np.pi, -np.pi/2, np.pi/2, np.pi])
print(values)

result_deg = np.rad2deg(values)
#   or
result_deg = np.degrees(values)
print(result_deg)

result_rad = np.deg2rad(result_deg)
#   or
result_rad = np.radians(result_deg)
print(result_rad)

