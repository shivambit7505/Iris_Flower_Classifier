const API_URL = 'http://localhost:5000/api';

// Get form and elements
const form = document.getElementById('predictionForm');
const resultSection = document.getElementById('resultSection');
const errorSection = document.getElementById('errorSection');
const resultContent = document.getElementById('resultContent');
const errorMessage = document.getElementById('errorMessage');
const submitBtn = form.querySelector('button');

// Form submission
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Hide previous results
    resultSection.style.display = 'none';
    errorSection.style.display = 'none';
    
    // Get form data
    const formData = new FormData(form);
    const data = {
        sepal_length: parseFloat(formData.get('sepal_length')),
        sepal_width: parseFloat(formData.get('sepal_width')),
        petal_length: parseFloat(formData.get('petal_length')),
        petal_width: parseFloat(formData.get('petal_width'))
    };
    
    // Validate input ranges
    if (!validateInput(data)) {
        showError('Please enter valid measurements within the expected ranges.');
        return;
    }
    
    // Disable submit button
    submitBtn.disabled = true;
    submitBtn.textContent = 'Classifying...';
    
    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok && result.success) {
            showResult(result.species, data);
        } else {
            showError(result.error || 'Failed to classify flower');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('Unable to connect to the server. Make sure the backend is running.');
    } finally {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Classify';
    }
});

function validateInput(data) {
    // Typical iris dataset ranges
    const ranges = {
        sepal_length: { min: 4.0, max: 8.0 },
        sepal_width: { min: 1.5, max: 4.5 },
        petal_length: { min: 0.5, max: 7.0 },
        petal_width: { min: 0.1, max: 2.5 }
    };
    
    for (const [key, range] of Object.entries(ranges)) {
        if (data[key] < range.min || data[key] > range.max) {
            console.warn(`${key} is outside typical range: ${range.min} - ${range.max}`);
        }
    }
    
    return Object.values(data).every(v => v > 0);
}

function showResult(species, measurements) {
    resultContent.innerHTML = `
        <div class="result-species">
            🌸 ${species}
        </div>
        <div class="result-details">
            <p><strong>Measurements:</strong></p>
            <ul>
                <li>Sepal Length: ${measurements.sepal_length.toFixed(1)} cm</li>
                <li>Sepal Width: ${measurements.sepal_width.toFixed(1)} cm</li>
                <li>Petal Length: ${measurements.petal_length.toFixed(1)} cm</li>
                <li>Petal Width: ${measurements.petal_width.toFixed(1)} cm</li>
            </ul>
            <p style="margin-top: 15px;"><strong>Predicted Species:</strong> ${getSpeciesDescription(species)}</p>
        </div>
    `;
    resultSection.style.display = 'block';
    resultSection.scrollIntoView({ behavior: 'smooth' });
}

function showError(message) {
    errorMessage.textContent = message;
    errorSection.style.display = 'block';
    errorSection.scrollIntoView({ behavior: 'smooth' });
}

function getSpeciesDescription(species) {
    const descriptions = {
        'Setosa': 'A smaller iris species with shorter petals, typically found in rocky areas.',
        'Versicolor': 'A medium-sized iris with medium-length petals, commonly found in moist areas.',
        'Virginica': 'The largest iris species with long petals, known for its beauty and elegance.'
    };
    
    return descriptions[species] || 'Unknown species';
}

// Check API health on page load
document.addEventListener('DOMContentLoaded', () => {
    checkAPIHealth();
});

async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_URL}/health`);
        if (!response.ok) {
            console.warn('Backend API is not responding');
        }
    } catch (error) {
        console.error('Backend API is not accessible:', error);
    }
}
