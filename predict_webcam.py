import argparse, cv2
from ultralytics import YOLO

parser = argparse.ArgumentParser()
parser.add_argument('--weights', default="best.pt")
parser.add_argument('--conf', type=float, default=0.25)
parser.add_argument('--source', default=0)
args = parser.parse_args()

model = YOLO(args.weights)
cap = cv2.VideoCapture(int(args.source) if str(args.source).isdigit() else args.source)

while True:
    ok, frame = cap.read()
    if not ok:
        break
    results = model(frame, conf=args.conf)
    annotated = results[0].plot()
    cv2.imshow("YOLOv8 Webcam", annotated)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
