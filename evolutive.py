from evaluate import evaluate_solution
from generateIndividual import generateIndividual
import random
from params import Param 

Gen = 20
alpha = 0.8
beta = 0.2

def crossover(param1, param2):
    return Param(
        param2.n_estimators,
        param1.max_depth,
        param1.min_samples_split,
        param1.min_samples_leaf,
        param1.max_features,
        param1.bootstrap,
        param2.criterion,
        param2.class_weight,
        param2.max_leaf_nodes,
        param2.min_impurity_decrease
    )

def mutation(param):
    nrand = random.randint(1,10)

    if(nrand == 1):
        param.n_estimators  = random.randint(10,300)
    elif(nrand == 2):
        param.max_depth = random.randint(2,30)
    elif(nrand == 3):
        param.min_samples_split = random.randint(2,20)
    elif(nrand == 4):
        param.min_samples_leaf = random.randint(1,20)
    elif(nrand == 5):
        param.max_features = random.uniform(0.1,1.0)
    elif(nrand == 6):
        param.bootstrap = random.randint(0,1)
    elif(nrand == 7):
        param.criterion = random.randint(0,1)
    elif(nrand == 8):
        param.class_weight = random.randint(0,1)
    elif(nrand == 9):
        param.max_leaf_nodes = random.randint(10,200)
    elif(nrand == 10):
        param.min_impurity_decrease = random.uniform(0,0.1)

def powerTournament(population):
    childs = []
    for i in range(len(population)):
        vp = population.copy()

        a = vp[random.randint(0,len(vp))]
        vp.remove(a)
        b = vp[random.randint(0,len(vp))]
        vp.remove(b)
        c = vp[random.randint(0,len(vp))]

        if(evaluate_solution(a)>evaluate_solution(b)):
            if(evaluate_solution(a)>evaluate_solution(c)):
                p1 = a
            else:
                p1 = c
        else:
            if(evaluate_solution(b)>evaluate_solution(c)):
                p1 = b
            else:
                p1 = c

        vp = population.copy()

        a = vp[random.randint(0,len(vp))]
        vp.remove(a)
        b = vp[random.randint(0,len(vp))]
        vp.remove(b)
        c = vp[random.randint(0,len(vp))]

        if(evaluate_solution(a)>evaluate_solution(b)):
            if(evaluate_solution(a)>evaluate_solution(c)):
                p2 = a
            else:
                p2 = c
        else:
            if(evaluate_solution(b)>evaluate_solution(c)):
                p2 = b
            else:
                p2 = c        

        p = random.random()
        if(p <= alpha):
            childs.append(crossover(p1,p2))
            childs.append(crossover(p2,p1))
        else:
            childs.append(p1)
            childs.append(p2)

    hiroshima(childs)
    return childs

def hiroshima(childs):
    for i in range(len(childs)):
        p = random.random()
        if(p <= beta):
            mutation(childs[i])

def auschwitz(population, childs):
    bests = population + childs
    aux = bests.copy()
    bests = list(set(aux))
    print(aux==bests)
    bests = sorted(bests, key=lambda child: evaluate_solution(child))

    return bests[len(bests)-len(population):]


population = []

for i in range(20):
    population.append(generateIndividual())


while(Gen>0):
    Gen-=1
    p = random.random()
    
    childs = powerTournament(population)

    bests = auschwitz(population, childs)
    population = bests