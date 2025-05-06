# 🚗 Vehicle Listings Dashboard

This is a **Streamlit-powered dashboard** that explores a dataset of used vehicle listings in the US.  
It allows users to visualize trends, distributions, and relationships in the data through interactive plots.

---

## 📌 Features

- Histogram of vehicle ages
- Scatter plot of price vs. odometer
- Data table toggle using a checkbox
- Interactive visuals using Plotly Express
- Easy deployment via Streamlit

---

## 📚 Technologies Used

- **Python 3**
- **Streamlit** for the web app framework
- **Pandas** for data handling
- **Plotly Express** for interactive visualizations

---

## 📂 Dataset

- File: `vehicles_us.csv`  
- Source: [Codecademy Datasets](https://github.com/Codecademy/datasets) or similar  
- Cleaned and used locally (not included in public repo due to size)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/project-5.git
cd project-5
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # or source venv/bin/activate on Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## 🌐 Live Application

You can view the deployed Streamlit dashboard here:  
➡️ [https://project-5-zgt0.onrender.com](https://project-5-zgt0.onrender.com)

## 📓 Exploratory Data Analysis

The `EDA.ipynb` notebook is included in the `notebooks/` folder and contains initial data exploration, histograms, and scatter plots used to build the dashboard.
