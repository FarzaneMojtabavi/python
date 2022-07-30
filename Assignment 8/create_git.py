import os
import imageio
images=[]
myfiles=os.listdir('picgif')
for i in range(len(myfiles)):
    image=imageio.imread('picgif/'+myfiles[i])
    images.append(image)
imageio.mimsave('moshiongif.gif',images)    