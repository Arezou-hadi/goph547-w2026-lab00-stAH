import numpy as np
import matplotlib.pyplot as plt
#from PIL import image

#from goph547lab00.arrays import (square_ones,)

# 1. Create an array of ones with 3 rows and 5 columns
ones_array = np.ones((3, 5))
print("1. Array of ones (3x5):")
print(ones_array)
print("-" * 30)

# 2. Produce an array of NaN with 6 rows and 3 columns
nan_array = np.full((6, 3), np.nan)
print("2. Array of NaNs (6x3):")
print(nan_array)
print("-" * 30)

# 3. Create a column vector of odd numbers between 44 and 75
# arange(start, stop, step); .reshape(-1, 1) converts the flat array into a column
odd_vector = np.arange(45, 75, 2).reshape(-1, 1)
print("3. Column vector of odd numbers (44-75):")
print(odd_vector)
print("-" * 30)

# 4. Find the sum of the vector produced in #3
vector_sum = np.sum(odd_vector)
print(f"4. Sum of the odd vector: {vector_sum}")
print("-" * 30)

# 5. Produce the array: A = [[5, 7, 2], [1, -2, 3], [4, 4, 4]]
A = np.array([[5, 7, 2], [1, -2, 3], [4, 4, 4]])
print("5. Array A:")
print(A)
print("-" * 30)

# 6. Using a single command, produce the identity array B (3x3)
B = np.eye(3)
print("6. Array B (Identity Matrix):")
print(B)
# 7. Perform element-wise multiplication of the arrays A and B
# This multiplies each element of A by the corresponding element in B.
element_wise = A * B
print("7. Element-wise multiplication (A * B):")
print(element_wise)
print("-" * 30)

# 8. Calculate the dot product (matrix-multiplication) of arrays A and B
# Using the @ operator or np.dot(). Since B is the Identity matrix, the result is A.
dot_product = A @ B
print("8. Dot product / Matrix multiplication (A @ B):")
print(dot_product)
print("-" * 30)

# 9. Calculate the cross product of arrays A and B
# This calculates the cross product for each corresponding row of the matrices.
cross_product = np.cross(A, B)
print("9. Cross product of A and B:")
print(cross_product)
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 10. Load the image
img = np.asarray(Image.open('rock_canyon.jpg'))

# 11. Plot and check shape
plt.imshow(img)
plt.show()
print(f"Original shape: {img.shape}") # Expected: (H, W, 3)

# 12. Re-open as grayscale
gray_img = np.asarray(Image.open('rock_canyon.jpg').convert("L"))
print(f"Grayscale shape: {gray_img.shape}") # Expected: (H, W)

#mkdir src
#mkdir src/goph547lab00
#mkdir examples
import os
from goph547lab00 import arrays

# تنظیم مسیر دقیق تصویر 
img_path = 'examples/rock_canyon.jpg'

# بررسی وجود فایل برای جلوگیری از خطای FileNotFoundError
if os.path.exists(img_path):
    img, gray_img = arrays.process_image(img_path)
    print("Image loaded successfully!")
    print(f"11. Color image shape: {img.shape}") 
else:
    print(f"Error: File not found at {img_path}. Please check the directory.")

    import numpy as np
from PIL import Image

def load_images(path):
    # ۱۰. بارگذاری تصویر اصلی به صورت آرایه 
    img = np.asarray(Image.open(path))
    
    # ۱۲. بارگذاری مجدد و تبدیل به خاکستری (Grayscale) [cite: 80-81]
    gray_img = np.asarray(Image.open(path).convert("L"))
    
    return img, gray_img

def crop_pinnacle(gray_img):
    # ۱۳. برش تصویر برای جدا کردن ستون سنگی (Pillar) 
    # این اعداد را بر اساس ابعاد تصویر خود تنظیم کنید (مثلاً ردیف 300 تا 700)
    small_gray_image = gray_img[300:700, 100:400]
    return small_gray_image
import numpy as np
from PIL import Image

def load_images(path):
    # ۱۰. بارگذاری تصویر اصلی به صورت آرایه 
    img = np.asarray(Image.open(path))
    
    # ۱۲. بارگذاری مجدد و تبدیل به خاکستری (Grayscale) 
    gray_img = np.asarray(Image.open(path).convert("L"))
    
    return img, gray_img

def crop_pinnacle(gray_img):
    # ۱۳. برش تصویر برای جدا کردن ستون سنگی (Pillar) 
    # این اعداد را بر اساس ابعاد تصویر خود تنظیم کنید (مثلاً ردیف 300 تا 700)
    small_gray_image = gray_img[300:700, 100:400]
    return small_gray_image
import matplotlib.pyplot as plt
from goph547lab00 import arrays

# مسیر تصویر
img_path = 'examples/rock_canyon.jpg'

# ۱۰ تا ۱۲. دریافت آرایه‌ها و چاپ ابعاد (Shape) 
img, gray_img = arrays.load_images(img_path)
print(f"Shape of color image: {img.shape}") 
print(f"Shape of grayscale image: {gray_img.shape}")

# ۱۴ و ۱۵. ایجاد زیرنمودارها (Subplots) [cite: 83-92]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# نمودار اول: میانگین در راستای محور Y (پروفیل افقی) 
x = range(img.shape[1])
ax1.plot(x, img[:,:,0].mean(axis=0), color='red', label='Red Mean')
ax1.plot(x, img[:,:,1].mean(axis=0), color='green', label='Green Mean')
ax1.plot(x, img[:,:,2].mean(axis=0), color='blue', label='Blue Mean')
ax1.plot(x, img.mean(axis=(0,2)), color='black', linewidth=3, label='Total RGB Mean')
ax1.set_title("Horizontal Profile (Mean along Y)")
ax1.set_xlabel("X-coordinate")
ax1.set_ylabel("Color Intensity")
ax1.legend()

# نمودار دوم: میانگین در راستای محور X (پروفیل عمودی) 
y = range(img.shape[0])
ax2.plot(img[:,:,0].mean(axis=1), y, color='red')
ax2.plot(img[:,:,1].mean(axis=1), y, color='green')
ax2.plot(img[:,:,2].mean(axis=1), y, color='blue')
ax2.plot(img.mean(axis=(1,2)), y, color='black', linewidth=3)
ax2.set_title("Vertical Profile (Mean along X)")
ax2.set_xlabel("Color Intensity")
ax2.set_ylabel("Y-coordinate")
ax2.invert_yaxis() # معکوس کردن برای تطبیق با نمایش تصویر

# ۱۶. ذخیره نمودار نهایی 
plt.tight_layout()
plt.savefig('examples/rock_canyon_RGB_summary.png')
plt.show()
