import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model(input_path, model_path):
    data = pd.read_csv(input_path)
    X = data[['feature1', 'feature2']]  # Replace with actual features
    y = data['target']
    
    model = LinearRegression()
    model.fit(X, y)
    
    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model("data/processed/preprocessed.csv", "models/model.pkl")
