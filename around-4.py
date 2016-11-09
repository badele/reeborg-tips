# Init world
# Execute two times (for select the world and execute this code)

World("Around 4")
color = 255
set_trace_style("thick")
set_trace_color("rgb(%(color)s, 0, 0)" % locals())
think(10)


def turn_right():
    for _ in range(3):
        turn_left()

while True:
    color = color ^ 255
    set_trace_color("rgb(%(color)s, 0, 0)" % locals())
    
    # Out of the corner
    while not front_is_clear():
        turn_right()
    
    # Turn around
    while front_is_clear():
        move()
        if right_is_clear():
            turn_right()
        elif not front_is_clear():
            turn_left()
