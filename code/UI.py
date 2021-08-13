from PIL import Image
import numpy as np

def draw_image(i):
    img = Image.fromarray(np.array(i, dtype=np.uint8), mode='L')
    return img

""" def draw_weight_image(i):
    img = Image.fromarray(np.array(i, dtype=np.uint8), mode='L') """