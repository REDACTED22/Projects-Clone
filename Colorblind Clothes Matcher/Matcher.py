import cv2
import numpy as np
from matplotlib import pyplot as plt
#Bacground removal package



#Converts image to HSV color space
#cv2.cvtColor
#Next need to use numpy to display the chart and match different photos together based on color

#removes background from image
shirt="/Users/alexandermcgreevy/Documents/GitHub/Projects-Clone/BlueShirt_no_bg.png"

img = cv2.imread(shirt)


blueHist=cv2.calcHist([img],[0],None,[256],[0,256])
greenHist=cv2.calcHist([img],[1],None,[256],[0,256])
redHist=cv2.calcHist([img],[2],None,[256],[0,256])

blue=np.argmax(blueHist)
green=np.argmax(greenHist)
red=np.argmax(redHist)

print(blue)
print(green)
print(red)
plt.plot(blueHist)
plt.show()
plt.plot(greenHist)
plt.show()
plt.plot(redHist)
plt.show()

#NEED TO FILTER OUT WHITE AND BLACK AS THEY ARE DOMINATING THE IMAGE or remove the background