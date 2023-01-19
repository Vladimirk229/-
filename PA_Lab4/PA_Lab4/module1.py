import random

def generate_things(min_price, max_price, min_weight, max_weight, things_amount):
    things = []
    for i in range(things_amount):
        things.append([random.randint(min_price, max_price), random.randint(min_weight, max_weight)])
    return things

def get_sum(population, things):
    sum = 0
    i = 0
    for p in population:
        if p == 1:
            sum = sum + things[i][1]
        i = i + 1
    return sum

def generate_population(genes_amount, things):
    population = []
    for i in range(5):
        population.append([])
        for j in range(genes_amount):
            if get_sum(population[i], things) <= 250:
                population[i].append(random.randint(0,1))
            else:
                population[i].append(0)
            if get_sum(population[i], things) > 250:
                population[i].pop()
                population[i].append(0)
    return population

def get_price(population, things):
    sum = 0
    for k in range(100):
        if population[k] == True:
            sum = sum + things[k][0]
    return sum

def mutation(population, mutation_chance):
    chance = random.randint(0, 100)
    if chance <= mutation_chance:
        first_gene = random.randint(0, 99)
        second_gene = random.randint(0, 99)
        buf = population[first_gene]
        population[first_gene] = population[second_gene]
        population[second_gene] = buf
    return population

def best_population(population, things):
    index = 0
    count = 0
    for row in population:
        if get_price(row, things) >= get_price(population[index], things):
            index = count
        count = count + 1
    return index
