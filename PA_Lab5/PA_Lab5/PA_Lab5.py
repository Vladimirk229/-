import random
import module2

distance_matrix = module2.generate_table(300)

bees = module2.generate_bees()
bee_ways = module2.generate_bee_ways()
count = 0
for bee in bees:
    current_node = 0
    next_node = 0
    uncompleted_nodes = []
    k = 1
    while k < 300:
        uncompleted_nodes.append(k)
        k = k + 1
    for i in range(299):
        next_node = random.choice(uncompleted_nodes)
        bee.append(distance_matrix[current_node][next_node])
        uncompleted_nodes.remove(next_node)
        bee_ways[count].append(next_node)
        current_node = next_node
    print("Bee", count)
    print("Distance =", module2.calculate_distance(bee))
    count = count + 1

best_bee = 0
count = 0
for bee in bees:
    if module2.calculate_distance(bee) < module2.calculate_distance(bees[best_bee]):
        best_bee = count
    count = count + 1

print("The best bee is bee №",best_bee)
print("Distance =", module2.calculate_distance(bees[best_bee]))
print("Way:")
print(bee_ways[best_bee])
print("Number of bees:", 20)
print("Number of nodes:", 300)