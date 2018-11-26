import json
import sys

from SalesmanProblem.Population import Population


def main(cost_table_file_name='costTable.json', population_size=8, generations=25, mutation_rate=4):
    with open(cost_table_file_name) as costFile:
        cost_table = json.load(costFile)

    p = Population(population_size, cost_table, mutation_rate)
    p.print_costs()
    p.evolve(generations)
    p.get_best()
    print("END")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        main()
