import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import (LinearRegression,Ridge,Lasso, ElasticNet, SGDRegressor)
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import HuberRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline #data Leakages
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
import lightgbm as lgb
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle

#Load Dataset
data = pd.read_csv(r"D:\Naresh IT FSDS Prakash Senapathi 7 PM\VSCODE\CAPSTONE PROJECT\HOUSING Regressor\data\USA_Housing.csv")

#Preprocessing
X = data.drop(['Price','Address'], axis=1)
y = data['Price']

#Split the data
X_train, X_teest, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Define Models
models= {
    'LinearRegression': LinearRegression(),
    'RidgeRegression': Ridge(),
    'RobustRegression': HuberRegressor(),
    'LassoRegression': Lasso(),
    'ElasticNet': ElasticNet(),
    'PolynomialRegression': Pipeline([
        ('poly', PolynomialFeatures(degree=4)),
        ('lin', LinearRegression())
    ]),
    'SGDRegressor': SGDRegressor(),
    'ANN': MLPRegressor(hidden_layer_sizes=(100,), max_iter=1000),
    'RandomForest': RandomForestRegressor(),
    'SVM': SVR(),
    'LGBM': lgb.LGBMRegressor(),
    'XGBoost': xgb.XGBRegressor(),
    'KNN': KNeighborsRegressor()
}