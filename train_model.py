import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
df = pd.read_csv("Hyderbad_House_price.csv")
# Clean columns
df.columns = df.columns.str.strip()

# Clean numeric columns
df["rate_persqft"] = df["rate_persqft"].astype(str).str.strip().astype(float)
df["area_insqft"] = df["area_insqft"].astype(str).str.strip().astype(float)

# Remove duplicates
df.drop_duplicates(inplace=True)

# One hot encoding
df = pd.get_dummies(df)

# Features and target
X = df.drop("price(L)", axis=1)
y = df["price(L)"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor()

model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully")