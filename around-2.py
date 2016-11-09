# Init world
# Execute two times (for select the world and execute this code)

#####################################
# !!! Around 2 and Around 3 same code
#####################################

World("Around 2")
color=255
set_trace_style("thick")
set_trace_color("rgb(%(color)s, 0, 0)" % locals())
think(100)

def turn_right():
    for _ in range(3):
        turn_left()

# Turn around
while True:
    while front_is_clear():
        # Test completely turn
        if default_robot().body.x == 1 and default_robot().body.y == 2:
            color = color ^ 255
            set_trace_color("rgb(%(color)s, 0, 0)" % locals())

        # Test if robot can turn right
        if right_is_clear():
            turn_right()

        move()

    turn_left()