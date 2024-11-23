import dlib
import cv2
import numpy as np

detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")


def get_face_descriptor(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    descriptors = []
    for face in faces:
        shape = shape_predictor(gray, face)
        descriptor = np.array(face_rec_model.compute_face_descriptor(image, shape))
        descriptors.append(descriptor)
    return descriptors


def compare_faces(descriptor1, descriptor2, threshold=0.6):
    distance = np.linalg.norm(descriptor1 - descriptor2)
    return distance < threshold, distance


face_db = {}  # { "name": descriptor }


def register_face(name, image):
    descriptors = get_face_descriptor(image)
    if descriptors:
        face_db[name] = descriptors[0]
        print(f"Rostro registrado: {name}")
    else:
        print("No se detectaron rostros en la imagen.")


def recognize_face(image):
    descriptors = get_face_descriptor(image)
    if not descriptors:
        print("No se detectaron rostros.")
        return

    for name, ref_descriptor in face_db.items():
        match, distance = compare_faces(descriptors[0], ref_descriptor)
        if match:
            print(f"Rostro reconocido: {name}, Distancia: {distance:.4f}")
            return
    print("Rostro no reconocido.")
