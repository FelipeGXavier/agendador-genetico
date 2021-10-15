import random
from evolution import Evolution
from chromosome import Chromosome
from copy import copy

class Genetic:

    POPULATION_SIZE = 300
    MAX_GENERATION = 1000
    MUTATION_RATE = 0.05
    
    # Dias de semana segunda à sexta
    WEEK_DAYS = [1,2,3,4,5]
    # Horário de ínicio da atividade, cada atividade dura 1 hora
    SCHEDULES = [10,11,12,13,14,15,16,17,18]
    # 0 -> Matutino, 1 -> Diurno
    PREFERENCES = [0, 1]

    def __init__(self, tasks):
        self.evolution = Evolution()
        self.tasks = tasks
        self.CHROMOSOME_SIZE = len(tasks)

    def run(self):
        population = self.init_population()
        population = list(map(lambda x: Chromosome(x), population))
        evolution = Evolution()
        generation = 0
        while True:
            print("Generetion n. " + str(generation))
            for chromossome in population:
                fitness = evolution.fitness(chromossome)
                chromossome.set_fitness(fitness)
            if generation > 0 and self.check_halt_point(population):
                break
            new_population = []
            for i in range(self.POPULATION_SIZE):
                selected_chromosome1 = evolution.selection(population, len(population) + 1)
                selected_chromosome2 = evolution.selection(population, len(population) + 1)
                new_chromosome1 = evolution.crossover(selected_chromosome1, selected_chromosome2)
                new_chromosome2 = evolution.crossover(selected_chromosome2, selected_chromosome1)
                new_population.append(new_chromosome1)
                new_population.append(new_chromosome2)
            
            for i in range(self.POPULATION_SIZE - 2):
                if random.random() <= self.MUTATION_RATE:
                    evolution.mutation(new_population[i])

            population = new_population
            generation = generation + 1
            if generation >= self.MAX_GENERATION:
                break
                
    def init_population(self):
        population = []
        weeks = self.WEEK_DAYS[:]
        for i in range(0, self.POPULATION_SIZE):
            cromossome = []
            possibilities = self.__init_possibilities_object()
            for task in self.tasks:
                result = copy(task)
                selected_week = weeks[random.randrange(len(weeks))]
                selected_week_days = possibilities[str(selected_week)]
                selected_schedule = selected_week_days.pop(random.randrange(len(selected_week_days)))
                result.set_schedule(selected_schedule)
                result.set_week(selected_week)
                cromossome.append(result)
            population.append(cromossome)
        return population

    def check_halt_point(self, population):
        sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
        best_fit = sorted_population[0].fitness
        print("Best fit=", best_fit)
        for i in population[0].genes:
            print(i)
        print("\n")
        max_fit = self.CHROMOSOME_SIZE + 5
        if best_fit >= max_fit:
            return True
        return False

    def __init_possibilities_object(self):
        result = {}
        for i in self.WEEK_DAYS:
            result[str(i)] = self.SCHEDULES[:]
        return result