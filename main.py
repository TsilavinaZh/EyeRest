import cv2

face_cascade = cv2.CascadeClassifier('Tools/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Tools/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
closed_eyes_frame = 0
threshold = 20 

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    status = "REVEILLER"

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)

        if len(eyes) == 0:
            closed_eyes_frame += 1
        else:
            closed_eyes_frame = 0



        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    if closed_eyes_frame > threshold:
        status = "ENDORMI"
        cv2.putText(frame, "ALERTE SOMMEIL", (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.putText(frame, f"ETAT : {status}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 2)

    cv2.imshow("EyeRest", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()