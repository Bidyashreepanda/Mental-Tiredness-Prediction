
import joblib
import pandas as pd
from pathlib import Path
from src.logger import logger

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "mental_tiredness_model.joblib"

model = joblib.load(MODEL_PATH)

logger.info("Mental Tiredness Model loaded successfully")

def predict_tiredness(input_data):
    try:
        input_df = pd.DataFrame([input_data])

        prediction = model.predict(input_df)

        result = float(prediction[0])

        logger.info("Prediction generated successfully")

        return result

    except Exception as e:
        logger.exception("Prediction failed: %s", e)
        raise
