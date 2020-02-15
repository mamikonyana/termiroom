#!/usr/bin/env python3
import rawpy
from pathlib import Path
import argparse
from tqdm import tqdm
from PIL import Image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--raw-folder', type=Path)
    parser.add_argument('-o', '--jpeg-folder', type=Path,
                        default=Path('./img'))
    args = parser.parse_args()

    args.jpeg_folder.mkdir(exist_ok=True)

    for path in tqdm(args.raw_folder.iterdir()):
        if path.suffix != '.CR2':
            continue
        with rawpy.imread(str(path)) as raw:
            img_data = raw.postprocess(no_auto_bright=True, output_bps=8)
        img = Image.fromarray(img_data)
        img.save(args.jpeg_folder / (path.stem + '.jpeg'))
