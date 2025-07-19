from flask import Flask, render_template
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')  

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    return "POST request received"

if __name__ == '__main__':
    app.run(port=3000, debug =True)