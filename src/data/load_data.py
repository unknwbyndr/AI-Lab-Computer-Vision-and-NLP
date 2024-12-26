import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import os

def load_data():
    # Loop through the directories and files but do not print them
    for dirname, _, filenames in os.walk('/kaggle/input'):
        pass

if __name__ == "__main__":
    load_data()
