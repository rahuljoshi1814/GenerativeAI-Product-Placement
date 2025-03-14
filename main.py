import os
from utils.get_all_images import get_all_product_images
from utils.batch_processing import process_batch

# Define directories
PRODUCTS_DIR = "inputs/products"  # Root folder where all product folders exist
BACKGROUND_DIR = "inputs/backgrounds"  # Background images
OUTPUT_DIR = "outputs"  # Where final images will be saved

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("🔄 Collecting product images from all subdirectories...")
    product_images = get_all_product_images(PRODUCTS_DIR)
    
    if not product_images:
        print("❌ No product images found! Check 'inputs/products' directory.")
        return  

    print(f"✅ Found {len(product_images)} product images from all subfolders.")

    print("🔄 Collecting background images...")
    background_images = get_all_product_images(BACKGROUND_DIR)
    
    if not background_images:
        print("❌ No background images found! Check 'inputs/backgrounds' directory.")
        return  

    print(f"✅ Found {len(background_images)} background images.")

    print("🚀 Starting batch processing...")
    process_batch(product_images, background_images, OUTPUT_DIR)

    print("✅ Batch processing completed! Results saved in 'outputs/'.")

if __name__ == "__main__":
    main()
