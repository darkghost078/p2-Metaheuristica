from generateIndividual import generateIndividual
from evaluate import evaluate_solution
from metrics import metrics
import numpy as np

def random_search(iter=20):
    print(f"--- Random Search ({iter} iter) ---")
    
    mejor_individual_global = None
    mejor_fitness_global = -1.0
    fitness = []
    
    for i in range(iter):
        individual = generateIndividual()
        
        fitness = evaluate_solution(individual)
        fitness.append(fitness)
        
        if fitness > mejor_fitness_global:
            mejor_fitness_global = fitness
            mejor_individual_global = individual
        
        print(f"Iterations {i+1}/{iter} completed -> Fitness: {fitness:.4f}")
        
    print(f"\n Best fitness (Random Search): {mejor_fitness_global:.4f}")

    metrics(fitness)

    return mejor_fitness_global, mejor_individual_global