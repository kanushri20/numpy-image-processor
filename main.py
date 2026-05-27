from PIL import Image
import numpy as np

def main():
    print("Hello there!")
    print("This project is NumPy Image Processor")
    print("""It can processor a sample image by:
    Negative Scaling
    Gray scaling
    Blurring
    Sharpening
    Flipping
    Adjusting Brightness
    """)
    imgProcessor()

def imgProcessor():
    img = Image.open("image/sample.jpg")
    img = img.resize((300, 300))
    arr = np.array(img)
    negative = 255 - arr
    gray = np.mean(arr, axis=2)
    gray_3d = np.stack((gray,) * 3, axis=-1)
    bright = arr + 50
    bright = np.clip(bright, 0, 255)
    flipped = arr[:, ::-1]
    blurred = np.zeros_like(arr)
    sharpened = np.zeros_like(arr)
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):

            neighborhood = arr[i - 1:i + 2, j - 1:j + 2]

            blurred[i, j] = np.mean(neighborhood, axis=(0, 1))
    for i in range(1, arr.shape[0] - 1):
        for j in range(1, arr.shape[1] - 1):

            for c in range(3):
                neighborhood = arr[i - 1:i + 2, j - 1:j + 2, c]

                value = np.sum(neighborhood * kernel)

                sharpened[i, j, c] = np.clip(value, 0, 255)


    new_img1 = Image.fromarray(negative.astype(np.uint8))
    new_img2 = Image.fromarray(gray_3d.astype(np.uint8))
    new_img3 = Image.fromarray(bright.astype(np.uint8))
    new_img4 = Image.fromarray(flipped.astype(np.uint8))
    new_img5 = Image.fromarray(blurred.astype(np.uint8))
    new_img6 = Image.fromarray(sharpened.astype(np.uint8))

    new_img1.save("output/negative.jpg")
    new_img2.save("output/grayscale.jpg")
    new_img3.save("output/bright.jpg")
    new_img4.save("output/flipped.jpg")
    new_img5.save("output/kernel.jpg")
    new_img6.save("output/sharp.jpg")

    print("All images saved successfully!")

main()