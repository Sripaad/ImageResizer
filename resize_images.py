import os
import argparse
import re
import glob
from tqdm import tqdm
from PIL import Image, ImageFile
from joblib import Parallel, delayed
import resizer

ImageFile.LOAD_TRUNCATED_IMAGES = True


def resize_images():

    # taking user arguments
    parser = argparse.ArgumentParser(description="Resize images")
    parser.add_argument(
        "-i", "--inputdir", default=".", type=str, help="image path input directory"
    )
    parser.add_argument(
        "-o", "--outputdir", default=".", type=str, help="output save directory"
    )
    parser.add_argument(
        "-r", "resize", default="512x512", type=str, help="image resize dimentions"
    )
    args = parser.parse_args()
    input_folder = args.inputdir
    output_folder = args.outputdir
    resize = args.resize
    resize = re.split(r"x|X", resize)
    # Parallelize
    images = glob.glob(os.path.join(input_folder, "*.jpg"))
    Parallel(n_jobs=12)(
        delayed(resizer.resizer)(i, output_folder, (resize[0], resize[1]))
        for i in tqdm(images)
    )
