import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # dt = weather.pivot_table(columns='city', index='month', values='temperature')  # this does not work, ?
    dt = pd.pivot_table(weather, index='month', columns='city', values='temperature', aggfunc='max')
    dt = dt.rename_axis(None, axis=1)
    return dt


df = pd.DataFrame([
    ['Jacksonville', 'January', 13],
    ['Jacksonville', 'February', 23],
    ['Jacksonville', 'March', 38],
    ['Jacksonville', 'April', 5],
    ['Jacksonville', 'May', 34],
    ['ElPaso', 'January', 20],
    ['ElPaso', 'February', 6],
    ['ElPaso', 'March', 26],
    ['ElPaso', 'April', 2],
    ['ElPaso', 'May', 43],
], columns=['city', 'month', 'temperature'])

print(pivotTable(df))
