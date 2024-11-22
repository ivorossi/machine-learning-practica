from deepface import DeepFace


def analyze_image(image):
    return DeepFace.analyze(image, actions=['emotion', 'age', 'gender'])


if __name__ == '__main__':
    import cv2
    example = cv2.imread("imagen.jpg")
    example = cv2.cvtColor(example, cv2.COLOR_BGR2RGB)
    result = analyze_image(example)
    print(result)
