import numpy as np
from sklearn.metrics import accuracy_score
import joblib

# Load the model
model = joblib.load('model.pkl')

# Generate some dummy test data
X_test, y_test = np.random.rand(20, 10), np.random.randint(0, 2, 20)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy}')
