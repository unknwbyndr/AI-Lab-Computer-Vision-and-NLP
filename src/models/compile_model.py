# Initialize the Adam optimizer with a learning rate of 0.0001
optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)

# Compile the model with the chosen optimizer, loss function, and evaluation metric
model.compile(
    optimizer=optimizer, 
    loss='categorical_crossentropy',  
    metrics=['accuracy']  
)

# Display the summary of the model architecture
model.summary()
