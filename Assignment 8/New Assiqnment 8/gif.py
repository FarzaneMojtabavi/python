import imageio
import os
file_list=os.listdir("images/")
images=[]
for file_name in file_list:
    print(file_name)
    file_path="images/"+file_name
    image= imageio.imread(file_path)
    images.append(image)
print(images)
imageio.mimsave("images/myoutputs.gif",images)