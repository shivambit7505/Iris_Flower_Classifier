import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

def train_model():
    """Train and save the Iris classifier model"""
    # Load dataset
    iris = load_iris()
    x = iris.data
    y = iris.target
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Standardize features
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    
    # Train model
    model = LogisticRegression(max_iter=50)
    model.fit(X_train_s, y_train)
    
    # Evaluate model
    test_prediction = model.predict(X_test_s)
    accuracy = accuracy_score(y_test, test_prediction)
    conf_matrix = confusion_matrix(y_test, test_prediction)
    
    print("Accuracy Score:", accuracy)
    print("Confusion Matrix:\n", conf_matrix)
    
    # Save model and scaler
    with open('iris_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open('iris_scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print("Model and scaler saved successfully!")
    return model, scaler

def load_model():
    """Load the trained model and scaler"""
    try:
        with open('iris_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('iris_scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        return model, scaler
    except FileNotFoundError:
        print("Model files not found. Training new model...")
        return train_model()

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    """Predict iris species from measurements"""
    model, scaler = load_model()
    
    # Prepare user data
    user_data = [[sepal_length, sepal_width, petal_length, petal_width]]
    user_data_scaled = scaler.transform(user_data)
    
    # Make prediction
    prediction = model.predict(user_data_scaled)
    species_names = ["Setosa", "Versicolor", "Virginica"]
    
    return species_names[prediction[0]]

if __name__ == "__main__":
    train_model()
