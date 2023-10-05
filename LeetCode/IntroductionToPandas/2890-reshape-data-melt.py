import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(
        id_vars='product', value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
        var_name="quarter", value_name="sales"
    )



df = pd.DataFrame([
    ['Umbrella', 417, 224, 379, 611],
    ['SleepingBag', 800, 936, 93, 875],
], columns=['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])

print(meltTable(df))
