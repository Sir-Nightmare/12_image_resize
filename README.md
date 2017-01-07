# Image Resizer
This script changes the input image resolution according to the input parameters. 
The script can work with jpg, png and bmp.


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

**Notes:**

- You have to specify scale of resizing or width or height of new image. 
- You can also specify width and height together.  
- If you specify only width or height, another parameter will be computed to save ratio of original image.
- You can't use both scale and width / height options  
- If output is not specified, output file will be placed at folder with original image with name  `<original_filename>__<width>x<height>.<original_extension>`

**Examples:**

```
python image_resize.py D:\img.jpg  -H 1000 -w 1500 # result: img__1500x1000.jpg at the same folder
python image_resize.py D:\img.jpg -s 0.5 -o D:\img_foder\new_img.jpg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
