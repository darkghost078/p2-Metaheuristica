import numpy as np 
from generateIndividual import bestIndividual
from evaluate import evaluate_solution

def metrics(fitness_scores):
           
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

    return mean, standard_deviation, best_absolute, worst

if __name__ == "__main__":
    individual, scores = metrics()