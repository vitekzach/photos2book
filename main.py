from PIL import Image
import os
import glob
from tqdm import tqdm

FOLDER_PATH = r"F:\Mikro"
TARGET_WIDTH = 1000
QUALITY = 50
OPTIMIZE = False

files = glob.glob(f"{FOLDER_PATH}/*.jpg")

subfolder_name = f"w{TARGET_WIDTH}_q{QUALITY}_o{OPTIMIZE}"
os.makedirs(os.path.join(FOLDER_PATH, subfolder_name), exist_ok=True)


for image_name in files[:1]:
    image_name_rel = os.path.split(image_name)[-1]
    this_image = Image.open(os.path.join(FOLDER_PATH, image_name_rel))
    width, height = this_image.size
    coefficient = width / TARGET_WIDTH
    new_height = height / coefficient
    this_image = this_image.resize((int(TARGET_WIDTH), int(new_height)))
    this_image.save(os.path.join(FOLDER_PATH, subfolder_name, image_name_rel), quality=QUALITY, optimize=OPTIMIZE)


import logging
logging.warning("Creating PDF from root folder, next time append optimized folder")
pdf_path = os.path.join(FOLDER_PATH, 'book.pdf')
images_to_pdf = glob.glob(f"{FOLDER_PATH}/*.jpg")

Image.open(images_to_pdf[0]).save(pdf_path, "PDF" ,resolution=100.0, save_all=True,
                                  append_images=(Image.open(f) for f in images_to_pdf[1:]))


