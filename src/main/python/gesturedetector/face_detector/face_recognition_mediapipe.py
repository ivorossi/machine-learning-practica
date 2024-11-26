import cv2
import mediapipe as mp
from mediapipe.python.solutions import face_detection

mp_face_detection = mp.solutions.face_detection


def detect_face(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image_rgb)
    return len(results.detections) > 0


if __name__ == "__main__":
    image_path = "ruta/de/tu/imagen.jpg"
    has_face = detect_face(cv2.imread(image_path))
    if has_face:
        print("La imagen contiene al menos un rostro humano.")
    else:
        print("La imagen no contiene rostros humanos.")
