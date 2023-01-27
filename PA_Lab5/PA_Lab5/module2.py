import random

#генерує матрицю з усіма відстанями між точками
def generate_table(nodes_amount):
    matrix = []
    for i in range(nodes_amount):
        matrix.append([])
        for j in range(nodes_amount):
            matrix[i].append(random.randint(5, 150))
    return matrix

#генерує матрицю з відстанями між кожними двома точками, між якими летіла бджола
def generate_bees():
    bees = []
    for i in range(20):
        bees.append([])
    return bees

#генерує матрицю зі шляхом з точок, через які пролетіла бджола
def generate_bee_ways():
    bee_ways = []
    for i in range(20):
        bee_ways.append([])
        bee_ways[i].append(0)
    return bee_ways

#обчислює повну відстань, пройдену бджолою
def calculate_distance(bee):
    distance = 0
    for node in bee:
        distance = distance + node
    return distance
