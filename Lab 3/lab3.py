import turtle
import random
import math
import time


# Structure class of vertexes of graph
class Vertex:
    def __init__(self, number, pos_x, pos_y, position, next_el, prev_el):
        self.number = number
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = position
        self.next_el = next_el
        self.prev_el = prev_el
        self.connections = []


# Creating matrix
def createMatrix(n3, n4, N):
    # Creating a matrix with random float numbers
    def randMatrix(n):
        random.seed(3222)
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(random.uniform(0, 2))
            matrix.append(row)
        return matrix

    # Multiplying matrix by number
    def multiplyMatrix(matrix, num):
        result = []
        for row in matrix:
            updated = [round(element * num) for element in row]  # rounding element
            result.append(updated)
        return result

    T = randMatrix(N)                           # creating matrix
    k = 1.0 - n3 * 0.02 - n4 * 0.005 - 0.25     # creating multiplier
    A = multiplyMatrix(T, k)                    # converting matrix into graph

    return A

# Changing dir to undirected matrix
def toUndir(dir_matrix):
    n = len(dir_matrix)

    undirected_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            undirected_matrix[i][j] = dir_matrix[i][j] or dir_matrix[j][i]

    return undirected_matrix


# Creating list of vertexes
def createPositions(N):
    vertexes = []
    sides = int(N/4)
    x = -150
    y = 150
    position = "angle"

    for i in range(N):
        prev = i - 1
        next_el = i + 1
        if i == 0:
            prev = N-1
        elif i == N - 1:
            next_el = 0

        if i % sides == 0:
            position = "angle"

        vert = Vertex(i, x, y, position, next_el, prev)
        vertexes.append(vert)

        if i < sides:
            x += 100
            position = "hor"
        elif sides <= i < sides*2:
            y -= 100
            position = "vert"
        elif sides*2 <= i < sides*3:
            x -= 100
            position = "hor"
        elif i >= sides*3:
            y += 100
            position = "vert"

    return vertexes


# Writing numbers in circles
def writeNumbers(N):
    sides = int(N/4)
    number = 1
    for i in range(4):
        for j in range(sides):
            turtle.write(f"{number}", False, 'center', ('Arial', 25, 'normal'))
            turtle.up()
            turtle.forward(100)
            turtle.down()
            number += 1

        turtle.up()
        turtle.right(90)
        turtle.down()


# Drawing circles
def drawCircles(N):
    sides = int(N/4)
    turtle.up()
    turtle.goto(-150, 125)
    turtle.setheading(360)
    turtle.down()
    for i in range(4):
        for j in range(sides):
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

    writeNumbers(N)


# Drawing arrow
def drawArrow():
    position = turtle.position()
    turtle.left(135)
    turtle.forward(10)
    turtle.up()
    turtle.goto(position)
    turtle.down()
    turtle.left(90)
    turtle.forward(10)


# Calculating a part of broken line
def calculateLine(distance, degrees):
    rad = math.radians(degrees)
    b = distance / 2 / math.cos(rad)
    return b


# Calculating the point of the start/end
def gotoPoint(position, x, y, diagonal=True):
    k = 1
    if not diagonal:
        k = -1
    if position == "hor":
        is_negative = y / abs(y)
        start = y - 25*k * is_negative
        result = (x, start)
    elif position == "vert":
        is_negative = x / abs(x)
        start = x - 25*k * is_negative
        result = (start, y)
    else:
        is_negative_x = x / abs(x)
        is_negative_y = y / abs(y)
        start_x = x - 25*k * math.cos(0.785) * is_negative_x
        start_y = y - 25*k * math.cos(0.785) * is_negative_y
        result = (start_x, start_y)

    return result


# Drawing diagonal connections
def drawDiagonal(row, el, direction):
    position = row.position
    x = row.pos_x
    y = row.pos_y

    turtle.up()
    turtle.goto(gotoPoint(position, x, y))
    turtle.down()

    position = el.position
    x = el.pos_x
    y = el.pos_y
    turtle.setheading(turtle.towards(x, y))
    goto_coord = gotoPoint(position, x, y)
    # drawing simple line if there is no connection
    if row.number not in el.connections:
        turtle.goto(goto_coord)
        if direction:
            drawArrow()
    # drawing broken line if there is a connection
    elif row.number in el.connections and not direction:
        return
    else:
        # calculating two parts of a line
        distance = turtle.distance(goto_coord)
        degrees = 10
        rad = math.radians(degrees)
        b = distance / 2 / math.cos(rad)

        turtle.color("orange")
        turtle.right(degrees)
        turtle.forward(b)
        turtle.setheading(turtle.towards(goto_coord))
        turtle.goto(goto_coord)
        drawArrow()
        turtle.color("black")

    row.connections.append(el.number)


# Drawing neighbour connections
def drawNeighbours(row, el, direction):
    distance = 50

    # Going to start point
    turtle.up()
    turtle.goto(row.pos_x, row.pos_y)
    turtle.setheading(turtle.towards(el.pos_x, el.pos_y))
    turtle.forward(25)
    turtle.down()

    # drawing simple line if there is no connection
    if row.number not in el.connections:
        turtle.forward(distance)
        if direction:
            drawArrow()
    # drawing broken line if there is a connection
    elif row.number in el.connections and direction:
        # calculating two parts of a line
        degrees = 30
        b = calculateLine(distance, degrees)

        turtle.color("blue")
        turtle.right(degrees)
        turtle.forward(b)
        turtle.left(degrees * 2)
        turtle.forward(b)
        drawArrow()
        turtle.color("black")

    # adding this element to connections of row element
    row.connections.append(el.number)


