from PIL import Image
from pillow_heif import register_heif_opener
import glob
import os

register_heif_opener()

path_converted = "PICS_CONVERTED/"

# Get all files with .HIF or .hif extension (case-insensitive)
hif_files = set(glob.glob('PICS_ORIGINAL/*.HIF') + glob.glob('PICS_ORIGINAL/*.hif'))

for file in hif_files:
    try:
        image = Image.open(file)

        path, filename = os.path.split(file)
        l_file = filename.lower()

        new_file = path_converted + l_file.replace("hif", "jpg")
        image.save(new_file, format='jpeg', optimize = True, quality = 100)
        print(f"Converted {file} to {l_file.replace('hif', 'jpg')}")
    except Exception as e:
        print(f"Error processing {file}: {e}")
