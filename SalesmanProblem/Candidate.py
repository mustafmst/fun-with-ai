import numpy as np


class Candidate:
    def __init__(self, genotype, cost_table):
        self.genotype = genotype
        self.cost = None
        self.cost_table = cost_table
        self.cities_count = len(self.cost_table)

    def get_cost(self):
        if self.cost is None:
            self._calculate_cost()
        return self.cost

    def _calculate_cost(self):
        cities_queue = []
        for index in range(len(self.genotype)):
            index_value_queue = [i for i, e in enumerate(self.genotype) if e == index]
            for city in index_value_queue:
                cities_queue.append(city)
        tmp_cost = 0
        for i in range(len(cities_queue) - 1):
            tmp_cost += self.cost_table[cities_queue[i]][cities_queue[i + 1]]
        tmp_cost += self.cost_table[cities_queue[len(cities_queue) - 1]][cities_queue[0]]
        self.cost = tmp_cost

    def breed_with(self, other_candidate):
        mix_index = np.random.randint(len(self.genotype))
        return Candidate(self.genotype[:mix_index] + other_candidate.genotype[mix_index:], self.cost_table)

    def mutate(self):
        self.cost = None
        mutation_index = np.random.randint(len(self.genotype))
        self.genotype[mutation_index] = np.random.randint(self.cities_count)
        pass

    @staticmethod
    def create_random_candidate(genoms_count, cost_table):
        genotype = []
        for i in range(genoms_count):
            genotype.append(np.random.randint(0, genoms_count))
        return Candidate(genotype, cost_table)
