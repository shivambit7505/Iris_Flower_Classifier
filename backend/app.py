from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_iris, train_model, load_model
import os

app = Flask(__name__)
CORS(app)

# Initialize model on startup
@app.before_request
def initialize():
    """Initialize model on first request"""
    if not os.path.exists('iris_model.pkl'):
        print("Training model...")
        train_model()
    else:
        print("Loading existing model...")
        load_model()

@app.route('/api/predict', methods=['POST'])
def predict():
    """API endpoint for iris prediction"""
    try:
        data = request.get_json()
        
        # Validate input
        required_fields = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Make prediction
        species = predict_iris(
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        )
        
        return jsonify({
            'species': species,
            'success': True
        }), 200
    
    except ValueError:
        return jsonify({'error': 'Invalid input values'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/train', methods=['POST'])
def train():
    """API endpoint to retrain the model"""
    try:
        train_model()
        return jsonify({
            'message': 'Model trained successfully',
            'success': True
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
