import os
import cv2
import random
from tqdm import tqdm
from utils.segmentation import segment_product
from utils.blending import blend_product_with_background

def process_batch(product_images, background_images, output_dir):
    """
    Processes multiple product images and integrates them into backgrounds.
    """
    os.makedirs(output_dir, exist_ok=True)  # Ensure output folder exists

    # Ensure backgrounds exist
    if not background_images:
        print("❌ No background images found! Please check 'inputs/backgrounds' directory.")
        return  

    for product_path in tqdm(product_images, desc="Processing products"):
        try:
            product = segment_product(product_path)

            # Check if segmentation failed
            if product is None:
                print(f"❌ Segmentation failed for {product_path}, skipping...")
                continue  # Skip this image

            # Select a random background
            bg_path = random.choice(background_images)
            background = cv2.imread(bg_path)

            # Check if background was loaded correctly
            if background is None:
                print(f"❌ Error loading background: {bg_path}, skipping...")
                continue

            # Ensure product is not larger than background
            ph, pw, _ = product.shape
            bh, bw, _ = background.shape
            if ph > bh or pw > bw:
                scale_factor = min(bh / ph, bw / pw) * 0.8  # Resize to fit
                new_w, new_h = int(pw * scale_factor), int(ph * scale_factor)
                product = cv2.resize(product, (new_w, new_h), interpolation=cv2.INTER_AREA)

            # Blend product with background
            output_image = blend_product_with_background(product, background)

            # Define output filename with correct format
            output_filename = os.path.join(output_dir, f"{os.path.basename(product_path).split('.')[0]}_{os.path.basename(bg_path)}.jpg")

            # Save the output image
            cv2.imwrite(output_filename, output_image)

        except Exception as e:
            print(f"❌ Error processing {product_path}: {str(e)}. Skipping...")

    print("✅ Batch processing completed successfully!")
