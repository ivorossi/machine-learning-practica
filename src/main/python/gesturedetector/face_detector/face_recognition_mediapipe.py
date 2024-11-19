import cv2
import mediapipe as mp

# Inicializamos los módulos de Mediapipe para detección de rostros
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Abrimos la cámara
cap = cv2.VideoCapture(0)

# Configuramos Mediapipe Face Detection
with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        # Convertimos el frame de BGR (por OpenCV) a RGB (por Mediapipe)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Realizamos la detección de rostros
        results = face_detection.process(frame_rgb)

        # Dibujamos las detecciones en el frame original
        if results.detections:
            for detection in results.detections:
                # Dibujar caja delimitadora y puntos clave
                mp_drawing.draw_detection(frame, detection)

        # Mostramos el frame con las detecciones
        cv2.imshow('Detección de Rostros', frame)

        # Salir si presionamos 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberamos los recursos
cap.release()
cv2.destroyAllWindows()
