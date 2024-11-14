import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
import os


# Parámetros
img_size = (128, 128)
batch_size = 32

# Generador de datos
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2  # Dividimos 80% para entrenamiento, 20% para validación
)

train_generator = train_datagen.flow_from_directory(
    "ruta/a/tu/dataset",  # Cambia a la ruta de tu dataset
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    "ruta/a/tu/dataset",  # Cambia a la ruta de tu dataset
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)


# Cargar el modelo base de MobileNetV2
base_model = MobileNetV2(input_shape=img_size + (3,), include_top=False, weights='imagenet')
base_model.trainable = False  # Congelamos las capas del modelo base

# Construimos el modelo final
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')  # Salida binaria para con/sin lentes
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# Entrenamiento
epochs = 10
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=epochs
)


loss, accuracy = model.evaluate(validation_generator)
print(f'Precisión en el conjunto de validación: {accuracy * 100:.2f}%')


model.save("modelo_clasificacion_lentes.h5")
print("Modelo guardado exitosamente.")