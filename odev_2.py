import cv2 as cv
import numpy as np

num = input('Which photo do you want to upload(1,2,3,4,5) ')
dosya_adi = 'data_set/photo-' + num + '.jpg'
img = cv.imread(dosya_adi)


blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)


lower_red1 = np.array([0, 100, 40])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 40, 40])
upper_red2 = np.array([179, 255, 255])

mask1 = cv.inRange(hsv, lower_red1, upper_red1)
mask2 = cv.inRange(hsv, lower_red2, upper_red2)
red_mask = mask1 + mask2

contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

if contours:
    
    largest_contour = max(contours, key=cv.contourArea)

   
    x, y, w, h = cv.boundingRect(largest_contour)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

 
    cx = x + w // 2
    cy = y + h // 2
    cv.circle(img, (cx, cy), 5, (255, 0, 0), -1)

    cv.putText(img, f"STOP ({cx},{cy})", (x, y - 10),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    print(f"Stop tabelasi bulundu: merkez=({cx}, {cy}), rec=({x},{y},{w},{h})")



cv.imshow("Result", img)
cv.imwrite("output_1.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()