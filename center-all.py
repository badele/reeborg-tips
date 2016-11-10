# Init world
# Execute two times (for select the world and execute this code)
# Work for all worlds dimension

think(10)


def turn_right():
    for _ in range(3):
        turn_left()


# Search widh and hight
lastposx = 1
lastposy = 1
cornerx = False
cornery = False

while not (cornerx and cornery):
    # Search width
    if not cornerx:
        cornerx = not front_is_clear()
        if not cornerx:
            lastposx += 1
            move()
            cornerx = not front_is_clear()

        # Turn left, if the cornery not found
        if not cornery:
            turn_left()

    # Search height
    if not cornery:
        cornery = not front_is_clear()
        if not cornery:
            lastposy += 1
            move()
            cornery = not front_is_clear()

        # Turn right, if the cornerx not found
        if not cornerx:
            turn_right()

# Turn
turn_left()
if lastposx > lastposy:
    turn_left()

# Move to x middle
middle = int(lastposx - ((lastposx + 1) / 2))
for _ in range(middle):
    move()

# Move to y middle
middle = int(lastposy - ((lastposy + 1) / 2))
turn_left()
for _ in range(middle):
    move()

put()