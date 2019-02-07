"""https://www.blog.pythonlibrary.org/2016/10/11/how-to-create-a-diff-of-an-image-in-python/"""

from PIL import Image
from PIL import ImageChops

def compare_images(path_one, path_two, diff_save_location):
    """
    Compares to images and saves a diff image, if there
    is a difference
 
    @param: path_one: The path to the first image
    @param: path_two: The path to the second image
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
 
    diff = ImageChops.difference(image_one, image_two)
 
    if diff.getbbox():
        diff.save(diff_save_location)
 
 
if __name__ == '__main__':
    compare_images('/Users/jack/Desktop/xxx.jpg',
                   '/Users/jack/Desktop/yyy.jpg',
                   '/Users/jack/Desktop/diff.jpg')
