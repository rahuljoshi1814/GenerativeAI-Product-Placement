import os
import glob

def get_all_product_images(base_dir):
    """
    Recursively fetch all image files from the given base directory, 
    including images inside subfolders.
    """
    image_extensions = ["*.jpg", "*.png", "*.jpeg"]
    all_images = []

    # Iterate over all subdirectories and fetch images
    for ext in image_extensions:
        all_images.extend(glob.glob(os.path.join(base_dir, "**", ext), recursive=True))

    print(f"✅ Found {len(all_images)} images in {base_dir}")
    return all_images
