img = np.expand_dims(img, axis=0)  # The shape becomes (1, 48, 48) - adding the batch dimension

img = img.reshape(1, 48, 48, 1)  # The shape becomes (1, 48, 48, 1)

result = model.predict(img)

# Convert the result 
result = list(result[0])

print(result)
