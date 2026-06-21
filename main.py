from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix

iris=load_iris()
x=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42,stratify=y)

scaler=StandardScaler()
X_train_s=scaler.fit_transform(X_train)
X_test_s=scaler.transform(X_test)

model=LogisticRegression(max_iter=50)
model.fit(X_train_s,y_train)

test_prediction=model.predict(X_test_s)

print("Accuracy Score:-",accuracy_score(y_test,test_prediction))
print(confusion_matrix(y_test,test_prediction))