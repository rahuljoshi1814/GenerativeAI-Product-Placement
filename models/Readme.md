# 📂 Segment Anything Model (`models/`)

## 📥 Downloading the SAM Model Checkpoint
The **Segment Anything Model (SAM)** is required for product segmentation.  
Since the model file is too large to be stored on GitHub, you need to **download it manually** and place it in this folder.

---

## 🔗 **Download the SAM Model Checkpoint**
Click the link below to download the required model:

🔗 **[SAM ViT-H Model (Largest, Best Accuracy)](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth)**

Alternatively, you can download smaller versions:
- 🔹 **[SAM ViT-L](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_l_0b3195.pth)** (Medium Size, Balanced Performance)
- 🔹 **[SAM ViT-B](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth)** (Smallest, Fastest)

---

## 📂 Organizing the Model Files
After downloading, **move the file** to this folder (`models/`).

✅ **Example Directory Structure:**
models/ │── sam_vit_h_4b8939.pth # Place the downloaded model file here │── (Other model files if needed)


---

## 🛠 Next Steps
1️⃣ **Make sure you have already downloaded the dataset** in `inputs/products/`.  
   - If not, follow the instructions in `inputs/products/README.md`.

2️⃣ **Once the model file is in place, run the pipeline:**
   ```bash
   python main.py
The script will automatically load the model from this folder.

