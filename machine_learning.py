import numpy
import scipy
import sklearn
import matplotlib
import pandas

from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
print (X)
print("yyyyy")
print (y)