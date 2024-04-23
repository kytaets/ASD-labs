import turtle
import random
import math
import time

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
            updated_row = []
            for element in row:
                element *= num
                if element >= 1.4:
                    updated = 1
                else:
                    updated = 0
                updated_row.append(updated)
            result.append(updated_row)
        return result

    T = randMatrix(N)  # creating matrix
    k = 1.0 - n3 * 0.01 - n4 * 0.005 - 0.15
    A = multiplyMatrix(T, k)  # converting matrix into graph

    return A

# Changing dir to undirected matrix
def toUndir(dir_matrix):
    n = len(dir_matrix)

    undirected_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            undirected_matrix[i][j] = dir_matrix[i][j] or dir_matrix[j][i]

    return undirected_matrix


# Drawing vertexes
def drawVertexes(N):

    def drawCircle():
        turtle.goto(pos[0], pos[1] - radius)
        turtle.setheading(360)
        turtle.down()
        turtle.circle(radius)
        turtle.up()
        turtle.goto(pos[0], pos[1] - radius / 1.25)
        turtle.write(f"{number}", False, 'center', ('Arial', 25, 'normal'))

    vert_coordinates = []

    radius = 25
    turn_degree = 360 / (N - 1)
    number = 1

    turtle.up()
    turtle.goto(75, 250)

    for i in range(N - 1):
        heading = turtle.heading()
        pos = turtle.pos()
        vert_coordinates.append(pos)
        drawCircle()

        turtle.goto(pos[0], pos[1])
        turtle.setheading(heading)
        turtle.right(turn_degree)
        turtle.forward(radius*6)
        number += 1

    turtle.goto(0, 0)
    pos = turtle.pos()
    vert_coordinates.append(pos)
    drawCircle()

    return vert_coordinates


# Drawing connections between vertexes
def drawConnections(matrix, vert_coord):

    def drawArrow():
        position = turtle.position()
        turtle.left(135)
        turtle.forward(10)
        turtle.up()
        turtle.goto(position)
        turtle.down()
        turtle.left(90)
        turtle.forward(10)

    def drawLine():
        turtle.up()
        turtle.goto(start)
        angle = turtle.towards(end)
        turtle.setheading(angle)
        turtle.forward(radius)
        turtle.down()

        turtle.forward(turtle.distance(end) - radius)
        drawArrow()

    turtle.speed(3)
    n = len(matrix)
    radius = 25

    for i in range(n):
        start = vert_coord[i]
        for j in range(n):
            end = vert_coord[j]
            # checking if vertexes have connection
            if matrix[i][j]:
                # checking if vertex is not the element itself
                if start != end:
                    drawLine()



def draw(matrix, N, direction=True):
    turtle.speed(0)
    vert_coord = drawVertexes(N)
    drawConnections(matrix, vert_coord)
    print(vert_coord)

def main():
    n3 = 2
    n4 = 2
    N = 10 + n3  # N = 12

    A = createMatrix(n3, n4, N)  # creating dir matrix
    print("Dir Matrix:")
    for i in range(N):
        print(A[i])

    draw(A, N)
    # time.sleep(5)
    # turtle.clear()
    #
    # undirA = toUndir(A)  # creating undirected matrix
    # print("Undirected Matrix:")
    # for i in range(N):
    #     print(undirA[i])
    #
    # draw(undirA, N, False)
    turtle.exitonclick()

main()