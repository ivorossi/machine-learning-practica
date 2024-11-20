from facenet_pytorch import MTCNN
from PIL import Image, ImageDraw

# Inicializar MTCNN
mtcnn = MTCNN()

# Cargar imagen
image = Image.open('imagen.jpg')

# Detectar rostros
boxes, _ = mtcnn.detect(image)

# Dibujar las cajas en la imagen
image_draw = image.copy()
draw = ImageDraw.Draw(image_draw)
for box in boxes:
    draw.rectangle(box.tolist(), outline=(255, 0, 0), width=3)

# Mostrar la imagen
image_draw.show()
