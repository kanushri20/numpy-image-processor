# NumPy Image Processor

A beginner-friendly image processing project built using NumPy and Pillow.

This project demonstrates how images can be represented as multidimensional arrays and manipulated using NumPy operations.

---

## Features

- Negative Filter
- Grayscale Conversion
- Brightness Adjustment
- Horizontal Flip
- Blur Filter
- Sharpen Filter

---

## Technologies Used

- Python
- NumPy
- Pillow (PIL)

---

## Project Structure

```txt
numpy-image-processor/
│
├── images/
│   └── sample.jpg
│
├── output/
│
├── main.py
├── README.md
```

---

## How It Works

Images are converted into NumPy arrays where each pixel contains RGB values.

Example pixel:

```python
[120, 45, 200]
```

This represents:

```txt
Red   = 120
Green = 45
Blue  = 200
```

The project applies mathematical operations directly on these arrays to generate image effects.

---

## Implemented Filters

### 1. Negative Filter

Creates a photographic negative effect by inverting pixel values.

Core logic:

```python
255 - arr
```

---

### 2. Grayscale Conversion

Converts RGB images into grayscale using channel averaging.

Core logic:

```python
np.mean(arr, axis=2)
```

---

### 3. Brightness Adjustment

Increases or decreases image brightness.

Core logic:

```python
arr + value
```

---

### 4. Horizontal Flip

Flips the image horizontally using NumPy slicing.

Core logic:

```python
arr[:, ::-1]
```

---

### 5. Blur Filter

Applies a blur effect by averaging neighboring pixels.

Concepts used:
- kernels
- neighboring pixel operations
- local averaging

---

### 6. Sharpen Filter

Enhances image details using convolution kernels.

Example sharpening kernel:

```python
[
 [ 0, -1,  0],
 [-1,  5, -1],
 [ 0, -1,  0]
]
```

---

## Installation

Clone the repository:

```bash
git clone <your-repository-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

---

## Requirements

```txt
numpy
pillow
```

---

## Learning Outcomes

This project helped in understanding:

- NumPy arrays
- RGB image representation
- image manipulation
- array slicing
- kernels and convolution
- pixel-wise operations
- basic image processing concepts

---

## Future Improvements

- Edge Detection
- Rotation
- Image Resizing
- Contrast Adjustment
- GUI Version
- Real-time Webcam Filters

---

## License

This project is open-source and free to use for educational purposes.
