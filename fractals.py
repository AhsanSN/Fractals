from turtle import Turtle
turtle = Turtle()
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

def processRule(rules):
    replaceList = [rules[0]]
    for i in range(1, len(rules)):
        toReplace=""
        toPut=""
        isFirst=True
        if(">" not in rules[i]):
            break;
        for j in range(len(rules[i])):
            if(isFirst and rules[i][j]!=">"):
                toReplace = toReplace + rules[i][j]
            if(rules[i][j]==">"):
                isFirst = False;
            if(isFirst ==False and rules[i][j]!=">"):
                toPut = toPut + rules[i][j]
        replaceList.append([toReplace, toPut])
    return(replaceList)

def createEquationFromRules(rules, n):
    rule = rules[0]
    for j in range (0, n):
        for i in range (1, len(rules)):
            rule = rule.replace(rules[i][0], rules[i][1])
    return rule

def implement_FRule(rule, fwd, theta):
    
    backlog = []
    for i in rule:
        #print(i)
        if(i=="F"):
            turtle.forward(fwd)
        if(i=="+"):
            turtle.left(theta)
        if(i=="-"):
            turtle.right(theta)
        if(i=="["):
            backlog.append((turtle.position()[0], turtle.position()[1], turtle.heading()))
        if(i=="]"):
            popped = backlog.pop()
            moveToPos(popped[0], popped[1], popped[2])

def q1_p1():
    moveToPos(0, -250, 90)
    fwd = 6
    theta = 25.7
    n = 5
    rules = processRule(["F", "F>F[+F]F[-F]F"])
    equation = createEquationFromRules(rules, n)
    implement_FRule(equation, fwd, theta)


def q1_p2():
    moveToPos(0, -250, 90)
    rule = "F[+F]F[-F][F]"
    fwd = 6
    theta = 20
    n = 5
    rules = processRule(["F", "F>F[+F]F[-F][F]"])
    equation = createEquationFromRules(rules, n)
    implement_FRule(equation, fwd, theta)

def q1_p3():
    moveToPos(0, -250, 90)
    rule = "FF-[-F+F+F]+[+F-F-F]"
    fwd = 6
    theta = 22.5
    n = 4
    for i in range (0, n):
        rule = rule.replace("F", "FF-[-F+F+F]+[+F-F-F]")
    implement_FRule(rule, fwd, theta)

def q1_p4():
    moveToPos(0, -250, 90)
    rule = "F[+X]F[-X]+X"
    fwd = 0.3
    theta = 20
    n = 7
    for i in range (0, n):
        rule = rule.replace("X", "F[+X]F[-X]+X")
        rule = rule.replace("F", "FF")
    implement_FRule(rule, fwd, theta)
    
def q1_p5():
    moveToPos(0, -250, 90)
    rule = "F[+X][-X]FX"
    fwd = 0.4
    theta = 25.7
    n = 7
    for i in range (0, n):
        rule = rule.replace("X", "F[+X][-X]FX")
        rule = rule.replace("F", "FF")
    implement_FRule(rule, fwd, theta)

def q1_p6():
    moveToPos(0, -250, 90)
    rule = "F-[[X]+X]+F[+FX]-X"
    fwd = 1
    theta = 22.5
    n = 5
    for i in range (0, n):
        rule = rule.replace("X", "F-[[X]+X]+F[+FX]-X")
        rule = rule.replace("F", "FF")
    implement_FRule(rule, fwd, theta)
    
q1_p1()

        
#a = processRule(["F", "F>F[+F]F[-F]F"])
#createEquationFromRules(a, 2)




        


