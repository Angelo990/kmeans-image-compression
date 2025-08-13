# main.py
# Image Compression using K-Means Clustering

from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load image
def load_image(path):
    img = Image.open(path)
    img = img.convert('RGB')
    return np.array(img)

# Main function
def main():
    # TODO: Add image path
    image_path = r'C:\Users\Angelo J. Papas\Pictures\Screenshots\Screenshot 2025-06-27 013146.png'  # Change to your image file
    img = load_image(image_path)
    print('Image loaded:', img.shape)

    # Reshape image to (num_pixels, 3)
    w, h = img.shape[0], img.shape[1]
    img_reshaped = img.reshape(-1, 3)

    # Set number of clusters/colors
    k = 3

    # Run k-means
    print(f'Running k-means with k={k}...')
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(img_reshaped)
    labels = kmeans.predict(img_reshaped)
    compressed_img = kmeans.cluster_centers_[labels].astype(np.uint8)
    compressed_img = compressed_img.reshape(w, h, 3)

    # Save and show compressed image
    compressed = Image.fromarray(compressed_img)
    compressed.save('images/compressed.jpg')
    print('Compressed image saved as images/compressed.jpg')
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.title('Original')
    plt.imshow(img)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.title(f'Compressed (k={k})')
    plt.imshow(compressed_img)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
