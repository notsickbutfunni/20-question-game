from flask import Flask, render_template
import joblib
import pandas as pd
import json
from sklearn.tree import DecisionTreeClassifier, export_text

app = Flask(__name__)

model = joblib.load('model.pkl') 
df = pd.read_csv(r"C:\Users\kaira\DTree\dataset\data.csv")
X = df.drop(columns=['Names'], axis=1)
y = df['Names']

clf = DecisionTreeClassifier(max_depth=None)
clf.fit(X, y)

feature_names = list(X.columns)
tree_text = export_text(model, feature_names=feature_names)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=3000, debug =True)