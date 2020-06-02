num_predictions = 36

model = load_model()

predict_gen = model.predict_generator(datagen.flow(x_test, y_test,
    batch_size=batch_size, shuffle=False),
    steps=(x_test.shape[0] // batch_size)+1, workers=4)

indices = [np.random.choice(range(len(x_test)))
           for i in range(num_predictions)]

cifar_grid(x_test,y_test,indices,6,labels,predictions=predict_gen)
#zdjęcia