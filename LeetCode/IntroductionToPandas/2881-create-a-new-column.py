import pandas as pd
from typing import List


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees


data = [
    ['Piper', 4548],
    ['Grace', 28150],
    ['Georgia', 1103],
    ['Willow', 6593],
    ['Finn', 74576],
    ['Thomas', 24433],
]

df = pd.DataFrame(data, columns=['name', 'salary'])
print(createBonusColumn(df))
