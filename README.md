# Customer Churn Prediction App

A interactive web application built with **Streamlit** and **TensorFlow/Keras** to predict whether a customer is likely to churn (leave the bank) based on their demographics and financial indicators.

## 🚀 Features
* **Deep Learning Model**: Utilizes an Artificial Neural Network (ANN) trained on bank customer churn data.
* **Streamlit Web UI**: Easy-to-use sliders and dropdown inputs to simulate customer profiles.
* **Immediate Prediction**: Calculates and displays churn probability in real time.

---

## 🛠️ Setup and Installation

### 1. Requirements
Ensure you have Python 3.11 or 3.13 installed. Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 2. How to Run Locally

#### Option A: Running from the VS Code Play Button
We have added a custom launch bootstrapper at the top of `app.py`. Simply open `app.py` in VS Code and click the **Run / Play** button. It will launch Streamlit automatically and open your browser to:
`http://localhost:8501`

#### Option B: Terminal Command
Alternatively, run the app using the Streamlit command line:
```bash
streamlit run app.py
```

---

## ⚡ Deployment & Dependency Resolution

During Streamlit Community Cloud deployment, we resolved a critical dependency conflict:
* **Conflict**: Older `tensorflow==2.12.0` required `numpy>=1.22,<1.24`, which conflicted with `numpy==1.26.4`.
* **Resolution**: Removed strict version pinning in `requirements.txt` to allow the package manager (`uv` / `pip`) to resolve the latest compatible versions of TensorFlow and NumPy.

The file loading paths were also made robust to support execution from any directory context without causing `FileNotFoundError`.
