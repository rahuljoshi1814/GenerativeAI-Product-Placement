import torch
import numpy as np
import cv2
from segment_anything import SamPredictor, sam_model_registry

# Load SAM model
MODEL_PATH = "models/sam_vit_h_4b8939.pth"
sam = sam_model_registry["vit_h"](checkpoint=MODEL_PATH)
sam.to("cuda" if torch.cuda.is_available() else "cpu")  # Move model to GPU if available
predictor = SamPredictor(sam)

def segment_product(image_path):
    """Segments the product from its background using SAM with improved accuracy."""
    
    # Read image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        print(f"❌ Error: Unable to load image {image_path}")
        return None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Set the image for SAM predictor
    predictor.set_image(image_rgb)

    # **Fix: Use multiple auto-selected points for better segmentation**
    height, width, _ = image.shape
    input_points = np.array([
        [width // 4, height // 4],  # Top-left
        [width // 2, height // 2],  # Center
        [3 * width // 4, 3 * height // 4]  # Bottom-right
    ])
    input_labels = np.array([1, 1, 1])  # 1 means foreground

    # Get segmentation mask
    masks, _, _ = predictor.predict(point_coords=input_points, point_labels=input_labels)

    if masks is None or len(masks) == 0:
        print(f"❌ No segmentation found for {image_path}")
        return None

    # **Fix: Choose the most confident mask**
    largest_mask_idx = np.argmax([np.sum(mask) for mask in masks])  # Find the biggest mask
    mask = masks[largest_mask_idx].astype(np.uint8) * 255

    # Apply mask to the image
    segmented_image = cv2.bitwise_and(image, image, mask=mask)

    # Convert black background to transparent
    segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2BGRA)

    # **Fix: Set transparent pixels correctly**
    alpha_channel = np.where(mask > 0, 255, 0).astype(np.uint8)
    segmented_image[:, :, 3] = alpha_channel  # Replace alpha channel

    return segmented_image

