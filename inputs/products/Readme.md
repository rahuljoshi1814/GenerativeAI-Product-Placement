# 📂 Product Images Folder (`inputs/products/`)

## 📥 Downloading the Dataset
To use this project, you need to **download the sample e-commerce product images** from the provided link.

🔗 **[Download Product Images](https://studio11productions.wetransfer.com/downloads/de89bec34407552e6e9596a465ed0cc420250219133542/7efbc8?t_exp=1771508142&t_lsid=c7655ff4-3e6a-4692-adfb-e4a73e271c30&t_network=link&t_rid=YXV0aDB8VHJhbnNmZXJ8cHBveWdkOXRmeHl3aXI=&t_s=download_link&t_ts=1739972142)**

---

## 📂 Organizing the Dataset
1. **Download the ZIP file** from the above link.
2. **Extract the ZIP file**, and you will get a folder named:
- SWADESH 19-02-2024 (21 ARTICLE)
3. Inside this folder, you will find multiple subfolders containing images.
4. **Move all these subfolders here (`inputs/products/`)**.
---

## ✅ Example Directory Structure (After Extraction)
inputs/ │── products/ # Place the extracted folders here │ │── 471033148001-FLEP/ │ │── 471034853001-FLEP/ │ │── 471039589001/ │ │── 471039590001/ │ │── ... │── backgrounds/ │── models/ │── outputs/
---

## 🛠 Next Steps:
1️⃣ **Make sure you have downloaded the required models**.  
   - Go to `models/` and check if the SAM model file (`sam_vit_h_4b8939.pth`) is there.
   - If not, follow the instructions in `models/README.md` to download it.  

2️⃣ **Once the dataset is placed correctly, run the pipeline:**  
   ```bash
   python main.py

This will automatically process the images and save them in the outputs/ folder.

## Important Notes
- Do not modify the image filenames after extracting the dataset.
- Ensure that all extracted folders are placed directly inside inputs/products/.
- The pipeline will automatically detect all images inside subfolders.

