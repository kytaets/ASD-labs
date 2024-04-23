import turtle
import random
import math


class Vertex:
    def __init__(self, number, pos_x, pos_y, position, next_el, prev_el):
        self.number = number
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = position
        self.next_el = next_el
        self.prev_el = prev_el


# Creating a matrix with random float numbers
def randMatrix(n):
    random.seed(3222)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.uniform(0,2))
        matrix.append(row)
    return matrix


# Multiplying matrix by number
def multiplyMatrix(matrix, num):
    result = []
    for row in matrix:
        updated = [round(element * num) for element in row]       # rounding element
        result.append(updated)
    return result


def createPositions(N):
    vertexes = []
    x = -150
    y = 150
    position = "angle"

    for i in range(N):
        prev = i - 1
        next_el = i + 1
        if i == 0:
            prev = 11
        elif i == 11:
            next_el = 0

        if i % 3 == 0:
            position = "angle"

        vert = Vertex(i, x, y, position, next_el, prev)
        vertexes.append(vert)

        if i <= 2:
            x += 100
            position = "hor"
        elif 2 < i <= 5:
            y -= 100
            position = "vert"
        elif 5 < i <= 8:
            x -= 100
            position = "hor"
        elif i > 8:
            y += 100
            position = "vert"


    return vertexes


# Writing numbers in circles
def writeNumbers():
    number = 1
    for i in range(4):
        for j in range(3):
            turtle.write(f"{number}", False, 'center', ('Arial', 25, 'normal'))
            turtle.up()
            turtle.forward(100)
            turtle.down()
            number += 1

        turtle.up()
        turtle.right(90)
        turtle.down()

# Drawing circles
def drawCircles():
    turtle.speed(0)
    turtle.up()
    turtle.goto(-150, 125)
    turtle.down()
    for i in range(4):
        for j in range(3):
            turtle.up()
            turtle.forward(100)
            turtle.down()
            turtle.circle(25)

        turtle.up()
        turtle.back(25)
        turtle.right(90)
        turtle.back(25)
        turtle.down()

    turtle.up()
    turtle.goto(-150, 130)
    turtle.down()

    turtle.speed(0)
    writeNumbers()


def drawArrow():
    position = turtle.position()
    turtle.left(135)
    turtle.forward(10)
    turtle.up()
    turtle.goto(position)
    turtle.down()
    turtle.left(90)
    turtle.forward(10)


def drawLeft(row, el):
    turtle.up()
    turtle.goto(row.pos_x, row.pos_y)
    turtle.setheading(180)
    turtle.forward(25)
    turtle.down()
    turtle.goto(el.pos_x + 25, el.pos_y)
    drawArrow()


def drawRight(row, el):
    turtle.up()
    turtle.goto(row.pos_x, row.pos_y)
    turtle.setheading(360)
    turtle.forward(25)
    turtle.down()
    turtle.goto(el.pos_x - 25, el.pos_y)
    drawArrow()


def drawUp(row, el):
    turtle.up()
    turtle.goto(row.pos_x, row.pos_y)
    turtle.setheading(90)
    turtle.forward(25)
    turtle.down()
    turtle.goto(el.pos_x, el.pos_y - 25)
    drawArrow()


def drawDown(row, el):
    turtle.up()
    turtle.goto(row.pos_x, row.pos_y)
    turtle.setheading(270)
    turtle.forward(25)
    turtle.down()
    turtle.goto(el.pos_x, el.pos_y + 25)
    drawArrow()


def calculateHorizontalLine(row, el, degrees):
    rad = math.radians(degrees)
    a = abs(row.pos_x - el.pos_x)
    b = a / 2 * math.cos(rad)
    return b

def drawDistantRightUp(row, el):
    degrees = 10
    b = calculateHorizontalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x, row.pos_y + 25)
    turtle.setheading(degrees)
    turtle.down()
    turtle.forward(b)
    turtle.right(degrees*2)
    turtle.forward(b)
    drawArrow()


def drawDistantLeftUp(row, el):
    degrees = 10
    b = calculateHorizontalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x, row.pos_y + 25)
    turtle.setheading(180 - degrees)
    turtle.down()
    turtle.forward(b)
    turtle.left(degrees*2)
    turtle.forward(b)
    drawArrow()


def drawDistantRightDown(row, el):
    degrees = 10
    b = calculateHorizontalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x, row.pos_y - 25)
    turtle.setheading(360-degrees)
    turtle.down()
    turtle.forward(b)
    turtle.left(degrees*2)
    turtle.forward(b)
    drawArrow()


def drawDistantLeftDown(row, el):
    degrees = 10
    b = calculateHorizontalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x, row.pos_y - 25)
    turtle.setheading(180+degrees)
    turtle.down()
    turtle.forward(b)
    turtle.right(degrees*2)
    turtle.forward(b)
    drawArrow()


def calculateVerticalLine(row, el, degrees):
    rad = math.radians(degrees)
    a = abs(row.pos_y - el.pos_y)
    b = a / 2 * math.cos(rad)
    return b

def drawDistantUpLeft(row, el):
    degrees = 10
    b = calculateVerticalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x - 25, row.pos_y)
    turtle.setheading(90+degrees)
    turtle.down()
    turtle.forward(b)
    turtle.right(degrees*2)
    turtle.forward(b)
    drawArrow()


