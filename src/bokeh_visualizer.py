from bokeh.plotting import figure, output_file, save
import os


def plot_interactive(training_df, ideal_df, matches):

    os.makedirs("../output", exist_ok=True)

    x = training_df["x"]

    for train_col, ideal_col in matches.items():

        p = figure(
            title=f"{train_col} vs {ideal_col}",
            width=800,
            height=400
        )

        p.line(
            x,
            training_df[train_col],
            legend_label="Training Pattern"
        )

        p.line(
            x,
            ideal_df[ideal_col],
            legend_label="Ideal Pattern"
        )

        output_file(
            f"../output/{train_col}_interactive.html"
        )

        save(p)