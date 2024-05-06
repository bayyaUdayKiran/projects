import pandas as pd
import sys


def add_data():
    try:
        data = sys.argv[1]
        units = sys.argv[2]
        price = sys.argv[3]

    except IndexError:
        date = input("Input Date: ")
        units = float(input("Input Units: "))
        price = float(input("Input Price: "))


    try:
        df = pd.read_csv("data.csv")

    except FileNotFoundError:
        cols = ["DATE", "UNITS", "PRICE"]
        mty_df = pd.DataFrame(columns=cols)
        mty_df.to_csv("data.csv", index=False)
        df = pd.read_csv("data.csv")

    

    nw_row = {"DATA": date, "UNITS": units, "PRICE": price}
    nw_df = pd.DataFrame([nw_row])
    df = pd.concat([df, nw_df])

    df.to_csv("data.csv")


def tot_units():
    df = pd.read_csv("data.csv")
    res = df["UNITS"].sum()
    return res


if __name__ == "__main__":
    add_data()