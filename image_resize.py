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


def get_new_image_size(source_width, source_height, new_width, new_height, scale):
    if scale:
        return int(source_width * scale), int(source_height * scale)
    if not new_height:
        scale = new_width / source_width
        return new_width, int(source_height * scale)
    if not new_width:
        scale = new_height / source_height
        return int(source_width * scale), new_height
    return new_width, new_height


def is_proportion_changed(source_width, source_height, new_width, new_height):
    permissible_error = 0.005
    proportions = new_width / source_width - new_height / source_height
    return abs(proportions) > permissible_error


def resize_image(source_image, args):
    source_width, source_height = source_image.size
    new_width, new_height = get_new_image_size(source_width, source_height, args.width, args.height,
                                               args.scale)
    is_ratio_changed = is_proportion_changed(source_width, source_height, new_width, new_height)
    new_image = source_image.resize((new_width, new_height), Image.ANTIALIAS)
    return new_image, is_ratio_changed


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
    source_image = Image.open(args.path)
    new_image, is_ratio_changed = resize_image(source_image, args)
    if is_ratio_changed:
        print('The proportions are not the same as in the original image.')
    save_new_image(args.output, args.path, new_image)
    print('The image was resized successfully!')

