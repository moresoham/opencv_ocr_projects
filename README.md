## opencv_ocr_projects
The Repository has 2 projects which works on OCR ( Optical Character Recognition ) and opencv.

## opencv and ocr for detection of text, character and only numbers.
This application uses OCR and opencv to detect text, character and only numbers using image_to_boxes() and image_to_data(). The app identifies each word, character as well as gives output on editor screen as what has been extracted.

Refer "project1.py"


## opencv and ocr for selctive text extraction + face detection 
Using ROI method of opencv, the user can draw a rectangle onto region of interest for extraction of the text. Instead of extracting all the text from image, this app helps to select only particular section or region of image and text inside it.
If you are using images which has a face, then a bounding box will be created around face inside image. It uses haarcascade method (haarcascade_frontalface_default) to detect face.

Refer "Pan_card_text_ocr.py"


## requirements
1. install opencv-python
2. install pytessaract
3. install the exe file - tesseract file can be downloaded from google
4. install numpy

Remember that the path where you installed the exe file. That path will be used in application (.exe). 




