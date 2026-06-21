# Iris Flower Classifier - Full Stack Application

A complete machine learning application with frontend and backend for classifying iris flowers into Setosa, Versicolor, or Virginica species based on sepal and petal measurements.

## Project Structure

```
Iris_Flower_Classifier/
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── style.css           # Styling
│   └── script.js           # Client-side logic
├── backend/
│   ├── app.py              # Flask API server
│   ├── model.py            # ML model and training
│   └── requirements.txt    # Backend dependencies
├── main.py                 # Original standalone script
├── main.ipynb              # Original Jupyter notebook
├── README.md               # This file
└── requirements.txt        # Overall project dependencies
```

## Features

- **Machine Learning Model**: Logistic Regression classifier trained on the Iris dataset
- **REST API**: Flask backend with endpoints for prediction and model training
- **Modern Web UI**: Responsive frontend with beautiful design
- **Model Persistence**: Trained models are saved and loaded efficiently
- **CORS Support**: Allows cross-origin requests for frontend-backend communication

## Backend

### Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train the model (optional - will auto-train on first run):
```bash
python model.py
```

### Running the Backend

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### API Endpoints

- **POST `/api/predict`** - Classify an iris flower
  ```json
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }
  ```

- **POST `/api/train`** - Retrain the model

- **GET `/api/health`** - Health check

## Frontend

### Setup

The frontend is a pure HTML/CSS/JavaScript application - no build step required!

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Open `index.html` in your web browser or use a local server:
```bash
# Using Python
python -m http.server 8000

# Using Node.js http-server (if installed)
http-server
```

3. Access the application at `http://localhost:8000` (or the port shown)

## Running the Full Application

### Terminal 1: Start the Backend
```bash
cd backend
python app.py
```

### Terminal 2: Start the Frontend
```bash
cd frontend
python -m http.server 8000
```

Then open your browser to `http://localhost:8000`

## Model Information

- **Algorithm**: Logistic Regression
- **Training Data**: Iris Dataset (150 samples)
- **Features**: 4 (Sepal Length, Sepal Width, Petal Length, Petal Width)
- **Classes**: 3 (Setosa, Versicolor, Virginica)
- **Preprocessing**: StandardScaler normalization

## Typical Iris Measurements (in cm)

### Setosa
- Sepal Length: 4.3 - 5.8
- Sepal Width: 2.3 - 4.4
- Petal Length: 1.0 - 1.9
- Petal Width: 0.1 - 0.6

### Versicolor
- Sepal Length: 4.9 - 7.0
- Sepal Width: 2.0 - 3.4
- Petal Length: 3.0 - 5.1
- Petal Width: 1.0 - 1.8

### Virginica
- Sepal Length: 4.9 - 7.9
- Sepal Width: 2.2 - 3.8
- Petal Length: 4.5 - 6.9
- Petal Width: 1.4 - 2.5

## Original Files

- `main.py` - Standalone training and evaluation script
- `main.ipynb` - Jupyter notebook with interactive training and prediction

## Dependencies

### Backend
- flask
- flask-cors
- scikit-learn
- numpy

### Frontend
- No external dependencies (vanilla JavaScript)
