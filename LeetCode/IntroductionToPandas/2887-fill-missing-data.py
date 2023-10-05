import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    return products.fillna(0)


data = [
    ['Wristwatch', 32, 135],
    ['WirelessEarbuds', None, 821],
    ['GolfClubs', None, 9319],
    ['Printer', 849, 3051],
]

print(fillMissingValues(pd.DataFrame(data, columns=['name', 'quantity', 'price'])))
