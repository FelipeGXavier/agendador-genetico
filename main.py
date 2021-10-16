import random
from genetic import Genetic
from task import Task


ids = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tasks = []
for i in ids:
    tasks.append(Task(i, random.randrange(0,2)))

task1 = Task('A', 0)
task2 = Task('B', 0)
task3 = Task('C', 1)
task4 = Task('D', 1)
task5 = Task('E', 0)
task6 = Task('K', 0)
task7 = Task('F', 1)
task8 = Task('G', 0)
task9 = Task('H', 0)
task10 = Task('I', 0)
task11 = Task('X', 0)
task12 = Task('W', 0)

task13 = Task('V', 1)
task14 = Task('J', 0)
task15 = Task('P', 0)
task16 = Task('Q', 0)
task17 = Task('R', 0)
task18 = Task('S', 1)


genetic = Genetic(tasks)
genetic.run()



