import pandas as pd
import numpy as np

df = pd.DataFrame({"A": ["2024-10-11", "2024-10-15", "2024-10-19"],
                   "B": [1, 2, 3]})

df["A"] = pd.to_datetime(df["A"])
df.set_index('A', inplace=True)

print(type(df.loc[:'2024-10-14'].to_json()))
