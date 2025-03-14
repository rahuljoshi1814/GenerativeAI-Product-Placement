import cv2
import numpy as np

def blend_product_with_background(product, background):
    """Places product onto a random background with transparency and blending adjustments."""
    
    # Ensure product image has an alpha channel
    if product.shape[2] == 3:
        product = cv2.cvtColor(product, cv2.COLOR_BGR2BGRA)

    # Resize product to fit naturally within the background
    h1, w1, _ = product.shape
    h2, w2, _ = background.shape

    scale_factor = np.random.uniform(0.3, 0.5)  # Adjust product size dynamically
    new_w = int(w2 * scale_factor)
    new_h = int(h2 * scale_factor)
    product = cv2.resize(product, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Ensure there is a proper alpha channel (Remove black background if needed)
    if product.shape[2] == 4:
        alpha_channel = product[:, :, 3]
        product[np.all(product[:, :, :3] == 0, axis=2)] = [0, 0, 0, 0]

    # Get a safe random position for placement
    x_offset = np.random.randint(10, w2 - new_w - 10)  # Avoid touching the edges
    y_offset = np.random.randint(10, h2 - new_h - 10)

    # Extract the alpha channel and create a shadow effect
    alpha_channel = product[:, :, 3] / 255.0  # Normalize alpha (0 to 1)
    shadow = cv2.GaussianBlur(alpha_channel * 255, (5, 5), 3)  # Soft shadow
    shadow = np.expand_dims(shadow, axis=-1)  # Convert to single channel

    # Apply shadow under product
    background_section = background[y_offset:y_offset + new_h, x_offset:x_offset + new_w]
    background_section = background_section.astype(np.float32)
    shadow_intensity = 0.4  # Adjust shadow strength
    background_section = background_section * (1 - (shadow / 255) * shadow_intensity)

    # Extract the ROI (Region of Interest) from the background
    roi = background[y_offset:y_offset + new_h, x_offset:x_offset + new_w]

    # Convert alpha mask to 3-channel for blending
    alpha_mask = np.stack([alpha_channel] * 3, axis=-1)

    # Blend product into background
    blended = (roi * (1 - alpha_mask) + product[:, :, :3] * alpha_mask).astype(np.uint8)

    # Place the blended product onto the background
    background[y_offset:y_offset + new_h, x_offset:x_offset + new_w] = blended

    return background

