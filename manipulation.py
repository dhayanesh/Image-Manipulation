import cv2
import numpy as np
import os
import math

#--------------------------------------------------------------------------------
#convert to grayscale
img = cv2.imread("image.png", cv2.IMREAD_COLOR)
imageHeight = len(img)
imageWidth = len(img[0])

for i in range(imageHeight):
    for j in range(imageWidth):
            img[i][j] = int((0.299+img[i][j][0] + 0.587+img[i][j][1] + 0.114+img[i][j][2]) / 3)

filename = 'gray_image.png'
cv2.imwrite(filename, img)

#--------------------------------------------------------------------------------  
#scaling
img2 = cv2.imread("gray_image.png", cv2.IMREAD_COLOR)
scale = 0.5

scaledHeight = int(len(img2)/2)
scaledWidth = int(len(img2[0])/2)

pixel = np.zeros([scaledHeight,scaledWidth,3],dtype=np.uint8)
pixel.fill(255) #blank white image to store scaled image

for y in range(scaledHeight):
    for x in range(scaledWidth):
        x_nearest = int(np.round(x/scale))
        y_nearest = int(np.round(y/scale))        
        pixel[y][x] = img2[y_nearest][x_nearest]   

filename = 'gray_image_scaled.png'
cv2.imwrite(filename, pixel)            
        
#--------------------------------------------------------------------------------
#Translating
img3 = cv2.imread("gray_image.png", cv2.IMREAD_COLOR)
translateImg = np.zeros([imageHeight,imageWidth,3],dtype=np.uint8)

for i in range(imageHeight):
    for j in range(imageWidth):
        if(i<imageHeight - 50 and j<imageWidth - 50):
            translateImg[i+50][j+50] = img3[i][j]

filename = 'gray_image_translated.png'
cv2.imwrite(filename, translateImg)

#--------------------------------------------------------------------------------
#flipping horizontal
img4= cv2.imread("gray_image.png", cv2.IMREAD_COLOR)
flipHoriImg = np.zeros([imageHeight,imageWidth,3],dtype=np.uint8)

for i in range(imageHeight):
    for j in range(imageWidth):  
        x = imageWidth-1      
        flipHoriImg[i][x-j] = img4[i][j]

filename = 'gray_image_flip_horizontal.png'
cv2.imwrite(filename, flipHoriImg)

#--------------------------------------------------------------------------------
#flipping vertical
img5 = cv2.imread("gray_image.png", cv2.IMREAD_COLOR)
flipVertiImg = np.zeros([imageHeight,imageWidth,3],dtype=np.uint8)

for i in range(imageHeight):
    x = imageHeight-1
    for j in range(imageWidth):
        flipVertiImg[x-i][j] = img5[i][j]

filename = 'gray_image_flip_vertical.png'
cv2.imwrite(filename, flipVertiImg)

#--------------------------------------------------------------------------------
#inversion
img6 = cv2.imread("gray_image.png", cv2.IMREAD_COLOR)
invertImg = np.zeros([256,512,3],dtype=np.uint8)
invertImg.fill(255)

invertImg = invertImg - img6

filename = 'gray_image_inversion.png'
cv2.imwrite(filename, invertImg)

#--------------------------------------------------------------------------------
#rotation
img7 = cv2.imread("gray_image.png", cv2.IMREAD_COLOR)
#rotateImg = np.zeros([256,512,3],dtype=np.uint8)
rotateImg = np.uint8(np.zeros(img7.shape))
rotationRad = math.radians(45)
#print(rotationRad)

midY = int((rotateImg.shape[1])/2) 
midX = int((rotateImg.shape[0])/2)  
#print(midX, midY)

for i in range(imageHeight):
    for j in range(imageWidth):
        newX = (i-midX)*math.cos(rotationRad) - (j-midY)*math.sin(rotationRad)
        newY = (i-midX)*math.sin(rotationRad) + (j-midY)*math.cos(rotationRad)

        newX = round(newX) + midX
        newY = round(newY) + midY

       # print(newX, newY)
        if (newX >= 0 and newY >= 0 and newX < imageHeight and newY < imageWidth):
            rotateImg[i,j,:] = img7[newX,newY,:]

filename = 'gray_image_rotated.png'
cv2.imwrite(filename, rotateImg) 


#--------------------------------------------------------------------------------
###BONUS###
#scaling
img2 = cv2.imread("image.png", cv2.IMREAD_COLOR)
scale = 0.5

scaledHeight = int(len(img2)/2)
scaledWidth = int(len(img2[0])/2)

pixel1 = np.zeros([scaledHeight,scaledWidth,3],dtype=np.uint8)
pixel1.fill(255) #blank white image to store scaled image

for y in range(scaledHeight):
    for x in range(scaledWidth):
        x_nearest = int(np.round(x/scale))
        y_nearest = int(np.round(y/scale))        
        pixel1[y][x] = img2[y_nearest][x_nearest]   

filename = 'image_scaled.png'
cv2.imwrite(filename, pixel1)            
        

#Translating
img3 = cv2.imread("image.png", cv2.IMREAD_COLOR)
translateImg1 = np.zeros([imageHeight,imageWidth,3],dtype=np.uint8)

for i in range(imageHeight):
    for j in range(imageWidth):
        if(i<imageHeight - 50 and j<imageWidth - 50):
            translateImg1[i+50][j+50] = img3[i][j]

filename = 'image_translated.png'
cv2.imwrite(filename, translateImg1)


#flipping horizontal
img4= cv2.imread("image.png", cv2.IMREAD_COLOR)
flipHoriImg1 = np.zeros([imageHeight,imageWidth,3],dtype=np.uint8)

for i in range(imageHeight):
    for j in range(imageWidth):  
        x = imageWidth-1      
        flipHoriImg1[i][x-j] = img4[i][j]

filename = 'image_flip_horizontal.png'
cv2.imwrite(filename, flipHoriImg1)


#flipping vertical
img5 = cv2.imread("image.png", cv2.IMREAD_COLOR)
flipVertiImg1 = np.zeros([imageHeight,imageWidth,3],dtype=np.uint8)

for i in range(imageHeight):
    x = imageHeight-1
    for j in range(imageWidth):
        flipVertiImg1[x-i][j] = img5[i][j]

filename = 'image_flip_vertical.png'
cv2.imwrite(filename, flipVertiImg1)
###BONUS###
#--------------------------------------------------------------------------------



#cv2.imshow("image", img)
#cv2.imshow("image2", pixel)
#cv2.imshow("image3", translateImg)
#cv2.imshow("image4", flipVertiImg) 
#cv2.imshow("image5", flipHoriImg)
#cv2.imshow("image6", invertImg)
#cv2.imshow("image7", rotateImg)


cv2.waitKey(0)
cv2.destroyAllWindows()