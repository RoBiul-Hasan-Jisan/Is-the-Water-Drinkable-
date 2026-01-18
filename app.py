from flask import Flask, request, render_template
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)


model = joblib.load('water_model.pkl')

@app.route('/')
def home():
   
    mode = request.args.get('mode', 'safe')

    if mode == 'unsafe':
       
        defaults = {
            'ph': 9.97,
            'Hardness': 237.02,
            'Solids': 26944.68,
            'Chloramines': 5.59,
            'Sulfate': 334.33,
            'Conductivity': 379.14,
            'Organic_carbon': 13.01,
            'Trihalomethanes': 86.19,
            'Turbidity': 3.64
        }
        message = "Loaded Unsafe Water Data (True Negative Example)"
    else:
     
        defaults = {
            'ph': 7.8,
            'Hardness': 192.92,
            'Solids': 39234.47,
            'Chloramines': 8.86,
            'Sulfate': 236.00,
            'Conductivity': 463.44,
            'Organic_carbon': 19.63,
            'Trihalomethanes': 81.50,
            'Turbidity': 3.76
        }
        message = "Loaded Safe Water Data"

    return render_template('index.html', form_data=defaults, load_msg=message)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Get data
        features = {
            'ph': float(request.form['ph']),
            'Hardness': float(request.form['Hardness']),
            'Solids': float(request.form['Solids']),
            'Chloramines': float(request.form['Chloramines']),
            'Sulfate': float(request.form['Sulfate']),
            'Conductivity': float(request.form['Conductivity']),
            'Organic_carbon': float(request.form['Organic_carbon']),
            'Trihalomethanes': float(request.form['Trihalomethanes']),
            'Turbidity': float(request.form['Turbidity'])
        }

       
        data = pd.DataFrame([features])
        ph_val = features['ph']
        data['ph_show_acidic'] = 1 if ph_val < 6.5 else 0
        data['ph_show_neutral'] = 1 if 6.5 <= ph_val <= 7.5 else 0
        data['ph_show_alkaline'] = 1 if ph_val > 7.5 else 0

      
        try:
            if hasattr(model, 'feature_names_in_'):
                required_cols = model.feature_names_in_
            elif hasattr(model, 'named_steps'):
                required_cols = model.named_steps['classifier'].feature_names_in_
            else:
                required_cols = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
                                 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']
            final_data = data[required_cols]
        except:
            final_data = data[['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 
                               'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']]

   
        prediction = model.predict(final_data)[0]
        
        if prediction == 1:
            res_text = " POTABLE (Safe to Drink)"
            color = "green"
        else:
            res_text = " NOT POTABLE (Unsafe)"
            color = "red"

        return render_template('index.html', prediction_text=res_text, color=color, form_data=features)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", color="black", form_data=request.form)

if __name__ == "__main__":
    app.run(debug=True)