import random
from copy import deepcopy
import numpy as np

class GeneticAlgorithm:
    def __init__(self, num_of_cities, num_of_chromosomes, distance_matrix):
        self.num_of_cities = num_of_cities
        self.num_of_chromosomes = num_of_chromosomes
        self.distance_matrix = distance_matrix
        self.population = self.define_population()
        self.fitness_vec = np.zeros((self.population.shape[0],1))
        self.fitness_vec = self.fitness()
        self.best = (np.min(self.fitness_vec), self.population[np.argmin(self.fitness_vec)])
    def define_population(self):
        pop = np.zeros((self.num_of_chromosomes, self.num_of_cities - 1))
        for i in range(self.num_of_chromosomes):
            pop[i] = random.sample(range(1, self.num_of_cities), self.num_of_cities - 1)
        return pop

    def fitness(self):
        temp_vec = np.zeros((self.population.shape[0],1))
        for i in range(self.num_of_chromosomes):
            temp_vec[i] += self.distance_matrix[0][int(self.population[i][0])]
            temp_vec[i] += self.distance_matrix[0][int(self.population[i][self.distance_matrix.shape[1] - 2])]
            for j in range(self.num_of_cities-2):
                temp_vec[i] += self.distance_matrix[int(self.population[i][j])][int(self.population[i][j + 1])]
        return temp_vec

    def selection(self, type='roulette'):
        selected_pop = np.zeros(self.population.shape)
        if type == 'roulette':
            inverted_fitness = [1 / (fitness) for fitness in self.fitness_vec]
            total_inv_fitness = sum(inverted_fitness)
            roulette = np.cumsum(inverted_fitness / total_inv_fitness)
            for i in range(self.population.shape[0]):
                random_num = random.uniform(0, 1)
                for j in range(self.population.shape[0]):
                    if random_num < roulette[j]:
                        selected_pop[i] = self.population[j]
                        break
        return selected_pop

    def get_parents(self):
        chrom_indices = list(range(0, self.num_of_chromosomes))
        parents_pairs = []
        while len(chrom_indices) > 0:
            random_nums = random.sample(range(0, self.num_of_chromosomes), 2)
            if random_nums[0] in chrom_indices and random_nums[1] in chrom_indices:
                chrom_indices.remove(random_nums[0])
                chrom_indices.remove(random_nums[1])
                parents_pairs.append(random_nums)
        return parents_pairs

    def cross_over(self, pairs, crossing_prob):
        crossed_pop = np.zeros((self.population.shape))
        copied_pop = self.population
        for i in range(len(pairs)):
            prob = random.uniform(0, 1)
            if prob < crossing_prob:
                parent1 = np.zeros((copied_pop.shape[1]))
                parent2 = np.zeros((copied_pop.shape[1]))
                crossing_points = random.sample(range(0, copied_pop.shape[1]), 2)
                cross1 = min(crossing_points)
                cross2 = max(crossing_points)
                parent1[cross1:cross2] = copied_pop[pairs[i][1]][cross1:cross2]
                parent2[cross1:cross2] = copied_pop[pairs[i][0]][cross1:cross2]
                list_of_chroms1 = list(copied_pop[pairs[i][0]][cross2:])
                list_of_chroms1.extend(list(copied_pop[pairs[i][0]][:cross2]))
                list_of_chroms2 = list(copied_pop[pairs[i][1]][cross2:])
                list_of_chroms2.extend(list(copied_pop[pairs[i][1]][:cross2]))
                for j in range(cross1,cross2):
                    list_of_chroms2.remove(parent2[j])
                    list_of_chroms1.remove(parent1[j])

                parent1[cross2:] = list_of_chroms1[:len(parent1[cross2:])]
                parent2[cross2:] = list_of_chroms2[:len(parent2[cross2:])]

                parent1[:cross1] = list_of_chroms1[len(parent1[cross2:]):]
                parent2[:cross1] = list_of_chroms2[len(parent2[cross2:]):]

                crossed_pop[pairs[i][0]] = parent1
                crossed_pop[pairs[i][1]] = parent2

            else:
                crossed_pop[pairs[i][0]] = copied_pop[pairs[i][0]]
                crossed_pop[pairs[i][1]] = copied_pop[pairs[i][1]]
        return crossed_pop

    def mutate(self, mutation_prob):
        mutated_pop = np.zeros(self.population.shape)
        copied_pop = self.population
        for i in range(copied_pop.shape[0]):
            prob = random.uniform(0, 1)
            if prob < mutation_prob:
                mutated_pop[i] = copied_pop[i]
                mutatation_points = random.sample(range(0,copied_pop.shape[1] - 1), 2)
                temp = deepcopy(copied_pop[i][mutatation_points[0]])
                mutated_pop[i][mutatation_points[0]] = copied_pop[i][mutatation_points[1]]
                mutated_pop[i][mutatation_points[1]] = temp
            else:
                mutated_pop[i] = copied_pop[i]
        return mutated_pop

    def check_if_best(self):
        if self.best[0] > np.min(self.fitness_vec):
            best = (np.min(self.fitness_vec), self.population[np.argmin(self.fitness_vec)])
            return best
        else:
            return self.best