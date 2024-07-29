import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S States Game")
# screen.width = 725
# screen.length = 491
# screen.screensize(725,491)
# screen.bgpic("./blank_states_img.gif")

img = "Blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
states_discovered = 0
df = pd.read_csv("50_states.csv")
list_of_states = df.state.to_list()
# print(df.to_list())

# print(df)print(list_of_states)
# print(df.state[df.state == 'Alabama'])
# print(list_of_states.index('Texas'))
# print(df.y[42])
# print(df.state.to_list())


def show_state(x, y, state):
    tim = turtle.Turtle()
    tim.hideturtle()
    tim.penup()
    tim.goto(x, y)
    tim.write(f"{state}",move=False, align="left",font= ("Arial",10,"normal"))

guessed_states = []
while states_discovered < 51:
    user_answer = screen.textinput(title="Guess the State", prompt="Name a state").title()
    if user_answer == 'Exit':
        break
    if user_answer in list_of_states:
        guessed_states.append(user_answer)
        ind = list_of_states.index(user_answer)
        # state_data = df[df.state == state]
        # print(state_data.x)
        x_ord = df.x[ind]
        y_ord = df.y[ind]
        # print(f"X: {x_ord}, Y: {y_ord}")
        show_state(x_ord, y_ord, user_answer)
        states_discovered += 1
        screen.title(f"{states_discovered}/50 States Correct")
## print states not guessed to a csv file
learn_states = []
for state in list_of_states:
    if state not in guessed_states:
        learn_states.append(state)
# print(len(learn_states))
new_df = pd.DataFrame(learn_states)
new_df.to_csv("States_to_be_learned.csv")