import cv2
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'G:/Users/Soham More/AppData/Local/Tesseract-OCR/tesseract.exe'
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



img  = cv2.imread('path to image containing text')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

text = tess.image_to_string(img)
print(text)
print("Image shape", img.shape)

'''
#detect characters
himg, wimg,_ = img.shape
#cong = r'--oem 3 --psm 6 outputbase digits' # identify only digits
boxes = tess.image_to_boxes(img)
for b in boxes.splitlines():
	b = b.split(' ')
	x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])

	cv2.rectangle(img,(x,himg-y),(w,himg-h),(0,0,255),1)
	cv2.putText(img,b[0],(x,himg-y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)
'''


#detect words
himg, wimg,_ = img.shape
boxes = tess.image_to_data(img)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
	if x!=0:
		b = b.split()
		print(b)
		if len(b)==12:
			x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])

			cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
			cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)



'''
# detect numbers only
himg, wimg,_ = img.shape
#cong = r'--oem 3 --psm 6 outputbase digits'
boxes = tess.image_to_data(img) #config=cong
for x,b in enumerate(boxes.splitlines()):
	if x!=0:
		b = b.split()
		print(b)
		if len(b)==12:
			x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])

			cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
			cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

'''
cv2.imshow('result', img)
cv2.waitKey(0)