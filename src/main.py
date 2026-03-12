import sys

from data_loader import load_all_data
from pattern_matcher import find_best_patterns
from weather_assigner import assign_weather_patterns
from db_writer import save_results
from visualizer import plot_weather_patterns
from bokeh_visualizer import plot_interactive


print("Loading datasets...")

training_df, ideal_df, test_df = load_all_data()

if any(df is None for df in (training_df, ideal_df, test_df)):

    print("Dataset loading failed.")

    sys.exit(1)


print("Finding best ideal weather patterns...")

best_patterns = find_best_patterns(training_df, ideal_df)

print("Best matches:")

print(best_patterns)


print("Assigning observed weather data...")

assigned_df = assign_weather_patterns(
    test_df,
    ideal_df,
    training_df,
    best_patterns
)


print("Saving results to database...")

save_results(assigned_df)


print("Project execution completed successfully.")
print("Generating graphs...")

plot_weather_patterns(training_df, ideal_df, best_patterns)

plot_interactive(training_df, ideal_df, best_patterns)