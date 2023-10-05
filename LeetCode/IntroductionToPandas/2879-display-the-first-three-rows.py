import pandas as pd
from typing import List


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees[:][0:3]


data = [
    [3, 'Bob', 'Operations', 48675],
    [90, 'Alice', 'Sales', 11096],
    [9, 'Tatiana', 'Engineering', 33805],
    [60, 'Annabelle', 'InformationTechnology', 37678],
    [49, 'Jonathan', 'HumanResources', 23793],
    [43, 'Khaled', 'Administration', 40454],
]

print(selectFirstRows(pd.DataFrame(data, columns=['employee_id', 'name', 'department', 'salary'])))
