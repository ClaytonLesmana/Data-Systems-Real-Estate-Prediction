from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__, template_folder='Pages')

# Load your trained model
model = joblib.load('final_model.pkl')

# Homepage


@app.route('/')
def home():
    return render_template('home.html')

# Contact Page


@app.route('/contact')
def contact():
    return render_template('contact.html')

# Map Page


@app.route('/map')
def map():
    return render_template('map.html')

# Prediction Page


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET':
        return render_template('prediction.html')
    elif request.method == 'POST':
        try:
            # Extract data from POST request
            data = request.get_json()
            print("Received data:", data)  # Output to console for debugging
            # Assuming data is in the form { 'feature1': value1, 'feature2': value2, ... }
            prediction = model.predict([list(data.values())])
            # Return the prediction
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
