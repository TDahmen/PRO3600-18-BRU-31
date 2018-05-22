import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = np.load("newGamesData.npy")[0:10000]
labels = np.load("newOneHotEncoded.npy")[0:10000]

y = np.argmax(labels, axis=1)
X = data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify=y)

knn = KNeighborsClassifier(n_neighbors=4)

knn.fit(X_train, y_train)

def predict_class_knn(plateau):
    return knn.predict(plateau[0:1])[0]

# print(knn.predict(np.load("newGamesData.npy")[20001:20010]))
# print(np.load("newOneHotEncoded.npy")[20001:20010])
