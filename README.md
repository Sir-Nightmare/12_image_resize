# Image Resizer


## Usage
- run `pip3 install -r requirements.txt` to install necessary module **Pillow**
- run `python image_resize.py <path_to_original_file> <options>` to launch the script

**Options:**

name | type | key |
--- | --- | --- |
**Scale** | float | `-s, --scale`
**Width** | int | `-w, --width`
**Height** | int | `-H, --height`
**Output** | string | `-o, --output`
**Help** | string | `-h, --help`

You have to specify scale or width or height. You can also specify width and height together.  
Note that you can't use both scale and width / height options  
If output is not specified, output file will be placed at folder with original image with name  `<original_filename>__<width>x<height>.<original_extension>`


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
