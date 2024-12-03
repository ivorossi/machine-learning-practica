import cv2
import mediapipe as mp
from mediapipe.python.solutions import face_detection

mp_face_detection = mp.solutions.face_detection


def detect_face(image):
    # Convierte la imagen a RGB (MediaPipe requiere formato RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Inicializa FaceDetection
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        # Procesa la imagen
        results = face_detection.process(image_rgb)

        # Verifica si hay detecciones
        return results.detections is not None and len(results.detections) > 0


if __name__ == "__main__":
    image_path = "ruta/de/tu/imagen.jpg"
    has_face = detect_face(cv2.imread(image_path))
    if has_face:
        print("La imagen contiene al menos un rostro humano.")
    else:
        print("La imagen no contiene rostros humanos.")
