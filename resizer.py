import os
from PIL import Image, ImageFile


ImageFile.LOAD_TRUNCATED_IMAGES = True


def resizer(image_path, output_folder, resize):

    base_name = os.path.basename(image_path)
    outpath = os.path.join(output_folder, base_name)
    img = Image.open(image_path)
    img = img.resize((resize[1], resize[0]), resample=Image.BILINEAR)
    img.save(outpath)
