import fitz
import os
from pathlib import Path

from tqdm import tqdm

root_directory = 'G:\\Shared drives\\ICS496\\2022Fall\\Posters\\Print\\'
files = ['']
mat = fitz.Matrix(300 / 72, 300 / 72)  # sets zoom factor for 300 dpi

for file in tqdm(os.listdir(root_directory)):
    if not file.lower().endswith(".pdf"):
        continue
    name = Path(file).stem
    doc = fitz.open(root_directory+file)
    page = doc.load_page(0)  # number of page
    # pix = page.get_pixmap(matrix=mat)
    pix = page.get_pixmap()
    pix.pil_save(name+".png", format="PNG")
