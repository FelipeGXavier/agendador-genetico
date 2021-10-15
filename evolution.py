
from copy import copy, deepcopy
import random
import numpy

from chromosome import Chromosome

class Evolution:

    # @TODO fix conflicts
    def crossover(self, chromosome1, chromosome2):
        new_chromosome = []
        chromosome1_chunks = numpy.array_split(numpy.array(chromosome1.genes),3)
        chromosome2_chunks = numpy.array_split(numpy.array(chromosome2.genes),3)
        first_section = chromosome1_chunks[0]
        second_section = chromosome2_chunks[1]
        third_section = chromosome1_chunks[2]
        new_chromosome.append(first_section)
        new_chromosome.append(second_section)
        new_chromosome.append(third_section)
        return Chromosome(self.flatten(new_chromosome))
            

    def mutation(self, chromosome):
        temp_chromosome = deepcopy(chromosome)
        chosen_gene = temp_chromosome.genes.pop(random.randrange(len(temp_chromosome.genes)))
        swap_gene = temp_chromosome.genes.pop(random.randrange(len(temp_chromosome.genes)))
        for gene in chromosome.genes:
            if gene.id == chosen_gene.id:
                gene.week = swap_gene.week
                gene.schedule = swap_gene.schedule
            elif gene.id == swap_gene.id:
                gene.week = chosen_gene.week
                gene.schedule = chosen_gene.schedule
     
    # Seleção por torneio
    def selection(self, population, n, tsize=5):
        candidates = random.sample(population, tsize)
        return max(candidates, key=lambda x: x.fitness)

    # Prioriza resultados que distribuem as tarefas em todos dias de semana e que respeitem a preferência de horário
    def fitness(self, chromosome):
        morning_hours = [10,11,12]
        noun_hours = [13,14,15,16,17,18]
        weeks_schedule = []
        fitness = 0
        genes = chromosome.genes
        for gene in genes:
            gene = gene.gene()
            week_day = gene[0]
            preference = gene[len(gene) - 2:len(gene) - 1]
            schedule = gene[1:len(gene) - 2]
            if int(preference) == 0 and int(schedule) in morning_hours:
                fitness += 1
            elif int(preference) == 1 and int(schedule) in noun_hours:
                fitness += 1
            if week_day not in weeks_schedule:
                weeks_schedule.append(week_day)
        return fitness + len(weeks_schedule)

    def chunks(self, lst, n):
        result = []
        for i in range(0, len(lst), n):
            result.append(lst[i:i + n])
        return result

    def flatten(self, t):
        return [item for sublist in t for item in sublist]
  