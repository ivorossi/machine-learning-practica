import cv2


def detect_face_in_image(image_path):
    # Cargar el modelo de detección de rostro
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Cargar la imagen
    image = cv2.imread(image_path)
    if image is None:
        print("Error: no se pudo cargar la imagen.")
        return False

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Verificar si se encontraron rostros
    if len(faces) > 0:
        print(f"Rostro(s) detectado(s): {len(faces)}")
        return True
    else:
        print("No se detectaron rostros.")
        return False


# Ejemplo de uso
if __name__ == "__main__":
    image_path = "ruta/de/tu/imagen.jpg"  # Reemplaza esto con la ruta de tu imagen
    has_face = detect_face_in_image(image_path)
    if has_face:
        print("La imagen contiene al menos un rostro humano.")
    else:
        print("La imagen no contiene rostros humanos.")
