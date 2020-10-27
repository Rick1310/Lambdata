"""Lambdata - a collection of Data Science helepr functions"""

# Libraries accessed through pipenv
import pandas as pd
import numpy as np

LIST = ['Things', 'Inside', 'A List']

def df_clean(df):
    """Cleans a dataframe"""


    # Will identify columns with more than 500 observations. 

    hc_cols = [for col in col in df.describe(include='object').columns
               if df[col].nunique() > 500]

    # Will take the identified columns and remove them from the df. 

    df.drop(columns=hc_cols, inplace=True)

    return df

def df_display(df):
    """sets notebook display option"""

    # Will set the max rows allowed in a notebook to 999.
    max_rows = pd.set_option("display.max_rows", 999)


def enlarge(n):
    """Multiplys a number by 100"""

    return n*100

    y = int(input("Enter a number"))
    print(y, enlarge(y))


