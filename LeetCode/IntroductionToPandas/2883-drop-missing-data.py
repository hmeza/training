import pandas as pd
from typing import List


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['name'].notna()]


data = [
    [32, 'Piper', 5],
    [217, 'Grace', 19],
    [779, None, 20],
    [849, None, 14],
]

print(dropMissingData(pd.DataFrame(data, columns=['student_id', 'name', 'age'])))
