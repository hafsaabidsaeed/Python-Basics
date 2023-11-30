import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
data = iris.data
columns = iris.feature_names
df = pd.DataFrame(data, columns=columns)

# Display the original dataset
print("Original Iris Dataset:")
print(df.head())

# Apply Min-Max Scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

# Create a new DataFrame with the scaled data
scaled_df = pd.DataFrame(scaled_data, columns=columns)

# Display the scaled dataset
print("\nScaled Iris Dataset:")
print(scaled_df.head())
