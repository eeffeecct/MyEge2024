from turtle import *
setheading(0)
tracer(0)
m = 20
for i in range(7):
    setheading(0)
    circle(4*m, -180)
    setheading(-90)
    circle(4*m, -180)
    setheading(-180)
    circle(4*m, -180)
    setheading(-270)
    circle(4*m, -180)
end_fill()


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