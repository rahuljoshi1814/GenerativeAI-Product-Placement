# GenerativeAI-Product-Placement
A Generative AI tool that places e-commerce product images into realistic backgrounds using SAM and OpenCV.

# 🛒 Generative AI Product Placement Tool

### **Automatically Place E-Commerce Product Images into Realistic Lifestyle Backgrounds using AI**  

🚀 This AI-powered tool takes standalone **product images** and seamlessly places them into **lifestyle backgrounds**, making them look like they naturally belong in the scene.

---

## 📌 Features
✅ **Batch Processing** – Handles multiple product images at once.  
✅ **AI-Powered Segmentation** – Uses **Segment Anything Model (SAM)** to extract product images.  
✅ **Realistic Placement** – Ensures correct **perspective, lighting, and transparency**.  
✅ **Preserves Product Details** – Keeps the original **quality, clarity, and shape**.  
✅ **Uses Only Free & Open-Source Models** – No paid APIs or tools required.  
✅ **Optimized for Lean Hardware** – Runs on standard machines without high-end GPUs.  

---

## 📂 Project Directory Structure
GenerativeAI-ProductPlacement/
│── main.py                     # Main script to run the pipeline
│── requirements.txt             # Dependencies list
│── README.md                    # Full project documentation
│── utils/                        # Helper functions
│   │── get_all_images.py         # Fetch images from folders
│   │── segmentation.py           # AI-based product segmentation (SAM)
│   │── blending.py               # Seamless blending with transparency
│   │── batch_processing.py       # Handles multiple images in batch mode
│── models/                       # Stores AI model checkpoints
│   │── README.md                 # Instructions to download SAM model
│── inputs/                       # Stores all input images
│   │── products/                 # Product images (organized in subfolders)
│   │   │── README.md             # Instructions to download & place dataset
│   │── backgrounds/              # Lifestyle background images
│   │   │── README.md             # (Optional) Instructions for adding backgrounds
│── outputs/                      # Final processed images
│── debug_outputs/                # Stores segmentation debug images
│── test_segmentation.py          # Script to test segmentation results
│── test_blending.py              # Script to test blending results


---

## 📥 **Installation & Setup**
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/GenerativeAI-ProductPlacement.git
cd GenerativeAI-Product-Placement

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Download the Required AI Model
- The Segment Anything Model (SAM) is required for segmentation.
- Follow the instructions in models/README.md to download and place the model.

### 4️⃣ Download & Place the Dataset
- Download product images from the provided link.
- Follow the instructions in inputs/products/README.md.

🚀 Running the Project
- Once everything is set up, run: python main.py
This will process all product images and save the final results in outputs/.

📂 Dataset Information
Product Images: Download from inputs/products/README.md.
Background Images: Stored in inputs/backgrounds/.
AI Model Checkpoints: Download instructions in models/README.md

## Technologies Used
- Python
- OpenCV
- Segment Anything Model (SAM)
- NumPy
- TQDM (Progress Bar)

## Possible Improvements
This project is functional, but there are several ways to enhance it further:

✅ **Better Depth Matching** – Use **depth estimation models** to match product depth with the background for even more realistic placement.  
✅ **Advanced Lighting Adjustments** – Implement **neural relighting** to adjust product lighting according to background conditions.  
✅ **User-Specified Positioning** – Allow users to **manually adjust** the placement of products inside backgrounds.  
✅ **More AI-Based Enhancements** – Integrate **Stable Diffusion Inpainting** to refine product blending using generative AI.

---

## 👨‍💻 Author
### **Rahul Joshi**  
📧 **Email:** rahuljoshi1814@gmail.com  
💼 **LinkedIn:** https://www.linkedin.com/in/rahul-joshi-39a3a3276/ 




