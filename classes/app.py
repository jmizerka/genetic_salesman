from classes.gen_algo import GeneticAlgorithm
from classes.route_map import CitiesMap

class App:
    def __init__(self, num_of_cities, num_of_generations, show_map):
        self.num_of_chromosomes = 10
        self.num_of_cities = num_of_cities
        self.num_of_generations = num_of_generations
        self.show_map = show_map
        self.map_of_cities, self.distance_matrix = self.create_map()
        self.genetic_algo = self.create_gen_algo()
    def create_map(self):
        map_of_cities = CitiesMap(self.num_of_cities)
        distance_matrix = map_of_cities.calc_distance_matrix()
        return map_of_cities, distance_matrix

    def create_gen_algo(self):
        return GeneticAlgorithm(self.num_of_cities,self.num_of_chromosomes,self.distance_matrix)

    def run_app(self):
        print(f"The best distance in the first population is: {self.genetic_algo.best[0]}")
        print(f"The best order of cities in the first population is: {self.genetic_algo.best[1]}")
        for i in range(self.num_of_generations):
            self.genetic_algo.population = self.genetic_algo.selection()
            parents_pairs = self.genetic_algo.get_parents()
            self.genetic_algo.population = self.genetic_algo.cross_over(parents_pairs, 1)
            self.genetic_algo.population = self.genetic_algo.mutate(0.01)
            self.genetic_algo.fitness_vec = self.genetic_algo.fitness()
            self.genetic_algo.best = self.genetic_algo.check_if_best()
        print(f"The best overall distance is: {self.genetic_algo.best[0]}")
        print(f"The best overall order of cities in the first population is: {self.genetic_algo.best[1]}")
        if self.show_map == True:
            self.map_of_cities.plot_route(self.genetic_algo.best[1])
