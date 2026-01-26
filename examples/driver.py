import numpy as np
import matplotlib.pyplot as plt
import os
from goph547lab00 import arrays

# --- Part 1: Basic Array Operations ---
print("1. Array of ones (3x5):")
print(np.ones((3, 5)))

print("\n3. Column vector of odd numbers (45-73):")
odd_vector = np.arange(45, 75, 2).reshape(-1, 1)
print(odd_vector)

print(f"\n4. Sum of the odd vector: {np.sum(odd_vector)}")

# --- Part 2: Image Processing ---
img_path = 'examples/rock_canyon.jpg'

if os.path.exists(img_path):
    # Use the function from your package
    img, gray_img = arrays.load_images(img_path)
    print(f"\nImage loaded. Color shape: {img.shape}")
    
    # Generate Plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Horizontal Profile (X-axis)
    x = range(img.shape[1])
    ax1.plot(x, img[:,:,0].mean(axis=0), color='red', label='Red')
    ax1.plot(x, img[:,:,1].mean(axis=0), color='green', label='Green')
    ax1.plot(x, img[:,:,2].mean(axis=0), color='blue', label='Blue')
    ax1.plot(x, img.mean(axis=(0,2)), color='black', linewidth=2, label='Total Mean')
    ax1.set_title("Horizontal Profile")
    ax1.legend()

    # Vertical Profile (Y-axis)
    y = range(img.shape[0])
    ax2.plot(img.mean(axis=(1,2)), y, color='black', linewidth=2)
    ax2.set_title("Vertical Profile")
    ax2.invert_yaxis()

    plt.tight_layout()
    plt.savefig('examples/rock_canyon_summary.png')
    print("Plot saved as 'rock_canyon_summary.png'")
    plt.show()
else:
    print(f"Error: File {img_path} not found.")