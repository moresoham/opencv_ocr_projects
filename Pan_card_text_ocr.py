import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'G:/Users/Soham More/AppData/Local/Tesseract-OCR/tesseract.exe'
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



img  = cv2.imread('imageTextN.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgcpy = img.copy()
print("Image shape", img.shape)
w = img.shape[1]
h = img.shape[0]
#img = cv2.resize(img,(w//3,h//3))

bb = cv2.selectROI("Tracking",img,False)
#print(bb)
#imgcrop = img[int(bb[0]):int(bb[1]),int(bb[2]):int(bb[3])]

imgcrop = img[int(bb[1]):int(bb[1])+int(bb[3]),int(bb[0]):int(bb[0])+int(bb[2])]

text = tess.image_to_string(imgcrop).lstrip()
t = text.split('\n')
print(t)


himg, wimg,_ = imgcrop.shape
boxes = tess.image_to_data(imgcrop)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
	if x!=0:
		b = b.split()
		print(b)
		if len(b)==12:
			x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])

			cv2.rectangle(imgcrop,(x,y),(w+x,h+y),(0,0,255),1)
			cv2.putText(imgcrop,b[11],(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.4,(50,50,255),1)


# IGNORE THIS
'''
# name 
himg, wimg,_ = img.shape
boxes = tess.image_to_data(img)
x,y,w,h = 35,100,200,26
cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,255),1)
cv2.putText(img,t[1],(x,y),cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),2)

# father name
x1,y1,w1,h1 = 35,128,160,26
cv2.rectangle(img,(x1,y1),(w1+x1,h1+y1),(0,255,255),1)
cv2.putText(img,t[2],(x1,y1),cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),2)

# DOB
x2,y2,w2,h2 = 35,160,140,26
cv2.rectangle(img,(x2,y2),(w2+x2,h2+y2),(0,255,255),1)
cv2.putText(img,t[3],(x2,y2),cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),2)

# pan number
x3,y3,w3,h3 = 35,220,200,26
cv2.rectangle(img,(x3,y3),(w3+x3,h3+y3),(0,255,255),1)
cv2.putText(img,t[7],(x3,y3),cv2.FONT_HERSHEY_PLAIN,1,(50,50,255),2)

'''



# detect face 
faces = face_cascade.detectMultiScale(img, 1.6, 4) 
# parameters for face detection (img_src, scale, neighbors)


# bounding box creation
for (x_face,y_face,w_face, h_face) in faces:
	cv2.rectangle(img, (x_face,y_face), (x_face+w_face,y_face+h_face), (255,255,0), 3)

cv2.imshow('result', img)
#imgcrop = cv2.resize(imgcrop,(1000,200) )
cv2.imshow('result cropprd', imgcrop)
cv2.waitKey(0)