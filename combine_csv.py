#!/usr/bin/python3

import os
import pandas as pd

def combine_csv():
    try:
        files = os.listdir(os.getcwd())
        csv_files = [f for f in files if f.endswith('.csv')]
        combined_file = pd.concat([pd.read_csv(f) for f in csv_files])
        combined_file.to_csv('combined_file.csv', index=False)
    except:
        pass

if __name__ == '__main__':
    combine_csv()