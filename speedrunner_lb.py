# Leaderboard module for Speed Runner, by Tausif Chowdhury & Danell Cespedes
# https://github.com/tausifc04/speedrunner

def load_lb(file_name, leader_names, leader_scores):

    lb_file = open(file_name, "r")

    for line in lb_file:
        leader_name = ""
        leader_score = ""
        index = 0

        while (line[index] != ","):
            leader_name += line[index]
            index += 1
        
        leader_names.append(leader_name)

        index += 1
        while (line[index] != "\n"):
            leader_score += line[index]
            index += 1
        
        leader_scores.append(int(leader_score))
    
    lb_file.close()


def update_lb(file_name, leader_names, leader_scores, name, score):

    leader_index = 0
    while (leader_index < len(leader_scores)):
        if score >= leader_scores[leader_index]:
            break
        else:
            leader_index += 1
    
    leader_scores.insert(leader_index, score)
    leader_names.insert(leader_index, name)

    if len(leader_names) == 6:
        leader_names.pop()
    if len(leader_scores) == 6:
        leader_scores.pop()
    
    lb_file = open(file_name, "w")

    leader_index = 0

    while (leader_index < len(leader_names)):
        lb_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
        leader_index += 1

    lb_file.close()


def draw_lb(leader_names, leader_scores, high_scorer, turtle_object, score):
    
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.hideturtle()
    turtle_object.goto(-100, 125)
    leader_index = 0

    while (leader_index < len(leader_names)):
        turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]), font = font_setup)
        turtle_object.goto(-100, int(turtle_object.ycor()) - 50)
        leader_index += 1
    
    if high_scorer:
        turtle_object.setx(-150)
        turtle_object.write("Congrats on making the leaderboard!", font = font_setup)
    else:
        turtle_object.write("Tough luck bud.", font = font_setup)

    turtle_object.goto(-100, int(turtle_object.ycor()) - 50)
