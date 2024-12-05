import pandas as pd

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    # Example: Drop missing values and save
    data = data.dropna()
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data("data/raw/dataset.csv", "data/processed/preprocessed.csv")
