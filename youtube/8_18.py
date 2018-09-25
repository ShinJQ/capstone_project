from matplotlib import pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import mglearn
cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(cancer.data,cancer.target, random_state=1)

print(X_train.shape())
print(X_test.shape())

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=50, centers=5, random_state=4, cluster_std=2)

X_train, X_test=train_test_split(X, random_state=5, test_size=1)

fig, axes = plt.subplots(1,3,figsize=(13,4))
axes[0].scatter(X_train[:,0], X_train[:,1], c=mglearn.cm2(0), lavel = "훈련 세트", s=60)
axes[0].scatter(X_train[:,0], X_train[:,1],marker="^", c=mglearn.cm2(1), lavel = "테스트 세트", s=60)
axes[0].legend(loc='upper_left')


