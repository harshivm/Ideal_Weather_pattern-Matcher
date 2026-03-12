import pandas as pd

def load_csv(path):

    try:
        df = pd.read_csv(path)
        print(f"[INFO] Loaded {path} shape={df.shape}")
        return df

    except Exception as e:
        print(f"[ERROR] Could not load {path}: {e}")
        return None


def load_all_data():

    training = load_csv("../data/weather_training_data.csv")

    ideal = load_csv("../data/weather_ideal_patterns.csv")

    test = load_csv("../data/weather_test_data.csv")

    return training, ideal, test