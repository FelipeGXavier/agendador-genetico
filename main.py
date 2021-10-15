from genetic import Genetic
from task import Task


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
task13 = Task('Z', 1)


genetic = Genetic([task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, task11, task12])
genetic.run()







