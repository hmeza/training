import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.sort_values(by='weight', ascending=False).loc[animals['weight'] > 100][['name']]


df = pd.DataFrame([
    ['Tatiana', 'Snake', 98, 464],
    ['Khaled', 'Giraffe', 50, 41],
    ['Alex', 'Leopard', 6, 328],
    ['Jonathan', 'Monkey', 45, 463],
    ['Stefan', 'Bear', 100, 50],
    ['Tommy', 'Panda', 26, 349],
], columns=['name', 'species', 'age', 'weight'])

print(findHeavyAnimals(df))
