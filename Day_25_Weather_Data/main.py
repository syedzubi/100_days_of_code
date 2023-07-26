import pandas
data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()

# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print((monday["temp"] * 9/5) + 32)
datas_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(datas_dict)
data.to_csv("new_data.csv")