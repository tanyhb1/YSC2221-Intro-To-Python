from scipy import misc, ndimage
import matplotlib.pyplot as plt

cat_pic = misc.imread('cute cat.jpg')
cat_pic.shape
cat_pic2 = cat_pic[150:400, 150:400, :]
rotate_cat = ndimage.rotate(cat_pic, 45)
rotate_face_noreshape = ndimage.rotate(cat_pic, 45, reshape=False)

for i in range(cat_pic.shape[0]):
    for j in range(cat_pic.shape[1]):
        if j < cat_pic.shape[1]/2:
            cat_pic[i][j]= 255-cat_pic[i][j]
            
plt.imshow(cat_pic)
plt.show()