import random

#������ ������� � ���� ��������� �� �������
def generate_table(nodes_amount):
    matrix = []
    for i in range(nodes_amount):
        matrix.append([])
        for j in range(nodes_amount):
            matrix[i].append(random.randint(5, 150))
    return matrix

#������ ������� � ��������� �� ������� ����� �������, �� ����� ����� ������
def generate_bees():
    bees = []
    for i in range(20):
        bees.append([])
    return bees

#������ ������� � ������ � �����, ����� �� �������� ������
def generate_bee_ways():
    bee_ways = []
    for i in range(20):
        bee_ways.append([])
        bee_ways[i].append(0)
    return bee_ways

#�������� ����� �������, �������� �������
def calculate_distance(bee):
    distance = 0
    for node in bee:
        distance = distance + node
    return distance
