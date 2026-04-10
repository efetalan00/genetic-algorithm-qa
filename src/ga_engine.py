import random

class GeneticAlgorithm:

    def __init__(self, pop_size=10, mutation_rate=0.1):


        if not (0.0 <= mutation_rate <= 1.0):
            raise ValueError("Mutation rate must be between 0 and 1")
        self.pop_size = pop_size
        self.mutation_rate = mutation_rate
        self.genome_length = 8
        self.population = [[random.randint(0, 1) for _ in range(8)] for _ in range(pop_size)]

    def calculate_fitness(self, individual):

        return sum(individual)

    def mutate(self, individual):

        return [1-g if random.random() < self.mutation_rate else g for g in individual]

    def crossover(self, p1, p2):


        pt = random.randint(1, 7)
        return p1[:pt] + p2[pt:]

    def select_parents(self):

        return random.sample(self.population, 2)
