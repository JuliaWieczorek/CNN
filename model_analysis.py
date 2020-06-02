#6.

exec(open("model.py").read())

from keras.utils import plot_model

plot_model(model, to_file="C:/Users/julia/Documents/bioinformatyka/mgr/CNN/results/model.svg",
           show_layer_names=True, show_shapes=True, rankdir="TB")
print(model.summary())

#wydruk modelu-> model ananlysis