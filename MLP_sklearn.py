from sklearn.datasets import fetch_openml
import numpy as np

X, y = fetch_openml('mnist_784', version=1, return_X_y=True)

import matplotlib.pyplot as plt
plt.gray()
plt.imshow(np.reshape(np.array(X)[0,:],(28,28)))
plt.show()

from sklearn.model_selection import train_test_split
X = X / 255.
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True,
test_size=0.2)
# X_train, X_test = X[:60000], X[60000:]
# y_train, y_test = y[:60000], y[60000:]

print(np.shape(X_train))

from sklearn.neural_network import MLPClassifier
# Définition du modèle
mlp = MLPClassifier(hidden_layer_sizes=(50, ), max_iter=10, solver='sgd', verbose=10, learning_rate_init=.1)
# Entrainement
model_final = mlp.fit(X_train, y_train)

print(f"Score sur les données d'entrainement : {mlp.score(X_train, y_train):.3f}")
print(f"Score sur les données de test : {mlp.score(X_test, y_test):.3f}")


exemple_test_x = np.array(X_test[:1])
exemple_test_y = np.array(y_test[:1])
plt.gray()
plt.imshow(exemple_test_x.reshape((28,28)))
plt.show()
print(f"Prediction : {mlp.predict(exemple_test_x)}")
print(f"Sortie : {exemple_test_y}")
