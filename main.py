import cv2
import numpy as np
import random
#importing haarcascade classifiers from OpenCV
face_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarascades\haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_mcs_mouth.xml')

bw_threshold = 80
font = cv2.FONT_HERSHEY_SIMPLEX
org = (30, 30)
wore_mask_font_color = (255, 255, 255)
not_wore_mask_font_color = (0, 0, 255)
thickness = 2
font_scale = 1
wore_mask = "Thank You for wearing MASK"
not_wore_mask = "Please wear MASK to defeat Corona"
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow('black_and_white', black_and_white)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 4)

    if (len(faces) == 0 and len(faces_bw) == 0):
        cv2.putText(img, "No face found...", org, font, font_scale, wore_mask_font_color, thickness, cv2.LINE_AA)
        #when no face is found
    elif (len(faces) == 0 and len(faces_bw) == 1):
        cv2.putText(img, wore_mask, org, font, font_scale, wore_mask_font_color, thickness, cv2.LINE_AA)
        #the code cant detect a white mask
    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.1, 5)
        #if lips/mouth is visible then person is not wearing a mask otherwise wearing a mask
        if (len(mouth_rects) == 0):
            cv2.putText(img, wore_mask, org, font, font_scale, wore_mask_font_color, thickness, cv2.LINE_AA)
        else:
            for (mx, my, mw, mh) in mouth_rects:

                if (y < my < y + h):
                    cv2.putText(img, not_wore_mask, org, font, font_scale, not_wore_mask_font_color, thickness, cv2.LINE_AA)
                    cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)
                    break

    cv2.imshow('Mask Detection', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
