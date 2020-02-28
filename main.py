import os, PIL
from PIL import Image
from shutil import copyfile
import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline


ratio = 16/9
threshold = 0.157
# Find photos with an aspect ratio of 16/9

def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(('.png')):
                matches.append(os.path.join(root, filename))
    for i in matches:
        try:
            im = Image.open(i)
        except PIL.UnidentifiedImageError:
            print("Exception PIL.UnidentifiedImageError occured with image\n"+i)
            matches.remove(i)
        except FileNotFoundError:
            print("Exception FileNotFoundError occured with image\n"+i+"\nFile may be ghost index?")
            matches.remove(i)
    return matches

matches = fileList("D:\\Le\\Lee")
print(matches)
y = []
for i in matches:
    im = Image.open(i)
    width, height = im.size
    aspect = width/height
    y.append(aspect)
    #print(aspect)
    if aspect >= ratio*(1-threshold) and aspect <= ratio*(1+threshold):
        print("Found aspect ratio "+str(aspect)+" in:\n"+i)
        #copyfile(i, "G:\\"+os.path.basename(i))

x = list(range(0, len(matches)))

plt.figure(1)
plt.plot(x, y, 'o', color='black')
plt.axhline(y=ratio, color='k', linestyle='--')
plt.axhline(y=ratio*(1-threshold), color='r', linestyle='-')
plt.axhline(y=ratio*(1+threshold), color='r', linestyle='-')
#plt.ylim([1.5,1.8])
plt.show()