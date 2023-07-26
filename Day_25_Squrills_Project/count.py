import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirills_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirills_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirills_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirills_count, cinnamon_squirills_count, black_squirills_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("final.csv")