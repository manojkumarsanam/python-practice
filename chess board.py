from turtle import *
speed(0)
penup()
goto(-250,-250)
pendown()
for i in range(10):
    for j in range(10):
        begin_fill()
        if i%2==0:
            if  j%2!=0:
                color("black")
            else:
                color("black","white")
        else:
            if  j%2!=0:
                color("black","white")
            else:
                color("black")
        for k in  range(4):
            forward(50)
            right(90)
        end_fill()
        forward(50)
    penup()
    goto(-250,-50*(4-i))   
    pendown()
undo()
exitonclick()