import pandas as pd
from typing import List


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees


data = [
    ['Jack', 19666],
    ['Piper', 74754],
    ['Mia', 62509],
    ['Ulysses', 54866],
]

print(modifySalaryColumn(pd.DataFrame(data, columns=['name', 'salary'])))
