import shutil

# Simulate deployment by copying the model to a deployment directory
shutil.copy('model.pkl', '/path/to/deployment/directory/')
print('Model deployed successfully.')

