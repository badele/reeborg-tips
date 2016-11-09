# Init vars
set_max_nb_instructions(10000)
color = 255
set_trace_style("thick")
set_trace_color("rgb(%(color)s, 0, 0)" % locals())
think(10)

while True:
    if default_robot().body.x == 1 and default_robot().body.y == 2:
        color = color ^ 255
        set_trace_color("rgb(%(color)s, 0, 0)" % locals())

    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

