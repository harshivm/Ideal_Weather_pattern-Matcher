import sqlite3
import os


def save_results(df):

    db_path = "../db/weather_patterns.db"

    os.makedirs("../db", exist_ok=True)

    conn = sqlite3.connect(db_path)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            x REAL,
            observed_weather REAL,
            deviation REAL,
            ideal_pattern TEXT
        )
    """)

    cursor.execute("DELETE FROM weather_matches")

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO weather_matches
            (x, observed_weather, deviation, ideal_pattern)
            VALUES (?, ?, ?, ?)
            """,
            (
                row["x"],
                row["observed_weather"],
                row["deviation"],
                row["ideal_pattern"]
            )
        )

    conn.commit()

    conn.close()

    print("Results saved to database.")