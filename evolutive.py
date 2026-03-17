import evaluate
from params import Param 

Gen = 20

def crossover(param1, param2):
    return Param(
        param1.n_estimators,
        param1.max_depth,
        param1.min_samples_split,
        param1.min_samples_leaf,
        param1.max_features,
        param2.bootstrap,
        param2.criterion,
        param2.class_weight,
        param2.max_leaf_nodes,
        param2.min_impurity_decrease
    )

def mutation(param):
    

population = []

#Generación de la población inicial (falta llamar a la funcion random)
for i in range(20):
    population.append()

while(Gen>0):
    Gen-=1
