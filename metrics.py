import numpy as np 
from generateIndividual import bestIndividual
from evaluate import evaluate_solution

def metrics():
    mejores_individuos = []
    fitness_scores = []
    iter=20
    
    print(f"Starting {iter} iterations.")
    
    for i in range(iter):
        # 1. Obtenemos el mejor individuo de los 5 generados
        mejor_ind = bestIndividual()
        mejores_individuos.append(mejor_ind)
        
        fitness = evaluate_solution(mejor_ind)
        fitness_scores.append(fitness)
        
        print("Iterations {i+1}/{iter} completed -> Fitness: {fitness:.4f}")
        
    # 3. Calcular métricas estadísticas usando numpy
    mean = np.mean(fitness_scores)
    standard_deviation = np.std(fitness_scores)
    best_absolute = np.max(fitness_scores)
    worst = np.min(fitness_scores)
    
    # 4. Mostrar los resultados
    print("STATISTICAL RESULTS")
    print("="*30)
    print(f"Mean Accuracy: {mean: 0.4f}")

    print(f"Standard Deviation: {standard_deviation: 0.4f}")

    print(f"Best Overall Accuracy: {best_absolute: 0.4f}")

    print(f"Worst Accuracy: {worst: 0.4f}")
    
    # Devolvemos los datos por si quieres usarlos para hacer gráficas en tu memoria
    return mejores_individuos, fitness_scores

if __name__ == "__main__":
    individual, scores = metrics()