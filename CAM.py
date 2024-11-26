
import cv2
import numpy as np
from ultralytics import YOLO

# טען מודל YOLOv8 מאומן מראש
model = YOLO("yolov8n.pt")

# אתחל את מצלמת האינטרנט
cap = cv2.VideoCapture(0)

while True:
    # קרא פריים מהמצלמה
    ret, frame = cap.read()
    
    # בצע זיהוי אובייקטים על הפריים
    results = model(frame)
    
    # צייר תיבות תוחמות ותוויות על הפריים
    for result in results:
        boxes = result.boxes.cpu().numpy()
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].astype(int)
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # הצג את הפריים עם הזיהויים
    cv2.imshow("Object Detection", frame)
    
    # צא מהלולאה אם נלחץ מקש 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# שחרר את המצלמה וסגור את החלונות
cap.release()
cv2.destroyAllWindows()