def drawDistantUpRight(row, el):
    degrees = 10
    b = calculateVerticalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x + 25, row.pos_y)
    turtle.setheading(90-degrees)
    turtle.down()
    turtle.forward(b)
    turtle.left(degrees*2)
    turtle.forward(b)
    drawArrow()


def drawDistantDownLeft(row, el):
    degrees = 10
    b = calculateVerticalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x - 25, row.pos_y)
    turtle.setheading(270-degrees)
    turtle.down()
    turtle.forward(b)
    turtle.left(degrees*2)
    turtle.forward(b)
    drawArrow()


def drawDistantDownRight(row, el, direction):
    degrees = 10
    b = calculateVerticalLine(row, el, degrees)

    turtle.up()
    turtle.goto(row.pos_x + 25, row.pos_y)
    turtle.setheading(270+degrees)
    turtle.down()
    turtle.forward(b)
    turtle.right(degrees*2)
    turtle.forward(b)
    drawArrow()


def drawDiagonal(row, el, direction):
    def gotoPoint():
        if position == "hor":
            is_negative = y / abs(y)
            print(is_negative)
            start = y - 25 * is_negative
            turtle.goto(x, start)
        elif position == "vert":
            is_negative = x / abs(x)
            print(is_negative)
            start = x - 25 * is_negative
            turtle.goto(start, y)
        else:
            is_negative_x = x / abs(x)
            is_negative_y = y / abs(y)
            print(is_negative_x, is_negative_y)
            start_x = x - 25 * math.cos(0.785) * is_negative_x
            start_y = y - 25 * math.cos(0.785) * is_negative_y
            turtle.goto(start_x, start_y)

    position = row.position
    x = row.pos_x
    y = row.pos_y

    turtle.up()
    gotoPoint()
    turtle.down()

    position = el.position
    x = el.pos_x
    y = el.pos_y
    turtle.setheading(turtle.towards(x,y))
    gotoPoint()
    drawArrow()


def drawConnections(matrix, vertexes, direction=True):
    # i=3

    for i in range(len(matrix)):
        vert1 = vertexes[i]
        for j in range(len(matrix[i])):
            turtle.speed(0)
            if matrix[i][j]:
                if vert1 != vertexes[j]:
                    if vertexes[j].pos_y == vert1.pos_y:
                        # Connecting neighbours
                        if vert1.next_el == vertexes[j].number:      # horizontal next
                            print("horiz next")
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if i <= 3:
                                drawRight(vert1, vertexes[j])
                            else:
                                drawLeft(vert1, vertexes[j])

                        elif vert1.prev_el == vertexes[j].number:    # horizontal previous
                            print("horiz prev")
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if i <= 3:
                                drawLeft(vert1, vertexes[j])
                            else:
                                drawRight(vert1, vertexes[j])

                        # Connecting other
                        elif vert1.number < vertexes[j].number:     # horizontal next
                            turtle.speed(0)
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if i <= 3:
                                drawDistantRightUp(vert1, vertexes[j])
                            elif 6 <= i <= 9:
                                drawDistantLeftDown(vert1, vertexes[j])
                        elif vert1.number > vertexes[j].number:     # horizontal previous
                            turtle.speed(0)
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if i <= 3:
                                drawDistantLeftUp(vert1, vertexes[j])
                            elif 6 <= i <= 9:
                                drawDistantRightDown(vert1, vertexes[j])

                    elif vertexes[j].pos_x == vert1.pos_x:
                        # Connecting neighbours
                        if vert1.next_el == vertexes[j].number:    # vertical next
                            print("vert next")
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if 0 < i <= 6:
                                drawDown(vert1, vertexes[j])
                            else:
                                drawUp(vert1, vertexes[j])
                        elif vert1.prev_el == vertexes[j].number:    # vertical previous
                            print("vert prev")
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if j <= 6:
                                drawUp(vert1, vertexes[j])
                            else:
                                drawDown(vert1, vertexes[j])

                        # Connecting other
                        elif vert1.number < vertexes[j].number:     # vertical next
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if 3 <= i < 6:
                                drawDistantDownRight(vert1, vertexes[j])
                            elif i == 0:
                                drawDistantDownLeft(vert1, vertexes[j])
                            elif i >= 9:
                                drawDistantUpLeft(vert1, vertexes[j])

                        elif vert1.number > vertexes[j].number:     # vertical previous
                            print(vertexes[j].number, vertexes[j].pos_x, vertexes[j].pos_y, vertexes[j].next_el,
                                  vertexes[j].prev_el)
                            if 5 <= i < 6:
                                drawDistantUpRight(vert1, vertexes[j])
                            elif i > 10:
                                drawDistantDownLeft(vert1, vertexes[j])

                    else:
                        drawDiagonal(vert1, vertexes[j])


n3 = 2
n4 = 2
N = 10 + n3     # N = 12

T = randMatrix(N)                       # creating matrix
k = 1.0 - n3*0.02 - n4*0.005 - 0.25     # creating multiplier
A = multiplyMatrix(T, k)                # converting matrix into graph
for i in range(N):
    print(A[i])


drawCircles()
createPositions(N)
vertMatrix = createPositions(N)
drawConnections(A, vertMatrix)







turtle.exitonclick()

