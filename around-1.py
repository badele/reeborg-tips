# Init world
# Execute two times (for select the world and execute this code)
World("Around 1")
color=255
set_trace_style("thick")
set_trace_color("rgb(%(color)s, 0, 0)" % locals())
think(100)

# Turn around
while True:
    while front_is_clear():
        # Test completely turn
        if default_robot().body.x == 1 and default_robot().body.y == 2:
            color = color ^ 255
            set_trace_color("rgb(%(color)s, 0, 0)" % locals())
        move()
    turn_left()