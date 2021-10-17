import random
from evolution import Evolution
from chromosome import Chromosome
from copy import copy, deepcopy
from tabulate import tabulate

class Genetic:

    POPULATION_SIZE = 300
    MAX_GENERATION = 500
    MUTATION_RATE = 0.05
    
    # Dias de semana segunda à sexta
    WEEK_DAYS = [1,2,3,4,5]
    # Horário de ínicio da atividade, cada atividade dura 1 hora
    SCHEDULES = [10,11,12,13,14,15,16,17,18]
    # 0 -> Matutino, 1 -> Vespertino
    PREFERENCES = [0, 1]

    def __init__(self, tasks):
        self.evolution = Evolution()
        self.tasks = tasks
        self.CHROMOSOME_SIZE = len(tasks)

    def run(self):
        # Inicia população
        population = self.init_population()
        population = list(map(lambda x: Chromosome(x), population))
        generation = 1
        evolution = Evolution()
        while True:
            print("Generetion n. " + str(generation))
            for chromossome in population:
                fitness = evolution.fitness(chromossome)
                chromossome.set_fitness(fitness)
            # Verifica ponto de parada relativo ao melhor fitness ou n. máximo de geração
            if self.check_halt_point(population, generation):
                break
            new_population = []
            # Gera novos indivíduos para a população
            for i in range(self.POPULATION_SIZE):
                selected_chromosome1 = evolution.selection(population)
                selected_chromosome2 = evolution.selection(population)
                new_chromosome1 = evolution.crossover(selected_chromosome1, selected_chromosome2)
                new_chromosome2 = evolution.crossover(selected_chromosome2, selected_chromosome1)
                new_population.append(new_chromosome1)
                new_population.append(new_chromosome2)
            # Aplica variabilidade por mutação
            for i in range(self.POPULATION_SIZE - 2):
                if random.random() <= self.MUTATION_RATE:
                    evolution.mutation(new_population[i])
            population = deepcopy(list(map(lambda x: Chromosome(x.genes), new_population)))
            generation = generation + 1
          
                
    def init_population(self):
        population = []
        for i in range(0, self.POPULATION_SIZE):
            chromosome = []
            possibilities = self.__init_possibilities_object()
            weeks = self.WEEK_DAYS[:]
            for task in self.tasks:
                result = copy(task)
                select_week_idx = random.randrange(len(weeks))
                selected_week = weeks[select_week_idx]
                selected_week_days = possibilities[str(selected_week)]
                if len(selected_week_days) == 1:
                    weeks.pop(select_week_idx)
                selected_schedule = selected_week_days.pop(random.randrange(len(selected_week_days)))
                result.set_schedule(selected_schedule)
                result.set_week(selected_week)
                chromosome.append(result)
            population.append(chromosome)
        return population

    def check_halt_point(self, population, generation):
        sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
        best_fit = sorted_population[0].fitness
        max_days_distribuiton = 5 if len(self.tasks) >= 5 else len(self.tasks)
        max_fit = self.CHROMOSOME_SIZE + max_days_distribuiton
        # Compara possível ótima solução com o melhor fitness da população de parâmetro
        if best_fit >= max_fit or generation >= self.MAX_GENERATION:
            print("Best fit=", best_fit)
            headers = ["ID", "Horário", "Preferência", "Dia da Semana"]
            table = []
            for data in sorted_population[0].genes:
                entity = []
                entity.append(data.id)
                entity.append(str(data.schedule) + ":00")
                entity.append('Matutino' if data.preference == 0 else 'Vespertino')
                entity.append(self.get_day(data.week))
                table.append(entity)
            # Exibe melhor resultado em forma de tabela com a lib tabulate
            print(tabulate(table, headers=headers, tablefmt="pretty"))
            return True
        return False

    def __init_possibilities_object(self):
        result = {}
        for i in self.WEEK_DAYS:
            result[str(i)] = self.SCHEDULES[:]
        return result
    
    def get_day(self, week):
        if week == 1:
            return "Segunda-feira"
        elif week == 2:
            return "Terça-feira"
        elif week == 3:
            return "Quarta-feira"
        elif week == 4:
            return "Quinta-feira"
        elif week == 5:
            return "Sexta-feira"
        else:
            return ""