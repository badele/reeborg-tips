# Init world
# Execute two times (for select the world and execute this code)

#####################################
# !!! Center 1 and Center 2 same code
#####################################

World("Center 2")
think(10)

# Search width
lastpos = 1
while front_is_clear():
    lastpos += 1
    move()

# Half turn
for _ in range(2):
    turn_left()

# Move to middle
middle = int(lastpos - ((lastpos + 1) / 2))
for _ in range(middle):
    move()

put()