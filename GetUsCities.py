import csv
import pandas as pd
import os


def load_csv_as_df(file_name, sub_directories, col_names=None):
    '''
    Load any csv as a pandas dataframe. Provide the filename, the subdirectories, and columns to read(if desired).
    '''
    base_path = os.getcwd()
    full_path = base_path + '/' + sub_directories + file_name

    if col_names is not None:
        return pd.read_csv(full_path, usecols=col_names)

    # print('Full Path: ', full_path)
    return pd.read_csv(full_path, header=0)


column_names = ["city_ascii", "state_id", "zips", "id"]
df = load_csv_as_df("uscities.csv", "", column_names)

print(df.head())
df.to_csv('US-Cities.csv', encoding='utf-8', index=False)

