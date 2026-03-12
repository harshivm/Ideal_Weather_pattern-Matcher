import matplotlib.pyplot as plt
import os


def plot_weather_patterns(training_df, ideal_df, matches):

    os.makedirs("../output", exist_ok=True)

    # use same length for plotting
    min_len = min(len(training_df), len(ideal_df))

    x = training_df["x"].iloc[:min_len]

    for train_col, ideal_col in matches.items():

        plt.figure(figsize=(8,4))

        plt.plot(
            x,
            training_df[train_col].iloc[:min_len],
            label="Training Pattern"
        )

        plt.plot(
            x,
            ideal_df[ideal_col].iloc[:min_len],
            label="Ideal Pattern"
        )

        plt.title(f"{train_col} vs {ideal_col}")

        plt.xlabel("Time Index")

        plt.ylabel("Weather Value")

        plt.legend()

        plt.savefig(f"../output/{train_col}.png")

        plt.close()