import numpy as np

from SalesmanProblem.Candidate import Candidate


class Population:
    def __init__(self, size, cost_table, mutation_rate=1):
        self.generations = None
        self.mutation_rate = mutation_rate
        self.cost_table = cost_table
        self.cities_count = len(self.cost_table)
        self.candidates = self.generate_population(size)

    def evolve(self, generations):
        self.generations = generations
        for i in range(generations):
            self.selection()
            self.breed()
            self.mutate()
            print("GEN: {gen:02d}".format(gen=i))
            self.print_costs()

    def selection(self):
        old_population = self.candidates
        new_population = []
        while len(old_population) > 1:
            candidate_one = Population.get_random_candidate(old_population)
            old_population.remove(candidate_one)
            candidate_two = Population.get_random_candidate(old_population)
            old_population.remove(candidate_two)
            new_population.append(Population.selection_round(candidate_one, candidate_two))
        self.candidates = new_population

    def breed(self):
        old_population = self.candidates
        new_population = []
        while len(old_population) > 1:
            candidate_one = Population.get_random_candidate(old_population)
            old_population.remove(candidate_one)
            new_population.append(candidate_one)
            candidate_two = Population.get_random_candidate(old_population)
            old_population.remove(candidate_two)
            new_population.append(candidate_two)
            new_population.append(candidate_one.breed_with(candidate_two))
            new_population.append(candidate_two.breed_with(candidate_one))
        self.candidates = new_population

    def mutate(self):
        for i in range(self.mutation_rate):
            mutation_candidate = Population.get_random_candidate(self.candidates)
            mutation_candidate.mutate()
        pass

    def print_costs(self):
        sign = "==========================================="
        print(sign)
        for i in range(len(self.candidates)):
            print("[{index:02d}]{gen}\t- {cost}".format(index=i, gen=self.candidates[i].genotype, cost=self.candidates[i].get_cost()))
        print(sign)

    def get_best(self):
        best = self.candidates[0]
        for candidate in self.candidates:
            if candidate.get_cost() < best.get_cost():
                best = candidate
        print("Best candidate after {2} generations: genotype: {0} - cost: {1}".format(best.genotype, best.get_cost(),
                                                                                       self.generations))
        return best

    def generate_population(self, size):
        population = []
        for i in range(size):
            population.append(Candidate.create_random_candidate(self.cities_count, self.cost_table))
        return population

    @staticmethod
    def selection_round(candidate_one, candidate_two):
        if candidate_one.get_cost() < candidate_two.get_cost():
            return candidate_one
        else:
            return candidate_two

    @staticmethod
    def get_random_candidate(population):
        index = np.random.randint(0, len(population))
        return population[index]
