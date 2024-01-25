import turtle
import pandas
from scorecard import Scorecard
from state_icons import States

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()
states = []

scorecard = Scorecard()  # Initiating the scorecard object to keep record of and display scores
state_icons = States()  # Initiate States() object to place state names in place
game_is_on = True
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
while game_is_on:
    if answer_state.title() in data_dict.get('state').values():
        condition = data['state'] == answer_state.title()  # Condition to access the row containing the state
        state_row = data[condition]  # Accessing the row using the condition above
        state_name = state_row.loc[state_row.index[0], 'state']
        xcor = int(state_row.loc[state_row.index[0], 'x'])
        ycor = int(state_row.loc[state_row.index[0], 'y'])
        states.append(state_name)
        scorecard.update_scorecard()  # Updating the scorecard
        state_icons.post_state_name(state_name, xcor, ycor)  # Calling the method to place the State name at its place

    if answer_state.title() == 'Exit':
        break
    if scorecard.score == 50:  # End game if all states are answered correctly
        game_is_on = False
    # Keep asking for next state until game is on
    answer_state = screen.textinput(title=f"{scorecard.score}/50 States Correct", prompt="What's another state's name?")

not_guessed = [state for state in data_dict.get('state').values() if state not in states]
# for state in data_dict.get('state').values():
#     if state not in states:
#         not_answered.append(state)
df = pandas.DataFrame(not_guessed)
df.to_csv("Unanswered_states.csv")
