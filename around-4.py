# Init world
# Execute two times

World("Around 4")
color = 255
set_trace_style("thick")
set_trace_color("rgb(%(color)s, 0, 0)" % locals())
think(10)


def turn_right():
    for _ in range(3):
        turn_left()

#############
# Out the box
#############
while not front_is_clear():
    turn_left()

while front_is_clear():
    move()

while right_is_clear():
    turn_right()
    move()

# Turn around
while True:
    while front_is_clear():
        # Test completely turn
        if default_robot().body.x == 1 and default_robot().body.y == 2:
            color = color ^ 255
            set_trace_color("rgb(%(color)s, 0, 0)" % locals())
            turn_left()
            move()

        # Test if robot can turn right
        if right_is_clear():
            turn_right()

        move()

    turn_left()