import cv2
img = cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
cv2.waitkey(0)
cv2.putText(img,  
           "Sun",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )
cv2.putText(img,  
           "Mercury",
           (50, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )
cv2.putText(img,  
           "Venus",
           (88, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )
cv2.putText(img,  
           "Mars",
           (90, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )
cv2.putText(img,  
           "Jupiter",
           (100, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )        
cv2.putText(img,  
           "Saturn",
           (120, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )
cv2.putText(img,  
           "Uranus",
           (142, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )   
cv2.putText(img,  
           "Neptune",
           (150, 300),  
           cv2.FONT_HERSHEY_COMPLEX,
           0.5,  
           (225,225,255)
           )

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)