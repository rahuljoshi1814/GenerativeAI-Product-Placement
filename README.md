# Generative AI Product Placement Tool
### A Generative AI tool that places e-commerce product images into realistic backgrounds using SAM and OpenCV.

This AI-powered tool takes standalone  product images and seamlessly places them into ifestyle backgrounds, making them look like they naturally belong in the scene.

## Features
**Batch Processing** – Handles multiple product images at once.  
**AI-Powered Segmentation** – Uses **Segment Anything Model (SAM)** to extract product images.  
**Realistic Placement** – Ensures correct **perspective, lighting, and transparency**.  
**Preserves Product Details** – Keeps the original **quality, clarity, and shape**.  
**Uses Only Free & Open-Source Models** – No paid APIs or tools required.  
**Optimized for Lean Hardware** – Runs on standard machines without high-end GPUs.

## Installation & Setup

### 1. Clone the Repository

= git clone https://github.com/rahuljoshi1814/GenerativeAI-Product-Placement.git
= cd GenerativeAI-Product-Placement

### 2. Install Dependencies

- pip install -r requirements.txt

### 3. Download the Required AI Model

- The Segment Anything Model (SAM) is required for segmentation.
- Follow the instructions in models/README.md to download and place the model.

### 4. Download & Place the Dataset

- Download product images from the provided link.
- Follow the instructions in inputs/products/README.md.

## Running the Project
- Once everything is set up, run: **python main.py**
- This will process all product images and save the final results in outputs/.

## Dataset Information
- Product Images: Download from **inputs/products/README.md**.
- Background Images: Stored in **inputs/backgrounds/**.
- AI Model Checkpoints: Download instructions in **models/README.md**.

## Technologies Used
- Python
- OpenCV
- Segment Anything Model (SAM)
- NumPy
- TQDM (Progress Bar)

## Possible Improvements
This project is functional, but there are several ways to enhance it further:

- **Better Depth Matching** – Use depth estimation models to match product depth with the background for even more realistic placement.
- **Advanced Lighting Adjustments** – Implement neural relighting to adjust product lighting according to background conditions.
- **User-Specified Positioning** – Allow users to manually adjust the placement of products inside backgrounds.
- **More AI-Based Enhancements** – Integrate Stable Diffusion Inpainting to refine product blending using generative AI.

### Author

**Rahul Joshi**

📧 Email: **rahuljoshi1814@gmail.com **

💼 LinkedIn: **https://www.linkedin.com/in/rahul-joshi-39a3a3276/ **

🔗 GitHub: **https://github.com/rahuljoshi1814/GenerativeAI-Product-Placement.git **



