from evolutive import evolutive
from evaluate import evaluate_solution
import numpy as np
def evolutiveTest():

    population=evolutive(beta=0.5, alpha=0.6)
    return population[0]
    

if __name__ == "__main__":
    results=[]
    for _ in range(5):
        results.append(evolutiveTest())

    fitnesses=[]
    for i in range (len (results)):
        fitnesses.append(results[i][1])

    fitnesses.sort(reverse=True)

    print("\n--- Results ---")
    print(f"Best Individual Score: {fitnesses[0]}")
    print(f"Test Mean: {np.mean(fitnesses)}")
    print(f"Test Desviation: {np.std(fitnesses)}")