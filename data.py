import pandas as pd

# Define a simple dataset with features and a target
data = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [10, 20, 30, 40, 50],
    "target": [0, 1, 0, 1, 0],
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("data/raw/dataset.csv", index=False)

print("Sample dataset has been created and saved to 'data/raw/dataset.csv'")
