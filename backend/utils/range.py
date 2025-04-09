import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(BASE_DIR, "Data", "Fertilizer.csv")
fertilizer_data = pd.read_csv(CSV_PATH)


def range():
    nitrogen_range = {
        "low": fertilizer_data["N"].quantile(0.33),
        "medium": fertilizer_data["N"].quantile(0.66),
        "high": fertilizer_data["N"].max(),
    }
    phosphorous_range = {
        "low": fertilizer_data["P"].quantile(0.33),
        "medium": fertilizer_data["P"].quantile(0.66),
        "high": fertilizer_data["P"].max(),
    }
    potassium_range = {
        "low": fertilizer_data["K"].quantile(0.33),
        "medium": fertilizer_data["K"].quantile(0.66),
        "high": fertilizer_data["K"].max(),
    }
    ph_values = {
        "acidic": 5.5,
        "neutral": 6.5,
        "alkaline": 7.5,
    }
    return (
        nitrogen_range,
        phosphorous_range,
        potassium_range,
        ph_values,
    )
