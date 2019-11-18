from PIL import Image
import os, sys

path = os.getcwd() + '/nica/'
print( 'path ', path )
dirs = os.listdir( path )
print (dirs)
final_size = 600;

def resize_aspect_fit():
    print('fn')
    for item in dirs:
        print('continue', path + ' ' , item)
        # if item == '.DS_Store':
        #     continue
        # if os.path.isfile(path+item):
        print('image')
        im = Image.open(path+item)
        print('im i', im)
        f, e = os.path.splitext(path+item)
        size = im.size
        print ('size')
        ratio = float(final_size) / max(size)
        new_image_size = tuple([int(x*ratio) for x in size])
        im = im.resize(new_image_size, Image.ANTIALIAS)
        new_im = Image.new("RGB", (final_size, final_size))
        new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
        new_im.save(f + 'resized.jpg', 'JPEG', quality=90)


resize_aspect_fit()