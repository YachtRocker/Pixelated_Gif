from PIL import Image
import glob
from natsort import natsorted

img = 'Meuq2.png'
# open image
img = Image.open(img)
size = 128
num = 1

img.save('./results/image_0.png')

while (size > 7):
    # Resizes down to the resampled size
    imgSmall = img.resize((size, size), resample=Image.BILINEAR)
    # Scale back up to original size
    result = imgSmall.resize(img.size,Image.NEAREST)
    # Saves Result
    result.save('./results/image_' + str(num) + '.png')
    # Decreases the size of the image each time through the loop
    size = size - 8
    num += 1



# Creates the GIF
#filepaths
fp_in = "./results/image_*.png"
fp_out = "./results/image.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in natsorted(glob.glob(fp_in), reverse=True)]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=600, loop=0)