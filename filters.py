from skimage import data,filters
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

orig = np.array(Image.open('./stock_img/juice.jpg'))
img = orig.copy()

print('shape: ',img.shape)
print('dimensions: ',img.ndim)
print('type: ',img.dtype.name)
print('pixel size: ',img[0][0].dtype.name)
print('pixels: ',img.size)

pixel = img[240,400]
print(pixel)
for x in range(len(img)):
    for y in range(len(img[x])):
        # absolute difference 
        diff = abs(sum(img[x,y]//3)-sum(img[240,400]//3))
        if(diff < 10):
            img[x,y] = ~img[x,y]

path = './filters/filter.jpg'
pil_img = Image.fromarray(img)
pil_img.save(path)