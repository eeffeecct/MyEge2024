from turtle import *


pencolor('red')
tracer(0)
begin_fill()
m = 60
# for i in range(7):
#     setheading(0)
#     circle(4*m, -180)
#     setheading(-90)
#     circle(4*m, -180)
#     setheading(-180)
#     circle(4*m, -180)
#     setheading(-270)
#     circle(4*m, -180)
# end_fill()


setheading(90)
# circle(6*m, 90)
# fd(2*m)
# circle(6*m, 90)
# fd(2*m)
# circle(6*m, 90)
# fd(2*m)
# circle(6*m, 90)
# fd(2*m)
circle(6*m, 262)
fd(2*m)
circle(6*m, 18)
fd(2*m)
circle(6*m, 18)
fd(2*m)
circle(6*m, 18)
fd(2*m)
fd(11*m)
circle(6*m, 18)

pencolor('green')
k = 20
for x in range(-k*m, k*m, m):
    penup()
    goto(x, -k*m)
    pendown()
    goto(x, k*m)


for y in range(-k*m, k*m, m):
    penup()
    goto(-k*m, y)
    pendown()
    goto(k*m, y)

update()
done()