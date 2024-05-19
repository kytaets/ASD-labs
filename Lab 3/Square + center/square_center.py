import turtle
import random
import math
import keyboard

# Creating a random matrix
def createMatrix(n3, n4, N):
    # Creating a matrix with random float numbers
    def randMatrix(n):
        random.seed(3219)
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
            updated_row = []
            for element in row:
                element *= num
                if element >= 0.5:
                    updated = 1
                else:
                    updated = 0
                updated_row.append(updated)
            result.append(updated_row)
        return result

    T = randMatrix(N)  # creating matrix
    k = 1.0 - n3 * 0.02 - n4 * 0.005 - 0.20
    A = multiplyMatrix(T, k)  # converting matrix into graph

    return A


# Drawing circles
def drawVertexes():
    vert_coordinates = []
    turtle.up()
    turtle.goto(-300, 200)
    vertexes_on_side = 3
    k = -1
    angle = 360
    number = 1

    for i in range(4):
        for j in range(vertexes_on_side):
            turtle.forward(200)
            # adding coordinates to the list of coordinates
            vert_coordinates.append(turtle.position())
            # going to the center
            turtle.setheading(270)
            turtle.forward(25)
            turtle.setheading(360)
            # drawing a circle
            turtle.down()
            turtle.circle(25)
            turtle.up()
            # writing a number of vertex
            turtle.write(f"{number}", False, 'center', ('Arial', 25, 'normal'))
            number += 1
            # going back to the center
            turtle.setheading(90)
            turtle.forward(25)
            turtle.setheading(angle)

        turtle.right(90)
        angle -= 90
        vertexes_on_side += k
        k *= -1

    turtle.goto(0, 0)
    vert_coordinates.append((0, 0))
    turtle.setheading(270)
    turtle.forward(25)
    turtle.setheading(360)
    turtle.down()
    turtle.circle(25)
    turtle.up()
    turtle.write(f"{number}", False, 'center', ('Arial', 25, 'normal'))
    number += 1

    return vert_coordinates


# Drawing arrow
def arrow():
    position = turtle.position()
    turtle.left(135)
    turtle.forward(10)
    turtle.up()
    turtle.goto(position)
    turtle.down()
    turtle.left(90)
    turtle.forward(10)


def simple_line(frm_coord, to_coord):
    turtle.goto(frm_coord)
    turtle.setheading(turtle.towards(to_coord))
    turtle.forward(25)
    turtle.down()
    turtle.forward(turtle.distance(to_coord) - 25)
    arrow()
    turtle.up()

# Drawing lines between circles
def drawLines(from_el, to_el, coords):
    frm_coord = coords[from_el]
    to_coord = coords[to_el]

    # When line goes to the element itself
    if from_el == to_el:
        turtle.goto(frm_coord)
        turtle.setheading(90)
        turtle.forward(25)
        turtle.setheading(360)
        turtle.down()
        turtle.circle(25)
        arrow()
        turtle.up()

    else:
        # When the line goes from the center
        if from_el == len(coords):
            simple_line(frm_coord, to_coord)

        # When the line goes from the first to the 10th el
        if (from_el == len(coords)-1 and to_el == 0) or (to_el == len(coords)-1 and frm_coord == 0):
            simple_line(frm_coord, to_coord)

        # When the line lies between neighbours
        if abs(from_el - to_el) == 1:
            simple_line(frm_coord, to_coord)

        # When the line lies between same y
        if frm_coord[1] == to_coord[1]:
            print("Same y")
            if frm_coord[1] < 0:
                print(frm_coord, to_coord, "-")
            else:
                print(frm_coord, to_coord, "+")

        # When the line lies between same x
        if frm_coord[0] == to_coord[0]:
            print("Same x")
            if frm_coord[0] < 0:
                print(frm_coord, to_coord, "-")
            else:
                print(frm_coord, to_coord, "+")


