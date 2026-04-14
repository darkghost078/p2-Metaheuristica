from generateIndividual import bestIndividual
from evaluate import evaluate_solution
from metrics import metrics
import numpy as np

def random_search(iter):
    print(f"--- Random Search ({iter} iter) ---")
    
    mejor_individual_global = None
    mejor_fitness_global = -1.0
    fitness = []
    # iter=20
    
    for i in range(5):
        individual = bestIndividual(iter)
        
        fitness_actual = evaluate_solution(individual.to_list())
        fitness.append(fitness_actual)
        
        print(f"Iterations {i+1}/{iter} completed -> Fitness: {fitness_actual:.4f}")
        
    print(f"\n Best fitness (Random Search): {mejor_fitness_global:.4f}")

    metrics(fitness)

    return mejor_fitness_global, mejor_individual_global

if __name__ == "__main__":
    # Ejecutamos primero el Random Search
    mejor_fit_rs, mejor_ind_rs = random_search()