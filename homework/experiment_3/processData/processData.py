import pandas as pd

if __name__ == '__main__':
    data_path = "../data/bank-additional-full.csv"
    data = pd.read_csv(data_path, sep=";")
    print(data.info())
