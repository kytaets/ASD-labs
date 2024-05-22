import turtle
import random
import math
import keyboard

# Creating a matrix with random float numbers
def matr_random(n):
    random.seed(3222)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.uniform(0, 2))
        matrix.append(row)
    return matrix


# Multiplying matrix by number
def multiply_matrix_by(matrix, num=1):
    result = []
    for row in matrix:
        updated_row = []
        for element in row:
            element *= num
            if element >= 1.5:
                updated = 1
            else:
                updated = 0
            updated_row.append(updated)
        result.append(updated_row)
    return result


# Changing dir to undirected matrix
def undir_matr(dir_matrix):
    n = len(dir_matrix)

    undirected_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            undirected_matrix[i][j] = dir_matrix[i][j] or dir_matrix[j][i]

    return undirected_matrix


# Creating matrix
def build_matrix(n3, n4, N):

    T = matr_random(N)  # creating matrix
    k = 1.0 - n3 * 0.01 - n4 * 0.005 - 0.05
    A = multiply_matrix_by(T, k)  # converting matrix into graph

    return A


# Drawing circles
def draw_vertexes():
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
def draw_lines(from_el, to_el, coords, direction):
    frm_coord = coords[from_el]
    to_coord = coords[to_el]

    if from_el == 5:
        print("5:", from_el, to_el)

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
        elif (from_el == len(coords)-1 and to_el == 0) or (to_el == len(coords)-1 and frm_coord == 0):
            simple_line(frm_coord, to_coord, direction)

        # When the line lies between neighbours
        elif abs(from_el - to_el) == 1:
            simple_line(frm_coord, to_coord, direction)

        # When the line lies between same y
        elif frm_coord[1] == to_coord[1]:
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
        elif frm_coord[0] == to_coord[0]:
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

        elif abs(frm_coord[0]) == abs(to_coord[0]) and abs(frm_coord[1]) == abs(to_coord[1]):
            turtle.goto(frm_coord)
            angle = turtle.towards(to_coord)
            turtle.setheading(angle)
            turtle.forward(25)

            distance = turtle.distance(to_coord) - 25
            rad = math.radians(10)
            side = distance / 2 / math.cos(rad)

            turtle.setheading(angle + 10)
            turtle.down()
            turtle.forward(side)
            turtle.setheading(angle - 10)
            turtle.forward(side)
            if direction:
                arrow()
            turtle.up()

        else:
            turtle.goto(frm_coord)
            turtle.setheading(turtle.towards(to_coord))
            turtle.forward(25)

            turtle.down()
            turtle.forward(turtle.distance(to_coord) - 25)
            if direction:
                arrow()
            turtle.up()


def draw(matrix, length, direction=True):
    turtle.speed(0)
    turtle.color("black")
    coords = draw_vertexes()
    for i in range(length):
        for j in range(length):
            if matrix[i][j]:
                draw_lines(i, j, coords, direction)

    return coords


def drawSimpleCircle(element, coords):
    turtle.goto(coords[element][0], coords[element][1] - 25)
    turtle.setheading(360)
    turtle.down()
    turtle.circle(25)
    turtle.up()


# Class for weighted vertexes
class WeightedVertex:
    def __init__(self, vertexes, weight):
        self.vertexes = vertexes
        self.weight = weight
        self.next = None


def prim_tree(matrix, coords):
    def elementProduct(matrix1, matrix2, k=1):
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(round(matrix1[i][j] * matrix2[i][j] * k))
            result.append(row)

        return result

    def symmetricMatrix(matrix):
        result = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                if matrix[i][j] != matrix[j][i]:
                    row.append(1)
                else:
                    row.append(0)
            result.append(row)

        return result

    def triangularMatrix(n):
        matrix = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] = 1

        return matrix

    def creareD(matrix):
        result = []
        for row in matrix:
            updated_row = []
            for element in row:
                if element > 0:
                    updated = 1
                else:
                    updated = 0
                updated_row.append(updated)
            result.append(updated_row)
        return result

    def createW():
        result = []
        for i in range(len(matrixD)):
            row = []
            for j in range(len(matrixD[0])):
                row.append((matrixD[i][j] + matrixH[i][j] * matrixTr[i][j]) * matrixC[i][j])
            result.append(row)

        for i in range(N):
            for j in range(N):
                result[i][j] = result[j][i]

        return result

    length = len(matrixA)
    matrixB = matr_random(length)
    matrixC = elementProduct(matrixA, matrixB, 100)
    matrixD = creareD(matrixC)
    matrixH = symmetricMatrix(matrixD)
    matrixTr = triangularMatrix(length)

    matrixW = createW()
    print("Weighted Matrix:")
    for i in range(length):
        for j in range(length):
            print(matrixW[i][j], end='\t')
        print()
    print()

    turtle.color("Red")
    turtle.pensize(3)
    turtle.speed(3)

    vertexes = [0]

    for i in range(length):
        row = vertexes[-1]
        col = 0
        min_weight = 0
        print("Min weight:", min_weight)
        for j in range(length):
            if j not in vertexes:
                print("To:", j)
                if min_weight == 0:
                    min_weight = matrixW[row][j]
                    col = j
                elif matrixW[row][j] != 0 and matrixW[row][j] < min_weight:
                    min_weight = matrixW[row][j]
                    col = j

        vertexes.append(col)
        print(vertexes)
        print(row, col)
        keyboard.wait("Space")
        drawSimpleCircle(row, coords)
        keyboard.wait("Space")
        draw_lines(row, col, coords, False)
        keyboard.wait("Space")
        drawSimpleCircle(col, coords)









n3 = 1
n4 = 9
N = 10 + n3

matrixA = build_matrix(n3, n4, N)
matrix_un = undir_matr(matrixA)                    # creating undirected matrix
print("Undirected Matrix:")
for i in range(N):
    print(matrix_un[i])

coords = draw(matrix_un, N, False)
print("Undirected graph has built.")

# input("Press enter to build tree...")
keyboard.wait("Space")
prim_tree(matrix_un, coords)


turtle.exitonclick()

