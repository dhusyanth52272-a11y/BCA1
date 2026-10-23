# Genetic Algorithm
import random

population = ["101101", "110010", "011101", "100111"]

print("Initial Population")
for chromosome in population:
    print(chromosome)

def decode(chromosome):
    return int(chromosome, 2)

def fitness(chromosome):
    x = decode(chromosome)
    return x * x

print("\nFitness:")
for chromosome in population:
    x = decode(chromosome)
    f = fitness(chromosome)
    print(chromosome, "->", x, "->Fitness=", f)

population.sort(key=fitness, reverse=True)

parent1 = population[0]
parent2 = population[1]

print("\nSelected Parents:")
print("Parent 1:", parent1)
print("Parent 2:", parent2)

point = 3
child1 = parent1[:point] + parent2[:point]
child2 = parent2[:point] + parent1[:point]

print("\nCrossover Point:", point)
print("Child 1:", child1)
print("Child 2:", child2)

def mutation(chromosome):
    position = random.randint(0, len(chromosome) - 1)
    bits = list(chromosome)
    bits[position] = "1" if bits[position] == "0" else "0"
    return "".join(bits)

child1 = mutation(child1)
child2 = mutation(child2)

print("\nAfter Mutation:")
print("Child 1:", child1)
print("Child 2:", child2)

new_population = [parent1, parent2, child1, child2]

print("\nNew Population")
for chromosome in new_population:
    print(chromosome, "Fitness=", fitness(chromosome))

# Sample Output (mutation is random, so results vary):
# Initial Population
# 101101
# 110010
# 011101
# 100111
# Fitness:
# 101101 -> 45 ->Fitness= 2025
# 110010 -> 50 ->Fitness= 2500
# 011101 -> 29 ->Fitness= 841
# 100111 -> 39 ->Fitness= 1521
# Selected Parents:
# Parent 1: 110010
# Parent 2: 101101
# Crossover Point: 3
# Child 1: 110101
# Child 2: 101110
# After Mutation:
# Child 1: 110100
# Child 2: 101111
# New Population
# 110010 Fitness= 2500
# 101101 Fitness= 2025
# 110100 Fitness= 2704
# 101111 Fitness= 2209
