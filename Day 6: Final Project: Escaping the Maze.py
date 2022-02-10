# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#Reborg has it's own sets of functions


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def run():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
            if front_is_clear():
                move()
                if wall_on_right():
                    turn_left()
                    if front_is_clear():
                        move()
        elif front_is_clear():
                move()
                if wall_on_right() and front_is_clear:
                    turn_left()
                    if front_is_clear():
                        move()
        elif wall_in_front():
            turn_left()

run()            
    
