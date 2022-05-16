from skimage import data,filters
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

orig = np.array(Image.open('./stock_img/juice.jpg'))

# inverts the image :D
# using binary operation 
img = orig.copy()

print('shape: ',img.shape)
print('dimensions: ',img.ndim)
print('type: ',img.dtype.name)
print('pixel size: ',img[0][0].dtype.name)
print('pixels: ',img.size)

# for whole image:
#   img = ~img
# is quicker
# but i did pixel by pixel first
for x in range(len(img)):
    for y in range(len(img[x])):
        img[x,y] = ~img[x,y]

path = './basics/negative.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)

# grey scale bits
# thought was to average the RGB values to find how close to white (0xffffff)
# a pixel was, then putting the avergae in each to make it a grey image
img = orig.copy()

for x in range(len(img)):
    for y in range(len(img[x])):
        # sum all 3 for the average, this will give how close to white it is
        pixel = sum(img[x,y])//3
        img[x,y] = [pixel,pixel,pixel]

path = './basics/greyscale.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)

# color scale bits
# thought was apply the idea of grayscale but only one color
img = orig.copy()

# python 101 haha
# this selects everything in the array for the x and y
# then syays any one or two indexes for pixels should be zero
# poor image quality but efficient
img[:, :, (1,2)] = 0

path = './basics/quickcolorscale.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)

img = orig.copy()

# original thought for color scale
# similar to grey scale except only one pixel value is changed
for x in range(len(img)):
    for y in range(len(img[x])):
        # sum all 3 for the average, this will give how close to white it is
        pixel = sum(img[x,y])//3
        img[x,y] = [pixel,0,0]

path = './basics/colorscale.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)

img = orig.copy()

# this just removes the decimal values, making the value of each pixel less precise every time
img = (img // 128) * 128

path = './basics/reduction.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)

img = orig.copy()

# this evaluates each pixel to see if it is greater than 128 (half of 255)
# then the boolena from the comparison is multiplied by 255 (becomes 255 or 0)
# rendering every pixel as black or white
img = ((img > 128) * 255).astype(np.uint8)

path = './basics/binarize.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)

img = orig.copy()

pixel = img[100,60]
print(pixel)
for x in range(len(img)):
    for y in range(len(img[x])):
        # absolute difference 
        diff = abs(sum(img[x,y]//3)-sum(img[100,60]//3))
        if(diff < 20):
            img[x,y] = ~img[x,y]

path = './basics/selecting.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)