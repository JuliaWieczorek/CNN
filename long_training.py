#long training
#8.

exec(open("settings.py").read())
exec(open("functions.py").read())
exec(open("sample_images.py").read())
exec(open("model.py").read())
exec(open("model_analysis.py").read())
exec(open("init_training.py").read())

epochs = 10

cpf = last_ckpt(ckpt_dir)
if cpf != "":
  print("Loading starting weights from \n\t{0}".format(cpf))
  model.load_weights(cpf)

# Fit the model on the batches generated by datagen.flow().
hist = model.fit_generator(datagen.flow(x_train, y_train,
    batch_size=batch_size,shuffle=True),
    steps_per_epoch=x_train.shape[0] // batch_size,
    epochs=epochs,verbose=2,
    validation_data=(x_test, y_test),
    workers=4, callbacks=[checkpoint,stahp])

# Save model and weights
model.save(model_path)
print('Saved trained model at %s ' % model_path)

with open(hist_path, 'wb') as f:
  pickle.dump(hist.history, f)
#long training, dwa zapisane modele