# Ideal Function Matching for Weather Pattern Identification

## Project Overview

This project implements an **Ideal Function Matching algorithm** to analyze weather patterns using real-world datasets. The system compares training weather data with a set of predefined ideal mathematical functions in order to identify which ideal functions best represent the observed weather patterns.

The algorithm uses the **Least Squares Error (LSE)** method to determine the similarity between training data and ideal functions. After identifying the most appropriate ideal functions, the system assigns observed weather data points to the closest matching ideal function based on a predefined deviation threshold.

The implementation is developed using Python and leverages several data analysis libraries to process datasets, perform mathematical computations, store results in a database, and visualize the outcomes.

---

# Project Objectives

The main objectives of this project are:

- Analyze weather patterns using real-world datasets
- Apply mathematical pattern matching techniques
- Identify ideal functions that approximate weather trends
- Classify observed weather data using deviation rules
- Store classification results in a database
- Visualize weather patterns using graphical tools

---

# Technologies Used

The project is implemented using the following technologies:

- Python
- Pandas
- NumPy
- Matplotlib
- Bokeh
- SQLite

---

# Dataset Sources

The datasets used in this project were obtained from **Kaggle weather datasets**.

Three weather datasets were used:

- Global Weather Dataset
- Daily Climate Dataset
- Weather Forecast Dataset

These datasets were processed to create the required datasets used by the algorithm.

---

# Project Structure

```
WeatherPatternMatcher/

kaggle_raw_data/
    GlobalWeatherRepository.csv
    DailyDelhiClimateTest.csv
    weather_forecast_data.csv

data/
    weather_training_data.csv
    weather_ideal_patterns.csv
    weather_test_data.csv

src/
    main.py
    data_loader.py
    pattern_matcher.py
    weather_assigner.py
    db_writer.py
    visualizer.py
    bokeh_visualizer.py

scripts/
    prepare_weather_datasets.py

db/
    weather_patterns.db

output/
    temperature_pattern.png
    humidity_pattern.png
    pressure_pattern.png
    wind_pattern.png

tests/
    test_data_loader.py
    test_pattern_matcher.py
    test_weather_assigner.py
```

---

# System Workflow

The workflow of the system follows these steps:

1. Load weather datasets from Kaggle
2. Preprocess datasets and generate training data
3. Generate ideal mathematical functions
4. Compare training patterns with ideal functions
5. Identify the best matching ideal functions
6. Assign observed weather values to ideal functions
7. Store results in a SQLite database
8. Generate visualizations of weather patterns

---

# Mathematical Model

The system uses the **Least Squares Error method** to determine the similarity between functions.

Formula:

```
LSE = Σ (y_training − y_ideal)^2
```

The ideal function with the smallest error is selected as the best match.

Observed weather values are assigned to an ideal function using the rule:

```
|y_observed − y_ideal| ≤ √2 × max_deviation
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/WeatherPatternMatcher.git
```

Navigate to the project directory:

```
cd WeatherPatternMatcher
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running the Project

### Step 1: Prepare datasets

Run the dataset preparation script:

```
python scripts/prepare_weather_datasets.py
```

This will generate the following datasets:

- weather_training_data.csv
- weather_ideal_patterns.csv
- weather_test_data.csv

### Step 2: Run the algorithm

Navigate to the source directory:

```
cd src
```

Run the main program:

```
python main.py
```

---

# Output

The system generates:

Database results:

```
db/weather_patterns.db
```

Visualization outputs:

```
output/
temperature_pattern.png
humidity_pattern.png
pressure_pattern.png
wind_pattern.png
```

These graphs illustrate how closely the ideal functions approximate the training weather patterns.

---

# Future Improvements

Possible improvements include:

- Integration with machine learning weather prediction models
- Analysis of larger climate datasets
- Real-time weather data processing
- Interactive dashboards for data visualization

---

# Author

Student Name  
Master's Program in Computer Science

---

# License

This project is intended for educational purposes.