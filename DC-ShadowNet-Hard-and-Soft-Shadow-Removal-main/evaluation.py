import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as ssim

def calculate_psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return float('inf')  # No difference between images
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def calculate_ssim(img1, img2):
    return ssim(img1, img2, channel_axis=-1)

input_dir = './input'  # Change to your input directory
output_dir = './output'  # Change to your output directory

# Get list of images in both directories
input_images = sorted(os.listdir(input_dir))
output_images = sorted(os.listdir(output_dir))

# Ensure both directories have the same number of images
if len(input_images) != len(output_images):
    print("The number of images in input and output directories do not match.")
else:
    total_psnr = 0
    total_ssim = 0
    count = 0

    for input_image, output_image in zip(input_images, output_images):
        input_path = os.path.join(input_dir, input_image)
        output_path = os.path.join(output_dir, output_image)

        # Read images
        img1 = cv2.imread(input_path)
        img2 = cv2.imread(output_path)

        # Check if images are loaded properly
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

        # Calculate PSNR and SSIM
        psnr_value = calculate_psnr(img1, img2)
        ssim_value = calculate_ssim(img1, img2)

        # Accumulate PSNR and SSIM values
        total_psnr += psnr_value
        total_ssim += ssim_value
        count += 1

        print(f"Image: {input_image} - PSNR: {psnr_value:.2f}, SSIM: {ssim_value:.4f}")

    if count > 0:
        average_psnr = total_psnr / count
        average_ssim = total_ssim / count
        print(f"\n PSNR: {average_psnr:.6f}")
        print(f" SSIM: {average_ssim:.6f}")