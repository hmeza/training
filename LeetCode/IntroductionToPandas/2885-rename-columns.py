import pandas as pd
from typing import List


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'})


data = [
    [1, 'Mason', 'King', 6],
    [2, 'Ava', 'Wright', 7],
    [3, 'Taylor', 'Hall', 16],
    [4, 'Georgia', 'Thompson', 18],
    [5, 'Thomas', 'Moore', 10],
]

print(renameColumns(pd.DataFrame(data, columns=['id', 'first', 'last', 'age'])))
