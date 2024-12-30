import turtle
import pandas as pd


my_t = turtle.Turtle()

screen = turtle.Screen()
screen.title("Guess The Region")
image = "gambia.gif"
screen.addshape(image)
my_t.shape(image)

data = pd.read_csv("regions.csv")

regions = data.region.tolist()
#print(regions)

guessed_regions = []
while len(guessed_regions) < 6:
    user_guess = screen.textinput(title=f"{guessed_regions}/6 Correct",prompt="What's the next Region?").title()
    if user_guess == "Exit":
        left_reg = []
        for reg in regions:
            if reg not in guessed_regions:
                left_reg.append(reg)

        new_d = pd.DataFrame(left_reg)
        new_d.to_csv("Regions_to_know.csv")
        break
    if user_guess in regions:
        guessed_regions.append(user_guess)
        row = data[data.region == user_guess]
        #print(row)
        new_t = turtle.Turtle()
        new_t.penup()
        new_t.hideturtle()
        new_t.goto(row.x.item(),row.y.item())
        new_t.write(user_guess)








