import numpy as np
import CNN.utils as utils

m = 50000
img_dim = 28

X = utils.extract_data('train-images-idx3-ubyte.gz', m, img_dim)
print(X.shape)

X -= int(np.mean(X))
X /= int(np.std(X))

# y_dash = utils.extract_labels('train-labels-idx1-ubyte.gz', m).reshape(m, 1)
# train_data = np.hstack((X, y_dash))

# np.random.shuffle(train_data)
