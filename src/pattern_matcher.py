import numpy as np
def calculate_lsq(y_train, y_ideal):

    return np.sum((y_train - y_ideal) ** 2)
def find_best_patterns(training_df, ideal_df):

    best_matches = {}

    for train_col in training_df.columns:

        if train_col == "x":
            continue

        min_error = float("inf")

        best_pattern = None

        for ideal_col in ideal_df.columns:

            if ideal_col == "x":
                continue

            error = calculate_lsq(
                training_df[train_col],
                ideal_df[ideal_col]
            )

            if error < min_error:

                min_error = error

                best_pattern = ideal_col

        best_matches[train_col] = best_pattern

    return best_matches