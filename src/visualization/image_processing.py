from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

# Load the image from the specified path, resize it to 48x48 pixels, and convert it to grayscale
img = image.load_img("/kaggle/input/fer2013/test/surprise/PublicTest_7431524.jpg", target_size=(48, 48), color_mode="grayscale")

# Convert the loaded image into a numpy array
img = np.array(img)

# Display the image using matplotlib
plt.imshow(img, cmap='gray')  
plt.axis('off')  
plt.show()

# Print the shape of the image array
print(f"Image shape: {img.shape}")
