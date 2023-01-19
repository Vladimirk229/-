import random
import module1

bag_size = 250
things_amount = 100
population_size = 5
things = module1.generate_things(2, 30, 1, 25, things_amount)
print('Generated array of things:')
for row in things:
    print('Price:', row[0], 'Weight:', row[1])

population = module1.generate_population(things_amount, things)
print('\n',"Start population:")
for row in population:
    print(row)

result = population[module1.best_population(population, things)]
for i in range(1000):
    first_population = population[module1.best_population(population, things)]
    second_population = population[random.randint(0, population_size - 1)]
    new_population = []
    for j in range(100):
        if j < 30:
            new_population.append(first_population[j])
        else:
            new_population.append(second_population[j])
    new_population = module1.mutation(new_population, 5)
    population.append(new_population)
    if module1.get_sum(population[module1.best_population(population, things)], things) <= 250:
        result = population[module1.best_population(population, things)]
    if i % 20 == 0:
        print("Iteration", i, "Weight =", module1.get_sum(result, things), "Price =", module1.get_price(result, things))
        print(result)
        print("New weight =", module1.get_sum(new_population, things), "New price =", module1.get_price(new_population, things))
        print(result)
    population_size = population_size + 1

print("The best set:")
print(result)
print("Sum =", module1.get_sum(result, things), "Price =",  module1.get_price(result, things))