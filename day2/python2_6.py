import turtle

turtle.shape("turtle")
turtle.speed(3)
"""
# 무식한 방법
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

# 조금 똑똑한 방법
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

# 조금 더 똑똑한 방법
def drawRec(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
"""


# 궁극의 방법
def draSomthing(size, angle):
    for i in range(4):
        turtle.forward(size)
        turtle.right(300/angle)

draSomthing(100, 5)
draSomthing(200, 6)
draSomthing(10, 64)


