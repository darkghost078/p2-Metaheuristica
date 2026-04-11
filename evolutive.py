from evaluate import evaluate_solution
from generateIndividual import generateIndividual
import random
from params import Param
import copy

def crossover(param1, param2):
    return Param(
        param1.n_estimators if random.random() > 0.5 else param2.n_estimators,
        param1.max_depth if random.random() > 0.5 else param2.max_depth,
        param1.min_samples_split if random.random() > 0.5 else param2.min_samples_split,
        param1.min_samples_leaf if random.random() > 0.5 else param2.min_samples_leaf,
        param1.max_features if random.random() > 0.5 else param2.max_features,
        param1.bootstrap if random.random() > 0.5 else param2.bootstrap,
        param1.criterion if random.random() > 0.5 else param2.criterion,
        param1.class_weight if random.random() > 0.5 else param2.class_weight,
        param1.max_leaf_nodes if random.random() > 0.5 else param2.max_leaf_nodes,
        param1.min_impurity_decrease if random.random() > 0.5 else param2.min_impurity_decrease
    )

def mutation(param):
    for _ in range(2):
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

def powerTournament(population, alpha, beta):
    childs = []
    for _ in range(len(population)//2):
        vp = population.copy()

        a = vp[random.randint(0,len(vp)-1)]
        vp.remove(a)
        b = vp[random.randint(0,len(vp)-1)]
        vp.remove(b)
        c = vp[random.randint(0,len(vp)-1)]

        a_fit=a[1]
        b_fit=b[1]
        c_fit=c[1]

        if(a_fit>b_fit):
            if(a_fit>c_fit):
                p1 = a[0]
            else:
                p1 = c[0]
        else:
            if(b_fit>c_fit):
                p1 = b[0]
            else:
                p1 = c[0]

        vp = population.copy()

        a = vp[random.randint(0,len(vp)-1)]
        vp.remove(a)
        b = vp[random.randint(0,len(vp)-1)]
        vp.remove(b)
        c = vp[random.randint(0,len(vp)-1)]

        a_fit=a[1]
        b_fit=b[1]
        c_fit=c[1]

        if(a_fit>b_fit):
            if(a_fit>c_fit):
                p2 = a[0]
            else:
                p2 = c[0]
        else:
            if(b_fit>c_fit):
                p2 = b[0]
            else:
                p2 = c[0]

        

        p = random.random()
        if(p <= alpha):
            childs.append(crossover(p1,p2))
            childs.append(crossover(p2,p1))
        else:
            childs.append(copy.deepcopy(p1))
            childs.append(copy.deepcopy(p2))

    aplyMutation(childs, beta)
    childs=fitness(childs)
    return childs

def aplyMutation(childs, beta):
    for i in range(len(childs)):
        p = random.random()
        if(p <= beta):
            mutation(childs[i])


def mergeArrays(a1, a2):
    result=[]
    aux=[]
    
    population=a1+a2

    for ind in population:
        if ind[0] not in aux:
            aux.append(ind[0])
            result.append(ind)
    
    return result

def finalPopulation(population, childs):
    bests = mergeArrays(population, childs)
    bests = sorted(bests, key=lambda childs: childs[1], reverse=True)

    return bests[:len(population)]

def fitness(population):
    result=[]
    for i in range(len(population)):
        result.append((population[i],evaluate_solution(population[i])))
    return result

def generatePopulation(population, n):
    for _ in range(n):
        individual=generateIndividual()
        population.append((individual,evaluate_solution(individual)))
    return population


def evolutive(Gen = 10, alpha = 0.8, beta = 0.2):
    population = []
    n=50
    elite_size=5
    population=generatePopulation(population,n)

    reset_count=0
    prev_best=0
    while(Gen>0):
        print(f"Gen Actual: {Gen}")
        Gen-=1
        childs = powerTournament(population, alpha, beta)

        bests = finalPopulation(population, childs)
        population = bests
        print(f"Best Fitness: {population[0][1]}")

        if (population[0][1]-prev_best )<0.005:
            reset_count+=1
            print("Fitness change not enough")
        else:
            reset_count=0
            print("Fitness change reset")

        prev_best=population[0][1]
        
        if reset_count>=3:
            elite=population[:elite_size]
            new_population=[]
            new_population=generatePopulation(new_population,n-elite_size)
            population=elite+new_population
            reset_count=0
            print("Reseting population")

    return population