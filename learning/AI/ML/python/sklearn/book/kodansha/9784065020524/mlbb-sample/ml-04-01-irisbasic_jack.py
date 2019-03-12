from sklearn import datasets
import numpy as np

iris = datasets.load_iris()

X = iris.data
Y = iris.target

# X = X[:, :2]
X = X[:, 2:]
print(X)

"""
print(Y)

print(X.shape)
print(Y.shape)

(n_samples, n_features) = X.shape
print('sample count : {0}'.format(n_samples))
print('feature dimention : {0}'.format(n_features))

n_classes = len(np.unique(Y))
print('class count : {0}'.format(n_classes))
"""