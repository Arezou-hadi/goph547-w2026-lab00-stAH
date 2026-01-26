import numpy as np
from PIL import Image

def square_ones(n):
    """Creates a square array of ones of size n x n."""
    return np.ones((n, n))

def load_images(path):
    """Loads a color image and its grayscale version."""
    # Load color image
    img = np.asarray(Image.open(path))
    # Load grayscale version
    gray_img = np.asarray(Image.open(path).convert("L"))
    return img, gray_img

def crop_pinnacle(gray_img):
    """Crops the grayscale image to isolate the rock pillar."""
    # Adjust these indices based on your specific image dimensions
    small_gray_image = gray_img[300:700, 100:400]
    return small_gray_image