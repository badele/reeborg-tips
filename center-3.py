# Init world
# Execute two times (for select the world and execute this code)

World("Center 3")
think(10)

# Search width
lastposx = 1
while front_is_clear():
    lastposx += 1
    move()

# Search height
turn_left()
lastposy = 1
while front_is_clear():
    lastposy += 1
    move()

# Move to x middle
middle = int(lastposx - ((lastposx + 1) / 2))
turn_left()
for _ in range(middle):
    move()

# Move to y middle
middle = int(lastposy - ((lastposy + 1) / 2))
turn_left()
for _ in range(middle):
    move()

put()