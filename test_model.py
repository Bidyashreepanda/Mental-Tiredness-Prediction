
import joblib
from pathlib import Path

# Specify the model path
model_path = Path("mental_tiredness_model (2).joblib")

if model_path.exists():

    print("Model found at:", model_path.resolve())

    model = joblib.load(model_path)

    print("\nModel loaded successfully!")
    print("Model type:", type(model))

    print("\nPipeline details:")
    print(model)

else:
    print("Model not found!")
    print("Check the model filename and location.")
