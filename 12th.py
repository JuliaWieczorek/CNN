import matplotlib.pyplot as plt

with open(, 'rb') as f:
  hist = pickle.load(f)

key2name = {'acc':'Accuracy', 'loss':'Loss',
    'val_acc':'Validation Accuracy', 'val_loss':'Validation Loss'}

fig = plt.figure()

things = ['acc','loss','val_acc','val_loss']
for i,thing in enumerate(things):
  trace = hist[thing]
  plt.subplot(2,2,i+1)
  plt.plot(range(len(trace)),trace)
  plt.title(key2name[thing])

fig.set_tight_layout(True)
fig
#wykresy