# def drawConnections(row, element, vertexes, direction=True):
#     # Drawing arrow
#     def drawArrow():
#         position = turtle.position()
#         turtle.left(135)
#         turtle.forward(10)
#         turtle.up()
#         turtle.goto(position)
#         turtle.down()
#         turtle.left(90)
#         turtle.forward(10)
#
#     # Calculating a part of broken line
#     def calculateLine(distance, degrees):
#         rad = math.radians(degrees)
#         b = distance / 2 / math.cos(rad)
#         return b
#
#     # Calculating the point of the start/end
#     def gotoPoint(position, x, y, diagonal=True):
#         k = 1
#         if not diagonal:
#             k = -1
#         if position == "hor":
#             is_negative = y / abs(y)
#             start = y - 25 * k * is_negative
#             result = (x, start)
#         elif position == "vert":
#             is_negative = x / abs(x)
#             start = x - 25 * k * is_negative
#             result = (start, y)
#         else:
#             is_negative_x = x / abs(x)
#             is_negative_y = y / abs(y)
#             start_x = x - 25 * k * math.cos(0.785) * is_negative_x
#             start_y = y - 25 * k * math.cos(0.785) * is_negative_y
#             result = (start_x, start_y)
#
#         return result
#
#     # Drawing diagonal connections
#     def drawDiagonal(row, el, direction):
#         position = row.position
#         x = row.pos_x
#         y = row.pos_y
#
#         turtle.up()
#         turtle.goto(gotoPoint(position, x, y))
#         turtle.down()
#
#         position = el.position
#         x = el.pos_x
#         y = el.pos_y
#         turtle.setheading(turtle.towards(x, y))
#         goto_coord = gotoPoint(position, x, y)
#         # drawing simple line if there is no connection
#         if row.number not in el.connections:
#             turtle.goto(goto_coord)
#             if direction:
#                 drawArrow()
#         # drawing broken line if there is a connection
#         elif row.number in el.connections and not direction:
#             return
#         else:
#             # calculating two parts of a line
#             distance = turtle.distance(goto_coord)
#             degrees = 10
#             rad = math.radians(degrees)
#             b = distance / 2 / math.cos(rad)
#
#             turtle.right(degrees)
#             turtle.forward(b)
#             turtle.setheading(turtle.towards(goto_coord))
#             turtle.goto(goto_coord)
#             drawArrow()
#
#         row.connections.append(el.number)
#
#     # Drawing neighbour connections
#     def drawNeighbours(row, el, direction):
#         distance = 50
#
#         # Going to start point
#         turtle.up()
#         turtle.goto(row.pos_x, row.pos_y)
#         turtle.setheading(turtle.towards(el.pos_x, el.pos_y))
#         turtle.forward(25)
#         turtle.down()
#
#         # drawing simple line if there is no connection
#         if row.number not in el.connections:
#             turtle.forward(distance)
#             if direction:
#                 drawArrow()
#         # drawing broken line if there is a connection
#         elif row.number in el.connections and direction:
#             # calculating two parts of a line
#             degrees = 30
#             b = calculateLine(distance, degrees)
#
#             turtle.right(degrees)
#             turtle.forward(b)
#             turtle.left(degrees * 2)
#             turtle.forward(b)
#             drawArrow()
#
#         # adding this element to connections of row element
#         row.connections.append(el.number)
#
#     # Drawing horizontal connections
#     def drawHor(row, el, direction):
#         degrees = 10
#
#         turtle.up()
#         turtle.goto(row.pos_x, row.pos_y)
#         turtle.setheading(turtle.towards(el.pos_x, el.pos_y))
#
#         # drawing more curved line if there is a connection
#         if row.number in el.connections and direction:
#             degrees += 10
#         # drawing nothing if there is a connection and no direction
#         elif row.number in el.connections and not direction:
#             return
#         # drawing next element
#         if row.number < el.number:
#             turtle.left(degrees)
#             if row.pos_x < el.pos_x:
#                 turtle.goto(row.pos_x, row.pos_y + 25)
#             else:
#                 turtle.goto(row.pos_x, row.pos_y - 25)
#
#         # drawing previous element
#         else:
#             turtle.right(degrees)
#             # checking order of elements (from left to right)
#             if row.pos_x < el.pos_x:
#                 turtle.goto(row.pos_x, row.pos_y - 25)
#             # (from right to left)
#             else:
#                 turtle.goto(row.pos_x, row.pos_y + 25)
#
#         distance = turtle.distance(el.pos_x, el.pos_y)
#         is_negative = el.pos_y / abs(el.pos_y)
#         goto_y = el.pos_y + 25 * is_negative
#         b = calculateLine(distance, degrees)
#
#         turtle.down()
#         turtle.forward(b)
#         turtle.setheading(turtle.towards(el.pos_x, goto_y))
#         turtle.goto(el.pos_x, goto_y)
#         if direction:
#             drawArrow()
#
#         row.connections.append(el.number)
#
#     # Drawing vertical connections
#     def drawVert(row, el, direction):
#         degrees = 10
#
#         turtle.up()
#         turtle.goto(row.pos_x, row.pos_y)
#         turtle.setheading(turtle.towards(el.pos_x, el.pos_y))
#         # drawing more curved line if there is a connection
#         if row.number in el.connections and direction:
#             degrees += 10
#         # drawing nothing if there is a connection and no direction
#         elif row.number in el.connections and not direction:
#             return
#
#         # drawing next element
#         if (row.number < el.number and row.number != 0) or el.number == 0:
#             turtle.left(degrees)
#             # checking order of elements (from left to right)
#             if row.pos_y > el.pos_y:
#                 turtle.goto(row.pos_x + 25, row.pos_y)
#             # (from right to left)
#             else:
#                 turtle.goto(row.pos_x - 25, row.pos_y)
#
#         # drawing previous element
#         else:
#             turtle.right(degrees)
#             if row.pos_y > el.pos_y:
#                 turtle.goto(row.pos_x - 25, row.pos_y)
#             else:
#                 turtle.goto(row.pos_x + 25, row.pos_y)
#
#         distance = turtle.distance(el.pos_x, el.pos_y)
#         is_negative = el.pos_x / abs(el.pos_x)
#         goto_x = el.pos_x + 25 * is_negative
#         b = calculateLine(distance, degrees)
#
#         turtle.down()
#         turtle.forward(b)
#         turtle.setheading(turtle.towards(goto_x, el.pos_y))
#         turtle.goto(goto_x, el.pos_y)
#         if direction:
#             drawArrow()
#
#         row.connections.append(el.number)
#
#     # Drawing connection with itself
#     def drawSelf(row, direction):
#         position = row.position
#         x = row.pos_x
#         y = row.pos_y
#
#         turtle.up()
#         turtle.goto(gotoPoint(position, x, y, False))
#         turtle.down()
#         turtle.setheading(turtle.towards(x, y) + 90)
#
#         turtle.color("red")
#         turtle.circle(20)
#         if direction:
#             drawArrow()
#         turtle.color("black")
#
#     # checking if vertex is not the element itself
#     if row != element:
#         # moving through neighbours
#         diff = len(vertexes) / 4 - abs(row.number - element.number)
#         if (row.number == 0 or element.number == 0) and row.pos_x == element.pos_x:
#             diff = 1
#
#         if row.next_el == element.number or row.prev_el == element.number:
#             drawNeighbours(row, element, direction)
#
#         # moving through the same y-es
#         elif row.pos_y == element.pos_y and diff >= 0:
#             drawHor(row, element, direction)
#
#         # moving through the same x-es
#         elif row.pos_x == element.pos_x and diff >= 0:
#             drawVert(row, element, direction)
#
#         # moving through diagonal elements
#         else:
#             drawDiagonal(row, element, direction)
#
#     # drawing connection with element itself
#     else:
#         drawSelf(row, direction)


# Drawing vertexes connections
# def drawGraph(matrix, vertexes, direction=True):
#     for i in range(len(matrix)):
#         turtle.speed(0)
#         row = vertexes[i]
#         for j in range(len(matrix[i])):
#             element = vertexes[j]
#             # checking if vertexes have connection
#             if matrix[i][j]:
#                 drawConnections(row, element, vertexes, direction)


# The main draw function
def draw(matrix, length, direction=True):
    turtle.speed(0)
    turtle.color("black")
    coords = drawVertexes()
    print(coords)
    for i in range(length):
        for j in range(length):
            if matrix[i][j]:
                drawLines(i, j, coords)


n3 = 1
n4 = 9
N = 10 + n3  # N = 11
matrixA = createMatrix(n3, n4, N)

print("Dir Matrix:")
for i in range(N):
    print(matrixA[i])
print()

draw(matrixA, N)
# keyboard.wait("r")
# turtle.clear()

turtle.exitonclick()


