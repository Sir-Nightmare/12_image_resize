import argparse

from os.path import exists, splitext
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to the image')
    parser.add_argument('-w', '--width', type=int)
    parser.add_argument('-H', '--height', type=int)
    parser.add_argument('-s', '--scale', type=float)
    parser.add_argument('-o', '--output')
    return parser.parse_args()


def get_new_image_size(width, height, scale):
    if scale:
        return int(image.width * scale), int(image.height * scale)
    if not height:
        scale = width / image.width
        return width, int(image.height * scale)
    if not width:
        scale = height / image.height
        return int(image.width * scale), height
    return width, height


def is_proportions_match(sourse_width, source_height, new_width, new_height):
    permissible_error = 0.005
    proportions = new_width / sourse_width - new_height / source_height
    return abs(proportions) < permissible_error


def save_new_image(output_path, path_to_image, image):
    if output_path:
        image.save(output_path)
    else:
        width, height = image.size
        base, ext = splitext(path_to_image)
        image.save('{}__{}x{}{}'.format(base, width, height, ext))


if __name__ == '__main__':
    args = get_args()
    if not exists(args.path):
        exit('Image does not exist')
    if args.scale and (args.width or args.height):
        exit('You can not specify the width or height and scale at one time.')
    if not (args.scale or args.width or args.height):
        exit('You have to specify the scale or height or width of result image.')
    image = Image.open(args.path)
    sourse_width, source_height = image.size
    new_width, new_height = get_new_image_size(args.width, args.height, args.scale)
    if not args.scale and not is_proportions_match(sourse_width, source_height, new_width,
                                                   new_height):
        print('The proportions are not the same as in the original image.')
    new_image = image.resize((new_width, new_height), Image.ANTIALIAS)
    save_new_image(args.output, args.path, new_image)
    print('The image was resized successfully!')
