model.fit(
        train_generator,
        steps_per_epoch=82,
        epochs=20,
        validation_data=validation_generator,
        validation_steps=82)
