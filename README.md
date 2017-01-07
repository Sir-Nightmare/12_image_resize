# Image Resizer
This script changes the input image resolution according to the input parameters.  
Original image will not be changed. A new one wil be created.   
The script can work with jpg, png and bmp.


## Usage

- Clone repository: `git clone https://github.com/Sir-Nightmare/12_image_resize.git`  
- Install necessary module **Pillow** `pip3 install -r requirements.txt` 
- Launch the script: `python image_resize.py <path_to_original_file> <options>` 

**Options:**

name | type | key | desription
--- | --- | --- | ---|
**Scale** | float | `-s, --scale`| Scale of resizing (can be < 1)
**Width** | int | `-w, --width`| Width of new image
**Height** | int | `-H, --height`| Height of new image
**Output** | string | `-o, --output`| Output path (with name and extention of the file)
**Help** | string | `-h, --help`| List of all parameters

**Notes:**

- You have to specify scale or width or height. 
- You can also specify width and height together.  
- If you specify only width or height, second parameter will be computed to keep ratio of original image.
- You can't use both scale and width / height options.  
- If output is not specified, output file will be placed at folder with original image with name  `<original_filename>__<width>x<height>.<original_extension>`.

**Examples:**

```
python image_resize.py D:\img.jpg  -H 1000 -w 1500 # result: img__1500x1000.jpg at the same folder
python image_resize.py D:\img.jpg -s 0.5 -o D:\img_foder\new_img.jpg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
