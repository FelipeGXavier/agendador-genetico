class Chromosome:

    def __init__(self, genes):
        self.fitness = 0
        self.genes = genes
    
    def set_fitness(self, fitness):
        self.fitness = fitness

    def __str__(self):
        result = ""
        for i in self.genes:
            result = result + i.__str__() + "\n"
        return result + ", fitness=" + str(self.fitness) + "\n"