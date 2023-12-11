from classes.city import City
import matplotlib.pyplot as plt
import math
import numpy as np

class CitiesMap:
    def __init__(self,num_of_cites):
        self.num_of_cities = num_of_cites
        self.list_of_cities = []
        for i in range(num_of_cites):
            self.list_of_cities.append(City())
        self.cities_coors = np.array([city.coor for city in self.list_of_cities])

    def plot_map(self):
        plt.figure(150,150)
        plt.plot(self.cities_coors[:,0],self.cities_coors[:,1])
        plt.grid(visible=True, which='both')
        plt.title('Map of cities')
        plt.show()

    def plot_route(self, order):
        order = np.insert(order, 0, 0)
        order = np.append(order, 0)
        plt.figure(figsize=(150, 150))
        plt.plot([self.cities_coors[int(i)][0] for i in order], [self.cities_coors[int(i)][1] for i in order], linestyle='-', marker='.')
        plt.plot(self.cities_coors[int(0)][0], self.cities_coors[int(0)][1], linestyle='-', marker='X', color='red', label='Start')
        plt.legend()
        plt.grid(visible=True, which='both')
        plt.title('Route')
        plt.show()

    def calc_distance_matrix(self):
        distance_matrix = np.zeros((self.num_of_cities,self.num_of_cities))
        for i in range(self.num_of_cities):
            x1, y1 = self.cities_coors[i]
            for j in range(self.num_of_cities):
                x2, y2 = self.cities_coors[j]
                distance_matrix[i][j] = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return distance_matrix
