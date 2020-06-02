import tensorflow,keras

sess = keras.backend.get_session()

model = keras.models.load_model()
_,_,_,_,labels = setup_load_cifar()

img = tensorflow.read_file()
img = tensorflow.image.decode_jpeg(img, channels=3)
img.set_shape([None, None, 3])
img = tensorflow.image.resize_images(img, (32, 32))
img = img.eval(session=sess) # convert to numpy array
img = np.expand_dims(img, 0) # make 'batch' of 1

pred = model.predict(img)
pred = labels["label_names"][np.argmax(pred)]
pred

#'cat'