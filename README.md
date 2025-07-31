# Diabetes_Prediction
Diabetes Prediction App
A machine learning-powered web application that predicts the likelihood of diabetes based on health parameters.

<img width="511" height="696" alt="image" src="https://github.com/user-attachments/assets/7b6c3504-ae3b-49f7-8008-53e543507ab3" />


📌 Features
Predicts diabetes risk based on key health metrics

Simple, user-friendly interface

Fast and 90% accurate predictions

Built with Streamlit

� Key Input Variables
The model uses the following health parameters for prediction:

Variable	Description	Normal Range
Pregnancies	Number of pregnancies (0 if not applicable)	0 - 5
Glucose	Plasma glucose concentration (mg/dL)	70 - 140 mg/dL (fasting)
BloodPressure	Diastolic blood pressure (mm Hg)	< 80 mm Hg
SkinThickness	Triceps skinfold thickness (mm) – measures body fat	10 - 40 mm
Insulin	2-hour serum insulin level (μU/mL)	2 - 25 μU/mL
BMI	Body Mass Index (kg/m²)	18.5 - 24.9
DiabetesPedigreeFunction	Genetic diabetes likelihood score	0.08 - 2.42
Age	Age in years	–



⚙️ Installation
Clone the repository:

bash
git clone https://github.com/your-username/diabetes-prediction.git
Navigate to the project folder:

bash
cd diabetes-prediction
Install dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py  # or `python app.py` if using Flask
Open http://localhost:8501 in your browser.

🤖 Model Details
Algorithm: Random Forest

Accuracy: 66%
Precision 70% and 51%


Dataset: Pima Indians Diabetes Dataset (https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

📂 Project Structure
text
diabetes-prediction/
├── app.py                # Main application script
├── model.pkl             # Trained ML model
├── requirements.txt      # Python dependencies
├── data/                 # Dataset (if included)
├── notebooks/            # EDA & model training notebooks
└── README.md             # This file
🛠 How to Contribute
Fork the repository

Create a new branch (git checkout -b feature/new-improvement)

Commit changes (git commit -m "Added new feature")

Push to branch (git push origin feature/new-improvement)

Open a Pull Request
