from keras.src.applications.mobilenet_v2 import MobileNetV2
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import models
from tensorflow.python.layers import layers
from src.main.python.gesturedetector.config.configurations import Config

img_size = (128, 128)
batch_size = 32
dataset_path_train = Config.get_config()['dataset_train_path']
dataset_path_validation = Config.get_config()['dataset_validation_path']

train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train_generator = train_datagen.flow_from_directory(
    dataset_path_train,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    dataset_path_validation,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)


base_model = MobileNetV2(input_shape=img_size + (3,), include_top=False, weights='imagenet')
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


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
