# get out of the maze on <https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json>

### coded just to not get syntax highlighting errors
def wall_in_front():
    pass
def wall_on_right():
    pass
def turn_left():
    pass
def move():
    pass
def at_goal():
    pass
###

# Solution bellow
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not wall_in_front():
    move()

turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif not wall_in_front():
        move()
    else:
        turn_left()
