import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

def evaluate_model(input_path, model_path, result_path):
    data = pd.read_csv(input_path)
    X = data[['feature1', 'feature2']]  # Replace with actual features
    y = data['target']
    
    model = joblib.load(model_path)
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    
    with open(result_path, "w") as f:
        f.write(f"Mean Squared Error: {mse}\n")

if __name__ == "__main__":
    evaluate_model(
        "data/processed/preprocessed.csv",
        "models/model.pkl",
        "results/metrics.txt"
    )
