from __future__ import division
import math
import random
import pylab

time = 0
POPULATION_SIZE = 10
P_OF_MUTATION = 0.20
P_OF_CROSSOVER = 0.15


# Randomize the initial population
# with random chromosomes
def initializePopulation(size):
    population = []
    for i in range(size):
        chromosome = []
        for i in range(10):
            gene = random.randint(0, 1)
            chromosomee.append(gene)
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



population = initializePopulation(POPULATION_SIZE)
chromosomes, fitness_list = get_fitness_list(population)

for i in range(time, 500):

    print "generation: " + str(time), "Max chromosome: " + str(chromosomes[0]), "X: " + str(
        bin2dec(chromosomes[0])), "MAX: " + str(fitness_list[0])
    for index in range(len(chromosomes)):
        # If probability of crossover between two neighbors
        # perform a crossover with possible mutation as well
        if (random.random() < P_OF_CROSSOVER):
            child = crossover(chromosomes[index], chromosomes[(index + 1) % 10])
            child = mutate(child)
            chromosomes[9] = child
            chromosomes, fitness_list = get_fitness_list(chromosomes)

    time += 1


X = range(1023)
Y = []
for i in range(1023):
    Y.append(fitness(i))


pylab.plot(X, Y)
pylab.show()
