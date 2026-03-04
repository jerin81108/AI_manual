from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.33)

model = GaussianNB()
model.fit(x_train, y_train)

preds = model.predict(x_test)
acc = accuracy_score(y_test, preds)
cm = confusion_matrix(y_test, preds)
print("True labels:", y_test)
print("Predictions:", preds)
print(f"Accuracy: {acc:.2f}")
print("Confusion Matrix:\n", cm)