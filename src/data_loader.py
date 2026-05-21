import tensorflow as tf

IMG_SIZE = (150, 150)
BATCH_SIZE = 32

def load_data(train_path, test_path):

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_path,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        train_path,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        test_path,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=False
    )

    return train_ds, val_ds, test_ds
