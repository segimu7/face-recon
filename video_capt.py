import cv2, time, keyboard

video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    cv2.imshow("capturing",frame)
    cv2.waitKey(1)
    if keyboard.is_pressed('q'):
        break
video.release()
cv2.destroyAllWindows