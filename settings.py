#1.
#settings.py

batch_size = 128
num_classes = 10
epochs_shortrun = 5
epochs_longrun = 500
random_seed = 343

save_dir = "C:/Users/julia/Documents/bioinformatyka/mgr/CNN/work"
res_dir = "C:/Users/julia/Documents/bioinformatyka/mgr/CNN/results"
model_name = "C:/Users/julia/Documents/bioinformatyka/mgr/CNN/convnet_cifar10"

# setup paths
import os

ckpt_dir = os.path.join(save_dir,"checkpoints")
if not os.path.isdir(ckpt_dir):
    os.makedirs(ckpt_dir)

### moje
if not os.path.isdir(res_dir):
    os.makedirs(os.path.join(res_dir))

if not os.path.isdir(model_name):
    os.makedirs(os.path.join(model_name))

model_path = os.path.join(res_dir, model_name + ".kerasave")
hist_path = os.path.join(res_dir, model_name + ".kerashist")