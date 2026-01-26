import numpy as np
from PIL import Image

def load_images(path):
    img = np.asarray(Image.open(path))
    gray_img = np.asarray(Image.open(path).convert("L"))
    return img, gray_img

def crop_pinnacle(gray_img):
    # These indices isolate the pillar (middle-left)
    # You may need to tweak these based on your specific image file
    return gray_img[250:850, 50:450]