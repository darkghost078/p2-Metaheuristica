import random
from evaluate import evaluate_solution
from params import Param

def generateIndividual():
    return Param(
        n_estimators=random.randint(10, 300),
        max_depth=random.randint(2, 30),
        min_samples_split=random.randint(2, 20),
        min_samples_leaf=random.randint(1, 20),
        max_features=random.uniform(0.1, 1.0),
        bootstrap=random.randint(0, 1),
        criterion=random.randint(0, 1),
        class_weight=random.randint(0, 1),
        max_leaf_nodes=random.randint(10, 200),
        min_impurity_decrease=random.uniform(0.0, 0.1)
    )

def bestIndividual():
    best = None
    best_fitness = -1.0 
    
    for _ in range(5):
        actual_individual = generateIndividual()
        
        actual_fitness = evaluate_solution(actual_individual.to_list())
        
        if actual_fitness > best_fitness:
            best_fitness = actual_fitness
            best = actual_individual

    print(f"Best fitness of the five: {best_fitness}")
    
    return best
