from turtle import Turtle


class States:
    def __init__(self):
        self.states = []

    def post_state_name(self, state, xcor, ycor):
        new_state = Turtle()
        new_state.ht()
        new_state.penup()
        new_state.goto(xcor, ycor)  # Set the turtle's position to (xcor, ycor)
        new_state.write(arg=state, move=True, align='left', font=('Arial', 12, 'normal'))
        self.states.append(new_state)
