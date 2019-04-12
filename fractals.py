import turtle
turtle.speed(0)

'''
turtle.position
turtle.forward(25)
#turtle.position()
turtle.forward(-75)
turtle.right(90)
#turtle.position()
'''

def moveToPos(x, y, angle):
    turtle.up()
    turtle.ht()
    turtle.setheading(angle)
    turtle.goto(x, y)
    # reshow the turtle
    turtle.st()
    turtle.down()

def implement_FRule(rule, fwd, theta):
    backlog = []
    for i in rule:
        #print(i)
        if(i=="F"):
            turtle.forward(fwd)
        if(i=="+"):
            turtle.right(theta)
        if(i=="-"):
            turtle.left(theta)
        if(i=="["):
            backlog.append((turtle.position()[0], turtle.position()[1], turtle.heading()))
        if(i=="]"):
            popped = backlog.pop()
            moveToPos(popped[0], popped[1], popped[2])

def q1_p1():
    moveToPos(0, -250, 90)
    rule = "F[+F]F[-F]F"
    fwd = 6
    theta = 25
    n = 5
    for i in range (0, n):
        rule = rule.replace("F", "F[+F]F[-F]F")
    implement_FRule(rule, fwd, theta)


q1_p1()
