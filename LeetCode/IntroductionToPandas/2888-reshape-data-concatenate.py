import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0)


df1 = pd.DataFrame([
                   [1, 'Mason', 8],
                   [2, 'Ava', 6],
                   [3, 'Taylor', 15],
                   [4, 'Georgia', 17],
], columns=['student_id', 'name', 'age'])

df2 = pd.DataFrame([
                   [5, 'Leo', 7],
                   [6, 'Alex', 7],
], columns=['student_id', 'name', 'age'])

print(concatenateTables(df1, df2))
