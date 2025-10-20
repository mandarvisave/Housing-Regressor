🏡 Housing Price Prediction (Machine Learning & Flask Deployment)

A complete end-to-end Machine Learning Regression Project that predicts house prices using multiple models and serves predictions through a Flask web application.

📌 Project Highlights

✅ Trained and compared 13 different regression models

✅ Saved the best-performing models using Pickle (.pkl)

✅ Created a Flask web app to take user input and predict house prices

✅ Displayed model evaluation metrics (MAE, MSE, R²) in a tabular format

✅ Used USA Housing Dataset

🛠 Tech Stack

| Category     | Tools Used                                                                                                                              |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Programming  | Python                                                                                                                                  |
| ML Models    | Linear Regression, Ridge, Lasso, ElasticNet, Polynomial, RandomForest, XGBoost, LightGBM, ANN, SVM, SGDRegressor, RobustRegression, KNN |
| Libraries    | Pandas, Scikit-learn, XGBoost, LightGBM, NumPy, Flask                                                                                   |
| Deployment   | Flask                                                                                                                                   |
| File Formats | `.pkl`, `.csv`, `.html`                                                                                                                 |


Project Structure 

📁 Housing-Price-Prediction

│
├── app.py                       # Flask App for UI & Prediction  
├── model.py                     # Model Training & Evaluation Script  
├── templates/    
│   ├── index.html               # Input Form for User  
│   ├── results.html             # Price Prediction Result Page  
│   ├── model.html               # Model Evaluation Table  
├── model_evaluation_results.csv # Performance metrics of models  
├── *.pkl                        # Saved trained models  
├── README.md                    # Project Documentation  


⚙️ How to Run the Project Locally
✅ 1. Clone the Repository
git clone https://github.com/your-username/housing-regressor.git
cd housing-regressor

✅ 2. Install Dependencies
pip install -r requirements.txt

✅ 3. Train Models (Optional)

If you want to retrain models:

python model.py

✅ 4. Run the Flask Web App
python app.py


Then open in browser:
http://127.0.0.1:5000/

📊 Model Evaluation Example

| Model             | MAE      | MSE       | R² Score        |
| ----------------- | -------- | --------- | --------------- |
| Linear Regression | 12345.67 | 567890123 | 0.91            |
| Random Forest     | 9876.54  | 432100987 | 0.94            |
| XGBoost           | 8765.43  | 345600789 | **0.95 (Best)** |

🚀 Future Improvements


✅ Add Docker & AWS deployment


✅ Add feature scaling & hyperparameter tuning


✅ Add Streamlit dashboard


✅ Use SHAP/Explainable AI for interpretation

🤝 Contributions

Feel free to fork this repo, raise issues, or submit pull requests!

⭐ Show Support

If you like this project, give it a ⭐ on GitHub — it helps a lot!
