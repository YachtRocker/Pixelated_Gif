from PIL import Image
import glob

img = 'Meuq2.png'
# open image
img = Image.open(img)
size = 128
num = 1

while (size > 7):
    imgSmall = img.resize((size, size), resample=Image.BILINEAR)
    result = imgSmall.resize(img.size,Image.NEAREST)
    result.save('./results/image_' + str(num) + '.png')
    size = size - 8
    num += 1




#filepaths
fp_in = "./results/image_*.png"
fp_out = "./results/image.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=1000, loop=0)