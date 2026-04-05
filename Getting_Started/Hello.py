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