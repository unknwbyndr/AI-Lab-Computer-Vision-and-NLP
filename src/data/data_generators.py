# Create a data generator for training images
train_generator = train_datagen.flow_from_directory(
    directory=train_dir, 
    target_size=(img_size, img_size),  
    batch_size=64,  
    color_mode="grayscale",  
    class_mode="categorical",  
    subset="training"  
)

# Create a data generator for validation images
validation_generator = validation_datagen.flow_from_directory(
    directory=test_dir,  
    target_size=(img_size, img_size),  
    batch_size=64,  
    color_mode="grayscale",  
    class_mode="categorical",  
    subset="validation"  
)
