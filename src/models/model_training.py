# Define the path to save or load the model
model_path = '/kaggle/working/model_fer2013.h5'

if os.path.exists(model_path):
    print("Loading pre-trained model...")
    model = tf.keras.models.load_model(model_path)
else:
    print("Training a new model from scratch...")
    
    # Compile the model (ensures it's ready for training)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    history = model.fit(x=train_generator,
                        epochs=100,
                        validation_data=validation_generator)

    # Save the trained model
    model.save(model_path)
    print(f"Model trained and saved at {model_path}")
