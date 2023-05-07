import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import precision_score, recall_score, accuracy_score

X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

#a
plt.scatter(X_train[:, 0], X_train[:, 1], marker="o", c=y_train, s=10, cmap='plasma')
plt.scatter(X_test[:, 0], X_test[:, 1], marker="x", c=y_test, s=15, cmap='plasma')
plt.show()

#b
LogRegression_model = LogisticRegression()
LogRegression_model.fit(X_train, y_train)

#c
theta0 = LogRegression_model.intercept_
coefs = LogRegression_model.coef_.T
a = -coefs[0]/coefs[1]
b = -theta0/coefs[1]
xy_min, xy_max = -4, 4
x1 = np.array([xy_min, xy_max])
y1 = a*x1 + b
plt.plot(x1, y1, linestyle='--',label='Granica odluke')
plt.scatter(X_train[:, 0], X_train[:, 1], marker="o", c=y_train, s=10, cmap='plasma')
plt.show()


#d
y_test_p = LogRegression_model.predict(X_test)

cm = confusion_matrix(y_test, y_test_p)
print("Matrica zabune:", cm)
cm_disp = ConfusionMatrixDisplay(cm)
cm_disp.plot()
plt.show()

print('Točnost:', round(accuracy_score(y_test, y_test_p), 2))
print('Preciznost:', round(precision_score(y_test, y_test_p), 2))
print('Odziv:', round(recall_score(y_test, y_test_p), 2))

#e
y_color = (y_test == y_test_p)
plt.scatter(X_test[:, 0], X_test[:, 1], marker="o", c=y_color, s=15, cmap=mcolors.ListedColormap(["black", "green"]))
plt.show()
print(y_color)
