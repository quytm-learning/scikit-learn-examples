import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

# # just for test
# print('data:')
# print(digits.data)
# print('target:')
# print(digits.target)
# print('image[0]:')
# print(digits.images[0])
print(len(digits.data))

clf = svm.SVC(gamma=0.001, C=100)

# Get latest item => will test it
x, y = digits.data[:-10], digits.target[:-10]
clf.fit(x, y)

index = 1734
test = digits.data[index].reshape(1, -1)
print('Prediction: ', clf.predict(test))

plt.imshow(digits.images[index], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
