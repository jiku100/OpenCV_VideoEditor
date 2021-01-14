import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("asdA", frame)
    if cv2.waitKey(10) == 27:
        break

