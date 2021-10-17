import random
from genetic import Genetic
from task import Task

ids = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tasks = []
for i in ids:
    tasks.append(Task(i+i, random.randrange(0,2)))

genetic = Genetic(tasks)
genetic.run()

