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
                if element >= 0.2:
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


def toUndir(dir_matrix):
    n = len(dir_matrix)

    undirected_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            undirected_matrix[i][j] = dir_matrix[i][j] or dir_matrix[j][i]

    return undirected_matrix


# Drawing circles
def drawVertexes():
    vert_coordinates = []
    turtle.up()
    turtle.goto(-300, 200)
    turtle.setheading(360)
    vertexes_on_side = 3
    k = -1
    angle = 360
    number = 1

    for i in range(4):
        for j in range(vertexes_on_side):
            turtle.forward(200)
            # adding coordinates to the list of coordinates
            position = turtle.position()
            rounded_position = (round(position[0]), round(position[1]))
            vert_coordinates.append(rounded_position)
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


def simple_line(frm_coord, to_coord, direction):
    turtle.goto(frm_coord)
    turtle.setheading(turtle.towards(to_coord))
    turtle.forward(25)
    turtle.down()
    turtle.forward(turtle.distance(to_coord) - 25)
    if direction:
        arrow()
    turtle.up()

# Drawing lines between circles
def drawLines(from_el, to_el, coords, direction):
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
        if direction:
            arrow()
        turtle.up()

    else:
        # When the line goes from the center
        if from_el == len(coords):
            simple_line(frm_coord, to_coord, direction)

        # When the line goes from the first to the 10th el
        if (from_el == len(coords)-1 and to_el == 0) or (to_el == len(coords)-1 and frm_coord == 0):
            simple_line(frm_coord, to_coord, direction)

        # When the line lies between neighbours
        if abs(from_el - to_el) == 1:
            simple_line(frm_coord, to_coord, direction)

        # When the line lies between same y
        if frm_coord[1] == to_coord[1]:
            turtle.goto(frm_coord)
            angle = turtle.towards(to_coord)
            distance = turtle.distance(to_coord)

            rad = math.radians(20)
            side = distance / 2 / math.cos(rad)

            if frm_coord[1] >= 0:
                turtle.setheading(90)
                turtle.forward(25)

                if frm_coord[0] > to_coord[0]:
                    turtle.setheading(angle - 20)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle + 20)
                else:
                    turtle.setheading(angle + 20)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle - 20)

            else:
                turtle.setheading(270)
                turtle.forward(25)

                if frm_coord[0] > to_coord[0]:
                    turtle.setheading(angle + 20)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle - 20)
                else:
                    turtle.setheading(angle - 20)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle + 20)

            turtle.forward(side)
            if direction:
                arrow()
            turtle.up()

        # When the line lies between same x
        if frm_coord[0] == to_coord[0]:
            turtle.goto(frm_coord)
            angle = turtle.towards(to_coord)
            distance = turtle.distance(to_coord)

            rad = math.radians(10)
            side = distance / 2 / math.cos(rad)

            if frm_coord[0] <= 0:
                turtle.setheading(180)
                turtle.forward(25)

                if frm_coord[1] > to_coord[1]:
                    turtle.setheading(angle - 10)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle + 10)

                else:
                    turtle.setheading(angle + 10)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle - 10)
            else:
                turtle.setheading(360)
                turtle.forward(25)

                print(frm_coord, to_coord)
                keyboard.wait("Space")
                if frm_coord[1] > to_coord[1]:
                    turtle.setheading(angle + 10)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle - 10)

                else:
                    turtle.setheading(angle - 10)
                    turtle.down()
                    turtle.forward(side)
                    turtle.setheading(angle + 10)

            turtle.forward(side)
            if direction:
                arrow()
            turtle.up()


def draw(matrix, length, direction=True):
    turtle.speed(0)
    turtle.color("black")
    coords = drawVertexes()
    print(coords)
    for i in range(length):
        for j in range(length):
            if matrix[i][j]:
                drawLines(i, j, coords, direction)


n3 = 1
n4 = 9
N = 10 + n3  # N = 11
matrixA = createMatrix(n3, n4, N)

print("Dir Matrix:")
for i in range(N):
    print(matrixA[i])
print()

draw(matrixA, N)
print("Directed graph has built.")
keyboard.wait("r")
turtle.clear()

matrix_un = toUndir(matrixA)                    # creating undirected matrix
print("Undirected Matrix:")
for i in range(N):
    print(matrix_un[i])

draw(matrix_un, N, False)
turtle.exitonclick()

