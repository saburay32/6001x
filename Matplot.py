import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image


img = Image.open('python.jpg')

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot()
ax.imshow(img)


plt.show()

# fig = plt.figure(figsize=(8,4))
# ax = fig.add_subplot()
#
# x = np.arange(-np.pi,np.pi,0.3)
# ax.stem(x,np.cos(x),bottom=.5)
#
# ax.grid()
#
# plt.show()


# x = np.arange(-2,2,0.1)
# y1 = np.array([-y**2 for y in x])+8
# y2 = np.array([-y**2 for y in x])+8
# y3 = np.array([-y**2 for y in x])+8
# ax.stackplot(x,y1,y2,y3)

# fig = plt.figure(figsize=(7,4),facecolor='#EEE')
# ax = fig.add_subplot()
# plt.figtext(0.05,0.6,'Window_zone text',fontsize=24,color='r')
# fig.suptitle('Window title')
# ax.set_xlabel('0x')
# ax.set_ylabel('0y')
#
# ax.text(0.5,0.1,"Soooooome text",bbox={'boxstyle':'darrow','facecolor':'g'})
# ax.annotate('Annotatione',xy=(0.2,0.4),xytext=(0.6,0.7),arrowprops={'facecolor':'gray','shrink':0.1})
# plt.show()