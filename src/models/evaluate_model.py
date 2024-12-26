# Evaluate the model on the training data
train_loss, train_acc = model.evaluate(train_generator)  

# Evaluate the model on the validation (test) data
test_loss, test_acc = model.evaluate(validation_generator) 

# Print the final training and validation accuracies as percentages
print("Final training accuracy = {:.2f}%, validation accuracy = {:.2f}%".format(train_acc * 100, test_acc * 100))
