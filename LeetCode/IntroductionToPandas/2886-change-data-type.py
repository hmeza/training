import pandas as pd
from typing import List


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students


data = [
    [1, 'Ava', 6, 73.0],
    [2, 'Kate', 15, 87.0],
]

print(changeDatatype(pd.DataFrame(data, columns=['student_id', 'name', 'age', 'grade'])))
