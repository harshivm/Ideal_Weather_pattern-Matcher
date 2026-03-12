import pandas as pd
import numpy as np
import os

# create folders if missing
os.makedirs("../data", exist_ok=True)

# -----------------------------
# LOAD KAGGLE DATASETS
# -----------------------------

global_weather = pd.read_csv("../kaggle_raw_data/GlobalWeatherRepository.csv")

climate = pd.read_csv("../kaggle_raw_data/DailyDelhiClimateTest.csv")

forecast = pd.read_csv("../kaggle_raw_data/weather_forecast_data.csv")


# -----------------------------
# CREATE TRAINING DATASET
# -----------------------------

training = pd.DataFrame()

training["x"] = range(len(global_weather))

training["temperature_pattern"] = global_weather["temperature_celsius"].fillna(method="ffill")

training["humidity_pattern"] = global_weather["humidity"].fillna(method="ffill")

training["pressure_pattern"] = global_weather["pressure_mb"].fillna(method="ffill")

training["wind_pattern"] = global_weather["wind_kph"].fillna(method="ffill")

training.to_csv("../data/weather_training_data.csv", index=False)


# -----------------------------
# CREATE IDEAL PATTERNS
# -----------------------------

x = np.arange(-20, 20, 0.5)

ideal = {"x": x}

for i in range(1, 51):

    if i % 4 == 0:
        ideal[f"ideal{i}"] = 20 + 10*np.sin(x/(i/5))

    elif i % 4 == 1:
        ideal[f"ideal{i}"] = 60 + 15*np.cos(x/(i/6))

    elif i % 4 == 2:
        ideal[f"ideal{i}"] = 1010 + 5*np.sin(x/(i/8))

    else:
        ideal[f"ideal{i}"] = 8 + 2*np.cos(x/(i/7))


ideal_df = pd.DataFrame(ideal)

ideal_df.to_csv("../data/weather_ideal_patterns.csv", index=False)


# -----------------------------
# CREATE TEST DATASET
# -----------------------------

test = pd.DataFrame()

test["x"] = range(len(forecast))

test["observed_weather"] = forecast["Temperature"].fillna(method="ffill")

test.to_csv("../data/weather_test_data.csv", index=False)


print("Datasets created successfully.")