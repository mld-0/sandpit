import numpy as np
from PIL import Image

values = np.full((512, 256, 3), 255, dtype=np.uint8)
img = Image.fromarray(values, "RGB")

#img.show()
#img.save("white.png", "PNG")

