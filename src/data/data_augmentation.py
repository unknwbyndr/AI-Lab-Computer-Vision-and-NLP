# Data augmentation for training images to improve model generalization
train_datagen = ImageDataGenerator(
    # rotation_range = 180,  
    width_shift_range=0.1, 
    height_shift_range=0.1,  
    horizontal_flip=True, 
    rescale=1.0 / 255,
    # zoom_range = 0.2, 
    validation_split=0.2 
)

# Data preparation for validation images, only normalizing pixel values
validation_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2 
)
