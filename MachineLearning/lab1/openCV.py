#import the OpenCv module
import cv2

#Reading image
img = cv2.imread('imgs/butterfly.jpg', 1)

#measure and size
print(img.shape, img.size)

#copy and place the region
cutted = img[110:238, 124:252]
img[0:128, 0:128] = cutted

#Set new shapes
resized = cv2.resize(img, (600, 600))

#Change color line on the image
img[176, 157] = (255, 0, 0)
img[176, 158] = (255, 0, 0)
img[176, 159] = (255, 0, 0)
img[176, 160] = (255, 0, 0)
img[176, 161] = (255, 0, 0)
img[176, 162] = (255, 0, 0)
img[176, 163] = (255, 0, 0)
img[176, 164] = (255, 0, 0)

#New shape = Old shape/2
scale_resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

#Shows the image on the window
cv2.imshow('image', img)


#Face Detecting
#Load the cascade
cascade = cv2.CascadeClassifier('classifier.xml')
#Read the input image
face_image = cv2.imread('imgs/footballer.jpeg')

#Convert into grayscale
gray = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

#Detect faces
faces = cascade.detectMultiScale(gray, 1.3, 5)

#Draw rectangle arround the faces
for (x, y, w, h) in faces:
    cv2.rectangle(face_image, (x, y), (x+w, y+h), (255, 0, 0), 2)

#display the output
cv2.imshow('detected', face_image)
#Wait so many times, you want
cv2.waitKey(0)








