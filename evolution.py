
from copy import deepcopy
import random

from chromosome import Chromosome

class Evolution:

    def crossover(self, chromosome1, chromosome2):
        # Seleciona uma seção aleatória de um dos cromossomos para iniciar a recombinação
        section = random.sample(chromosome1.genes, random.randrange(2, len(chromosome1.genes) - 2))
        section_genes_ids = list(map(lambda x: x.id, section))
        new_genes = section
        missing_genes = []
        # Identifica quais pedaços de gene faltam para não perder nenhuma informação na recombinação como repetir uma mesma tarefa
        for gene in chromosome1.genes:
            if gene.id not in section_genes_ids:
                missing_genes.append(gene.id)
        # Faz a recombinação dos genes que faltam da seção inicial com o segundo cromossomo
        for id in missing_genes:
            chromosome2_gene = chromosome2.find_task_by_id(id)
            valid_gene = True
            for gene in new_genes:
                if chromosome2_gene.id == gene.id and chromosome2_gene.week == gene.week and chromosome2_gene.schedule == gene.schedule:
                    valid_gene = False
                    break
            if valid_gene:
                new_genes.append(chromosome2_gene)
            else:
                chromosome1_gene = chromosome1.find_task_by_id(id)
                new_genes.append(chromosome1_gene)
        new_genes = sorted(new_genes, key=lambda x: x.id)
        # Verifica se o novo cromosso gerado possui conflitos de horário
        # Caso tenha deve ser mitigado para gerar uma possível solução recombinando sem conflitos
        has_conflicts = self.check_conflicts(new_genes)
        return Chromosome(new_genes)
            
    def mutation(self, chromosome):
        temp_chromosome = deepcopy(chromosome)
        chosen_gene = temp_chromosome.genes.pop(random.randrange(len(temp_chromosome.genes)))
        swap_gene = temp_chromosome.genes.pop(random.randrange(len(temp_chromosome.genes)))
        # Troca dois genes de posição mudando o dia de semana e horário de duas tarefas distintas
        for gene in chromosome.genes:
            if gene.id == chosen_gene.id:
                gene.week = swap_gene.week
                gene.schedule = swap_gene.schedule
            elif gene.id == swap_gene.id:
                gene.week = chosen_gene.week
                gene.schedule = chosen_gene.schedule
     
    # Seleção por torneio
    def selection(self, population, size=3):
        candidates = random.sample(population, size)
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
            preference = gene[len(gene) - 3:len(gene) - 2]
            schedule = gene[1:len(gene) - 3]
            if int(preference) == 0 and int(schedule) in morning_hours:
                fitness += 1
            elif int(preference) == 1 and int(schedule) in noun_hours:
                fitness += 1
            if week_day not in weeks_schedule:
                weeks_schedule.append(week_day)
        return fitness + len(weeks_schedule)

    def check_conflicts(self, genes):
        conflictable_info = list(map(lambda x: str(x.week) + str(x.schedule), genes))
        return len(conflictable_info) != len(set(conflictable_info))
        
  