from turtle import *
color('black', 'blue')
begin_fill()
while True:
    forward(100)
    left(50)
    if abs(pos()) < 1:
        break
end_fill()
done()