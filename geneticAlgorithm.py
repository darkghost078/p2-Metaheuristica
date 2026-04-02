from evolutive import evolutive
from evaluate import evaluate_solution
import numpy as np
def evolutiveTest():

    population=evolutive(beta=0.5, alpha=0.6)

    fitnesses=[]
    for i in range (len (population)):
        fitnesses.append(population[i][1])

    print("\n--- Results ---")
    print(f"Best Individual Score: {fitnesses[0]}")
    print(f"Population Mean: {np.mean(fitnesses)}")
    print(f"Population Desviation: {np.std(fitnesses)}")

    

if __name__ == "__main__":
    evolutiveTest()