import numpy as np
from PIL import Image

def square_ones(n):
    """Creates a square array of ones of size n x n."""
    return np.ones((n, n))

def load_images(path):
    """Loads a color image and its grayscale version."""
    img = np.asarray(Image.open(path))
    gray_img = np.asarray(Image.open(path).convert("L"))
    return img, gray_img