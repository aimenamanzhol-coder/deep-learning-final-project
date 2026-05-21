"""
mobilenet_model.py
-------------------
Transfer Learning model using MobileNetV2.
"""

import tensorflow as tf
from tensorflow.keras import layers, models


def build_mobilenet_model():

    # Data augmentation
    data_augmentation = tf.keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ])

    # Pretrained MobileNetV2
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(150, 150, 3),
        include_top=False,
        weights='imagenet'
    )

    # Freeze pretrained layers
    base_model.trainable = False

    # Final model
    model = models.Sequential([

        data_augmentation,

        layers.Rescaling(1./255),

        base_model,

        layers.GlobalAveragePooling2D(),

        layers.Dropout(0.3),

        layers.Dense(128, activation='relu'),

        layers.Dropout(0.3),

        layers.Dense(6, activation='softmax')
    ])

    return model
