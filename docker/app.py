from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hallo DevNet student! Ik draai in een container."

if __name__ == '__main__':
    # Luister op alle netwerkinterfaces (belangrijk voor Docker!)
    app.run(host='0.0.0.0', port=5000)