# Drawing horizontal connections
def drawHor(row, el, direction):
    degrees = 10

    turtle.up()
    turtle.goto(row.pos_x, row.pos_y)
    turtle.setheading(turtle.towards(el.pos_x, el.pos_y))

    # drawing more curved line if there is a connection
    if row.number in el.connections and direction:
        degrees += 10
        turtle.color("red")
    # drawing nothing if there is a connection and no direction
    elif row.number in el.connections and not direction:
        return
    # drawing next element
    if row.number < el.number:
        turtle.left(degrees)
        if row.pos_x < el.pos_x:
            turtle.goto(row.pos_x, row.pos_y + 25)
        else:
            turtle.goto(row.pos_x, row.pos_y - 25)

    # drawing previous element
    else:
        turtle.right(degrees)
        # checking order of elements (from left to right)
        if row.pos_x < el.pos_x:
            turtle.goto(row.pos_x, row.pos_y - 25)
        # (from right to left)
        else:
            turtle.goto(row.pos_x, row.pos_y + 25)

    distance = turtle.distance(el.pos_x, el.pos_y)
    is_negative = el.pos_y / abs(el.pos_y)
    goto_y = el.pos_y + 25 * is_negative
    b = calculateLine(distance, degrees)

    turtle.down()
    turtle.forward(b)
    turtle.setheading(turtle.towards(el.pos_x, goto_y))
    turtle.goto(el.pos_x, goto_y)
    if direction:
        drawArrow()

    row.connections.append(el.number)
    turtle.color("black")


# Drawing vertical connections
def drawVert(row, el, direction):
    degrees = 10

    turtle.up()
    turtle.goto(row.pos_x, row.pos_y)
    turtle.setheading(turtle.towards(el.pos_x, el.pos_y))
    # drawing more curved line if there is a connection
    if row.number in el.connections and direction:
        degrees += 10
        turtle.color("red")
    # drawing nothing if there is a connection and no direction
    elif row.number in el.connections and not direction:
        return

    # drawing next element
    if row.number < el.number:
        turtle.left(degrees)
        # checking order of elements (from left to right)
        if row.pos_y > el.pos_y:
            turtle.goto(row.pos_x + 25, row.pos_y)
        # (from right to left)
        else:
            turtle.goto(row.pos_x - 25, row.pos_y)

    # drawing previous element
    else:
        turtle.right(degrees)
        if row.pos_y > el.pos_y:
            turtle.goto(row.pos_x - 25, row.pos_y)
        else:
            turtle.goto(row.pos_x + 25, row.pos_y)

    distance = turtle.distance(el.pos_x, el.pos_y)
    is_negative = el.pos_x / abs(el.pos_x)
    goto_x = el.pos_x + 25 * is_negative
    b = calculateLine(distance, degrees)

    turtle.down()
    turtle.forward(b)
    turtle.setheading(turtle.towards(goto_x, el.pos_y))
    turtle.goto(goto_x, el.pos_y)
    if direction:
        drawArrow()

    row.connections.append(el.number)
    turtle.color("black")


# Drawing connection with itself
def drawSelf(row, direction):
    position = row.position
    x = row.pos_x
    y = row.pos_y

    turtle.up()
    turtle.goto(gotoPoint(position, x, y, False))
    turtle.down()
    turtle.setheading(turtle.towards(x, y) + 90)

    turtle.color("green")
    turtle.circle(20)
    if direction:
        drawArrow()
    turtle.color("black")


# Drawing vertexes connections
def drawConnections(matrix, vertexes, direction=True):
    for i in range(len(matrix)):
        row = vertexes[i]
        for j in range(len(matrix[i])):
            element = vertexes[j]
            # checking if vertexes have connection
            if matrix[i][j]:
                # checking if vertex is not the element itself
                if row != element:
                    # moving through neighbours
                    diff = len(vertexes) / 4 - abs(row.number - element.number)
                    if row.next_el == element.number or row.prev_el == element.number:
                        drawNeighbours(row, element, direction)

                    # moving through the same y-es
                    elif row.pos_y == element.pos_y and diff >= 0:
                        drawHor(row, element, direction)

                    # moving through the same x-es
                    elif row.pos_x == element.pos_x and diff >= 0:
                        drawVert(row, element, direction)

                    # moving through diagonal elements
                    elif row.pos_y != element.pos_y and row.pos_x != element.pos_x:
                        drawDiagonal(row, element, direction)

                # drawing connection with element itself
                else:
                    drawSelf(row, direction)


# The main draw function
def draw(A, N, direction=True):
    turtle.speed(0)
    drawCircles(N)
    vertexes = createPositions(N)
    drawConnections(A, vertexes, direction)


def main():
    n3 = 2
    n4 = 2
    N = 10 + n3  # N = 12

    A = createMatrix(n3, n4, N)             # creating dir matrix
    print("Dir Matrix:")
    for i in range(N):
        print(A[i])

    draw(A, N)
    time.sleep(5)
    turtle.clear()

    undirA = toUndir(A)                    # creating undirected matrix
    print("Undirected Matrix:")
    for i in range(N):
        print(undirA[i])

    draw(undirA, N, False)
    turtle.exitonclick()


main()
