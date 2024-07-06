import os
import shutil

# Define the deployment directory
deployment_dir = 'deployment/'

# Create the deployment directory if it doesn't exist
os.makedirs(deployment_dir, exist_ok=True)

# Copy the model to the deployment directory
shutil.copy('model.pkl', deployment_dir)
print('Model deployed successfully.')

