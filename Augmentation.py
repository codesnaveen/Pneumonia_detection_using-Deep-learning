train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        '/content/drive/MyDrive/Colab Notebooks/chest_xray/chest_xray/train',
        target_size=(64, 64),
        batch_size=64,
        class_mode='binary')
validation_generator = test_datagen.flow_from_directory(
        '/content/drive/MyDrive/Colab Notebooks/chest_xray/chest_xray/test',
        target_size=(64, 64),
        batch_size=64,
        class_mode='binary')
