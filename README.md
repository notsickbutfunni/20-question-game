# 🎮 20 Questions Game (Decision Tree + Flask)

An interactive **web app** inspired by the classic “20 Questions” game — built using a **Decision Tree algorithm** to predict **anime characters** based on **yes/no answers**.

---

## 🧩 Overview

This project combines **Machine Learning** and **Web Development** to create a fun, explainable AI experience.  
The model is trained to classify anime characters using their traits, and the web interface guides the user through a sequence of questions until it makes a prediction.

---

## 🚀 Features

- 🧠 **Decision Tree Classifier** trained on anime character traits  
- 🌐 **Flask Web App** with simple and interactive UI  
- 💾 **Model Persistence** using `pickle` (`model.pkl`)  
- 🧰 Built entirely in **Python**

---

## Project structure
```
20q-game/
├── app.py 
├── model.ipynb #just training and testing
├── model.pkl 
├──dataset/
    └── data.csv #trained data
    └── anime_traits_better.csv #original data from kaggle
    └── output.png #visualization of trained model
└── templates/
    └── index.html 
```
---

## ⚙️ How It Works

1. The **Decision Tree** model is trained in `model.ipynb` using anime character traits.  
2. The trained model is exported as `model.pkl`.  
3. The **Flask app** (`app.py`) loads this model and serves a simple yes/no interface.  
4. User answers are processed, and the model predicts the most likely anime character.

---

## 💻 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/inkarkairatkyzy/20q-game.git
   cd 20q-game
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the Flask app** 
   ```bash
   python app.py
5.Open your browser and go to 
     👉 http://127.0.0.1:5000


