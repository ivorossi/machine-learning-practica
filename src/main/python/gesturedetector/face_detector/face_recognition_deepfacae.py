from deepface import DeepFace

# Analizar emociones, género, edad
result = DeepFace.analyze(img_path="imagen.jpg", actions=['emotion', 'age', 'gender'])
print(result)
