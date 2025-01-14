import cv2
import numpy as np
from matplotlib import pyplot as plt



#Converts image to HSV color space
#cv2.cvtColor
#Next need to use numpy to display the chart and match different photos together based on color


shirt="/Users/alexandermcgreevy/Documents/GitHub/Projects-Clone/Colorblind Clothes Matcher/BlueShirt.jpg"

img = cv2.imread(shirt)

histogram=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histogram)
plt.show()