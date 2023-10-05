import pandas as pd
from typing import List


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[(students['student_id'] == 101)][['name', 'age']]


data = [
    [101, 'Ulysses', 13],
    [53, 'William', 10],
    [128, 'Henry', 6],
    [3, 'Henry', 11],
]

print(selectData(pd.DataFrame(data, columns=['student_id', 'name', 'age'])))
