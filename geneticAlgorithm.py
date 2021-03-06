from __future__ import division
import math
import random
import timeit

start = timeit.default_timer()
import matplotlib.pyplot as plt

time = 0
POPULATION_SIZE = 40
P_OF_MUTATION = 0.25
P_OF_CROSSOVER = 0.25
avg_fitness = []


# Randomize the initial population
# with random chromosomes
def initializePopulation(size):
    population = []
    for i in range(size):
        chromosome = []
        for i in range(10):
            gene = random.randint(0, 1)
            chromosome.append(gene)
        population.append(chromosome)
    return population


# Convert binary value to decimal
# Used to create the chromosomes
# of decimal values
def bin2dec(binary):
    y = 0
    for j in binary:
        y = str(y) + str(j)
    return int(y, 2)


# Calculate the Y value for fitness evaluation on
# the function to be optimized
def fitness(x):
    y = (-1 / 10000) * x * (x - 1023) + 5 * math.sin(x / 8) * math.cos(x / 19)
    return y


# Get fitness values and return chromosome list
# based on highest fitness value
def get_fitness_list(chromosomes):
    fitness_list = []
    for chromosome in chromosomes:
        chrom_fitness = fitness(bin2dec(chromosome))
        fitness_list.append(chrom_fitness)
    return [x for (y, x) in sorted(zip(fitness_list, chromosomes), reverse=1)], sorted(fitness_list, reverse=1)


# Function that creates a child with a
# crossover between 2 parents
def crossover(p1, p2):
    child = p1[0:3] + p2[3:10]
    return child


# Function to toggle a gene during mutation
def toggle(gene):
    if gene == 1:
        gene = 0
    elif gene == 0:
        gene = 1
    return gene


def mutate(chromosome):
    for index in range(len(chromosome)):
        if (random.random() < P_OF_MUTATION):
            chromosome[index] = toggle(chromosome[index])
    return chromosome


# For base function graphing
X = range(1023)
Y = []
for i in range(1023):
    Y.append(fitness(i))
population = initializePopulation(POPULATION_SIZE)
chromosomes, fitness_list = get_fitness_list(population)
plt.ion()

f, ax = plt.subplots(1)
ax.plot(X, Y, color="k")
total = 1
for chromosome in chromosomes:
    total += bin2dec(chromosome)
avg = total / POPULATION_SIZE

ax.plot(int(avg), fitness(int(avg)), marker='o', color="b", label="avg")
ax.plot(bin2dec(chromosomes[0]), fitness(bin2dec(chromosomes[0])), marker='o', color="g", label="best")
ax.plot(bin2dec(chromosomes[9]), fitness(bin2dec(chromosomes[9])), marker='o', color="r", label="worst")
ax.legend()


for i in range(time, 5000):
    print "generation: " + str(time), "Max chromosome: " + str(chromosomes[0]), "X: " + str(bin2dec(chromosomes[0])), "MAX: " + str(int(fitness_list[0]))

    if int(fitness_list[0]) == 31:
        break

    chromosomes = chromosomes[0:int(POPULATION_SIZE/2)]

    while(len(chromosomes)<POPULATION_SIZE):
        if random.random() < P_OF_CROSSOVER:
            parents = random.sample(xrange(0, len(chromosomes)-1), 2)
            parent1 = parents[0]
            parent2 = parents[1]
            child = crossover(chromosomes[parent1], chromosomes[parent2])

            if random.random() < P_OF_MUTATION:
                child = mutate(child)
            chromosomes.append(child)


    chromosomes, fitness_list = get_fitness_list(chromosomes)



    time += 1
    ax.plot(bin2dec(chromosomes[0]), fitness(bin2dec(chromosomes[0])), marker='o', color="g", label="best")
    ax.plot(bin2dec(chromosomes[9]), fitness(bin2dec(chromosomes[9])), marker='o', color="r", label="worst")
    # plt.pause(0.01)
stop = timeit.default_timer()
print ("--- %.7s seconds ---" % (stop - start))
plt.show(block=True)