import pandas as pd
import numpy as np


def assign_weather_patterns(test_df, ideal_df, training_df, best_matches):

    results = []

    for _, row in test_df.iterrows():

        x_val = row["x"]

        observed = row["observed_weather"]

        best_fit = None

        smallest_dev = float("inf")

        for train_col, ideal_col in best_matches.items():

            delta = np.max(
                np.abs(training_df[train_col] - ideal_df[ideal_col])
            )

            try:

                ideal_value = ideal_df.loc[
                    ideal_df["x"] == x_val,
                    ideal_col
                ].values[0]

            except IndexError:

                continue

            deviation = abs(observed - ideal_value)

            if deviation <= np.sqrt(2) * delta:

                if deviation < smallest_dev:

                    smallest_dev = deviation

                    best_fit = {

                        "x": x_val,

                        "observed_weather": observed,

                        "deviation": deviation,

                        "ideal_pattern": ideal_col

                    }

        if best_fit:

            results.append(best_fit)

    return pd.DataFrame(results)