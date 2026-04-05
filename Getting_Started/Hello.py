# Import FastAPI
from fastapi import FastAPI

# Create Our App
app = FastAPI()

# Main Endpoint
@app.get('/')
# Endpoint Function
def Hi():
    return { "message": "Hello World !" }

# Test It: http://127.0.0.1:8000/

# Launch Our API
# $ python -m uvicorn Hello:app --reload
# python -m is like if we say run this module/package as a program
# uvicorn is our server that we use to start our API
# Hello is the name of our file
# app is our app that we just create it 
# --reload is an auto-refresh

# Creating New Endpoint
@app.get('/calculate_bmi')
def calculate_bmi(weight: float, height: float):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        message = 'You are underweight. Consider gaining weight with a balanced diet and proper nutrition.'
    elif 18.5 <= bmi < 25:
        message = 'You have a normal weight. Keep maintaining a healthy lifestyle.'
    elif 25 <= bmi < 30:
        message = 'You are overweight. Consider regular exercise and a balanced diet.'
    else:
        message = 'You are in the obese range. It s recommended to consult a healthcare professional and adopt a healthier lifestyle.'
        
    return {
        'bmi': bmi,
        'message': message
    }

# Test It: http://127.0.0.1:8000/calculate_bmi?weight=69&height=1.76