from facenet_pytorch import MTCNN

mtcnn = MTCNN()


def analyze_image(image):
    boxes, _ = mtcnn.detect(image)
    return boxes is not None and len(boxes) >= 1


if __name__ == '__main__':
    from PIL import Image
    example = Image.open("imagen.jpg")
    result = analyze_image(example)
    print(f"face: {result}")
