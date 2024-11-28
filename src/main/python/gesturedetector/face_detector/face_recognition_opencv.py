import cv2
from src.main.python.gesturedetector.config.configurations import Config

face_cascade = cv2.CascadeClassifier(Config.get_config()['haar_cascade_frontal_face_cv_path'])


def detect_face_in_image(image):
    if image is None:
        return False
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    return len(faces) > 0


if __name__ == "__main__":
    image_path = "ruta/de/tu/imagen.jpg"
    has_face = detect_face_in_image(cv2.imread(image_path))
    if has_face:
        print("La imagen contiene al menos un rostro humano.")
    else:
        print("La imagen no contiene rostros humanos.")
