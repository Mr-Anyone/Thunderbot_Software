import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

PATH_TO_CSV = "/tmp/tbots/yellow_test/path_summary.csv"
MAXIMUM_DATAPOINT_COUNT = 20

def extract_row(row):
    x = [] 
    y = []
    duration = 0 # placeholder value which will be overwrited

    for i in range(1, MAXIMUM_DATAPOINT_COUNT +1, 1):
        x_point = row[f"x{i}"]
        y_point = row[f"y{i}"]
        x.append(x_point)
        y.append(y_point)
        duration = row[f"duration"]

    return np.array(x), np.array(y), duration


if __name__ == "__main__":
    df = pd.read_csv(PATH_TO_CSV)
    # data used to standardize
    maximum_duration = df["duration"].max()
    minimum_duration = df["duration"].min()

    # plotting every row in the dataframe
    for row in df.iloc():
        x, y, duration = extract_row(row)
        standardized_color = (duration - minimum_duration) / (maximum_duration - minimum_duration)
        color = (standardized_color, standardized_color, standardized_color)

        plt.plot(x, y, c=color)
    plt.show()
