# Genetic Salesman 

## Introduction

> The goal of the project was to solve the traveling salesman problem (TSP). TSP is a classic optimization problem in the field of computer science, operations research, and mathematics. The problem can be stated as follows:
>>Given a list of cities and the distances between each pair of cities, the task is to find the shortest possible tour that visits each city exactly once and returns to the original city. The tour must be a closed loop, and the total distance traveled should be minimized. The Traveling Salesman Problem is NP-hard, meaning that there is no known algorithm that can solve all instances of the problem in polynomial time. Therefore, researchers and practitioners often use approximation algorithms or heuristics to find near-optimal solutions in a reasonable amount of time.

>  My solution uses a genetic algorithm (GA). It is a type of optimization algorithm inspired by the principles of natural selection and genetics. It belongs to the broader class of evolutionary algorithms and is used to find approximate solutions to optimization and search problems. Genetic algorithms are particularly useful for solving complex problems where traditional algorithms may be less effective. Here's a simplified overview of how a genetic algorithm works:
> 1. Initialization:
>- A population of potential solutions (individuals or chromosomes) is created randomly. Each solution represents a possible candidate for the optimal solution to the problem.
>
>2. Evaluation:
>- Each individual in the population is evaluated based on its fitness, which is a measure of how well it solves the problem at hand. The fitness function quantifies the quality of a solution.
>
>3. Selection:
>- Individuals are selected to become parents for the next generation. The probability of selection is typically proportional to the individual's fitness – better solutions have a higher chance of being selected.
>
>4. Crossover (Recombination):
>- Pairs of parents are chosen, and a crossover operation combines their genetic information to create offspring. This mimics the process of genetic recombination in biological reproduction.
>
>5. Mutation:
>- Random changes are introduced to the genetic information of some individuals. This introduces diversity into the population and helps explore new areas of the solution space.
>
>6. Replacement:
>- The new generation, which consists of both parents and offspring, replaces the old generation. The individuals with higher fitness are more likely to be selected for the next generation.
>
>7. Termination:
>- The algorithm continues evolving new generations until a stopping criterion is met. This could be a specified number of generations, a satisfactory level of fitness, or other criteria.


## Code Samples

1. Usage from command line:

`python main.py num_of_cities num_of_generations show_map`

- num_of_cities: Specify the number of cities on the map as an integer.
- num_of_generations: Specify the number of algorithm generations as integer
 - show_map: Specify whether to show the map of cities with route between them as True/False

2. Example:

`python main.py 10 100 True`

## Installation
`pip install requirements.txt`