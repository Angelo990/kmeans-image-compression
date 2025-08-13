# K-means Image Compression

This is a simple school project demonstrating image compression using k-means clustering.

This project demonstrates image compression using the k-means clustering algorithm in Python.

## How It Works

1. **Load Image**: The script loads an image from a specified path and converts it to RGB format.
2. **Reshape Data**: The image is reshaped into a 2D array where each row represents a pixel's RGB values.
3. **K-means Clustering**: The k-means algorithm groups pixels into `k` clusters (colors). Each pixel is assigned to the nearest cluster centroid.
4. **Reconstruct Image**: Each pixel's color is replaced with its cluster centroid, reducing the number of unique colors and compressing the image.
5. **Save and Display**: The compressed image is saved and both the original and compressed images are displayed side by side.

## Usage

1. Place your image in a known location and update the `image_path` variable in `main.py` to point to it.
2. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
3. Run the script:
   ```powershell
   python main.py
   ```
4. The compressed image will be saved as `images/compressed.jpg`.

## Parameters
- `k`: Number of clusters/colors. Lower values mean higher compression but less color detail.
- `image_path`: Path to your input image.

## Requirements
* Python 3.x: The programming language used for the project.
* numpy: For efficient numerical operations and array manipulations.
* scikit-learn: Provides the k-means clustering algorithm used for compression.
* matplotlib: Used to display and visualize the original and compressed images.
* Pillow: For loading, converting, and saving image files.

## Example
```
python main.py
```

## File Structure
- `main.py`: Main script for image compression.
- `requirements.txt`: Python dependencies.
- `images/`: Folder for input and output images.

## Author
Angelo J. Papas

---
