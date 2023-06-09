
import cv2
import face_recognition

 

img = cv2.imread("CR.png")

# Converting BGR Format to RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("images/Cristiano_Ronaldo.png")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

# Comparing both faces images and checking if they are same person
result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)


cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)
