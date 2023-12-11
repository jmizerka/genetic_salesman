from classes.gen_algo import GeneticAlgorithm
from classes.route_map import CitiesMap


NUM_OF_CITIES = 20
NUM_OF_CHROMOSOMES = 10

map_of_cities = CitiesMap(NUM_OF_CITIES)
distance_matrix = map_of_cities.calc_distance_matrix()

genetic_algo = GeneticAlgorithm(NUM_OF_CITIES, NUM_OF_CHROMOSOMES, distance_matrix)
print(f"The best chromosome in the first population is: {genetic_algo.best}")

for i in range(100):
    genetic_algo.population = genetic_algo.selection()
    parents_pairs = genetic_algo.get_parents()
    genetic_algo.population = genetic_algo.cross_over(parents_pairs, 1)
    genetic_algo.population = genetic_algo.mutate(0.01)
    genetic_algo.fitness_vec = genetic_algo.fitness()
    genetic_algo.best = genetic_algo.check_if_best()

print(f'Best overall: {genetic_algo.best}')

map_of_cities.plot_route(genetic_algo.best[1])