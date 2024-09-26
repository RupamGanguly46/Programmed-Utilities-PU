from sklearn.datasets import load_iris
import pandas as pd

# Load dataset and convert to DataFrame
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df.head())

from sklearn.model_selection import train_test_split

X = df.iloc[:, :-1]  # Features (input)
y = df.iloc[:, -1]   # Target (output)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.neighbors import KNeighborsClassifier

# Initialize KNN classifier and train
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

# Predict and calculate accuracy
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

from sklearn.model_selection import cross_val_score

# Perform 5-fold cross-validation
scores = cross_val_score(knn, X, y, cv=5)
print(f"Cross-Validation Scores: {scores}")
print(f"Mean Accuracy: {scores.mean():.2f}")

neighbors = range(1, 11)
accuracies = []

for n in neighbors:
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(X_train, y_train)
    accuracies.append(knn.score(X_test, y_test))

print(accuracies)
