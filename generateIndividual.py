import random
from evaluate import evaluate_solution

def generateIndividual():
    individual = [
        random.randint(10, 300),          # n_estimators (entero) 
        random.randint(2, 30),            # max_depth (entero) 
        random.randint(2, 20),            # min_samples_split (entero) 
        random.randint(1, 20),            # min_samples_leaf (entero) 
        random.uniform(0.1, 1.0),         # max_features (real) 
        random.randint(0, 1),             # bootstrap (binario) 
        random.randint(0, 1),             # criterion (categórico: 0=gini, 1=entropy) 
        random.randint(0, 1),             # class_weight (binario: 0=None, 1=balanced) 
        random.randint(10, 200),          # max_leaf_nodes (entero) 
        random.uniform(0.0, 0.1)          # min_impurity_decrease (real) 
    ]
    return individual

def bestIndividual():
    best = None
    best_fitness = -1.0 
    
    for _ in range(5):
        actual_individual = generateIndividual()
        
        actual_fitness = evaluate_solution(actual_individual)
        
        if actual_fitness > best_fitness:
            best_fitness = actual_fitness
            best = actual_individual

    print(f"Best fitness of the five: {best_fitness}")
    
    return best
