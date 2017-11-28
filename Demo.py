import numpy as np
import cv2

# load pre-trained cascade classifier xml file

card_cascade = cv2.CascadeClassifier('cascade.xml')




cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # add this
    # image, reject levels level weights.
    cards = card_cascade.detectMultiScale(gray, 1.3, 5)

    # add this
    for (x, y, w, h) in cards:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)


    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

# # fetch detected card location for display
# for (x, y, w, h) in cards:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     roi_gray = gray[y:y + h, x:x + w]
#     roi_color = img[y:y + h, x:x + w]
#
#
#     cv2.imshow('img', img)
#     cv2.waitKey(0)
#
# cv2.destroyAllWindows()


