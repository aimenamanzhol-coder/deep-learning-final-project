from tensorflow.keras import layers, models

def build_baseline_model():

    model = models.Sequential([

        layers.Input(shape=(150,150,3)),

        layers.Conv2D(32, (3,3), activation='relu'),
        layers.MaxPooling2D(),

        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(),

        layers.Conv2D(128, (3,3), activation='relu'),
        layers.MaxPooling2D(),

        layers.Flatten(),

        layers.Dense(128, activation='relu'),

        layers.Dense(6, activation='softmax')
    ])

    return model
