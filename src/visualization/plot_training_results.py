import matplotlib.pyplot as plt

# Extract training and validation accuracy and loss values from the history object
accuracy = history.history['accuracy']  
val_acc = history.history['val_accuracy']  
loss = history.history['loss']  
val_loss = history.history['val_loss']  

# Define the range for epochs (number of iterations)
epochs = range(len(accuracy))

# Plot training and validation accuracy
plt.plot(epochs, accuracy, 'r', label='Training accuracy')  
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')  
plt.title('Training and Validation Accuracy')  
plt.legend(loc=0)  
plt.figure()  

# Show the plot for accuracy
plt.show()

# Plot training and validation loss
plt.plot(epochs, loss, 'r', label='Training loss')  
plt.plot(epochs, val_loss, 'b', label='Validation loss')  
plt.title('Training and Validation Loss')  
plt.legend(loc=0)  

# Show the plot for loss
plt.show()
