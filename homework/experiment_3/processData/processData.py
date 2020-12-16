import pandas as pd

if __name__ == '__main__':
    data_path = "../data/bank-additional-full.csv"
    data = pd.read_csv(data_path, sep=";")
    print(data.info())

    for i in data.columns:
        if type(data[i][0]) is str:
            print("未知的列为：" + i + ": " + str(data[data[i] == "unknown"]["y"].count()))