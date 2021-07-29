from PIL import Image
import numpy as np

def draw_image(i, name):
    img = Image.fromarray(np.array(i, dtype=np.uint8), mode='L')
    img.save(name + ".png")