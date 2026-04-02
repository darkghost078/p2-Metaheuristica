import itertools
from evaluate import evaluate_solution
from metrics import metrics

def gridSearch(paramGrid):
    combinations = list(itertools.product(*paramGrid))
    
    totalComb = len(combinations)
    print(f"Total combinations to evaluate: {totalComb}")
    
    bestFitness = -1.0
    bestIndividual = None
    allFitnessScores = []
    
    for index, combo in enumerate(combinations):
        actualIndividual = list(combo)
        
        actualFitness = evaluate_solution(actualIndividual)
        allFitnessScores.append(actualFitness)
        
        if actualFitness > bestFitness:
            bestFitness = actualFitness
            bestIndividual = actualIndividual
            
        if (index + 1) % 10 == 0 or (index + 1) == totalComb:
            print(f"[{index + 1}/{totalComb}] Evaluated -> Current Best: {bestFitness:.4f}")
            
    print("\n--- Grid Search Results ---")
    print(f"Best Accuracy: {bestFitness:.4f}")
    print(f"Best Parameters: {bestIndividual}")
    
    print("\nOverall Statistics:")
    metrics(allFitnessScores)
    
    return bestFitness, bestIndividual

if __name__ == "__main__":
    myGrid = [
        [50, 150],            # 0: n_estimators (2 options)
        [10, 20],             # 1: max_depth (2 options)
        [2],                  # 2: min_samples_split (Fixed)
        [1],                  # 3: min_samples_leaf (Fixed)
        [0.5, 1.0],           # 4: max_features (2 options)
        [1],                  # 5: bootstrap (Fixed to True)
        [0, 1],               # 6: criterion (2 options)
        [0],                  # 7: class_weight (Fixed to None)
        [50],                 # 8: max_leaf_nodes (Fixed)
        [0.0]                 # 9: min_impurity_decrease (Fixed)
    ]
    gridSearch(myGrid)