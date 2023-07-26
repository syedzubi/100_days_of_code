# import turtle
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# answer_state = screen.textinput(title="Guess U.S. states", prompt= "Whats another state's name?").lower()


import pandas as pd
data = pd.read_csv("50_states.csv")
data["state"].str.lower()
print(data["state"])
# print(data[data.state == "Alabama"])
# print(data[data.state == answer_state])
