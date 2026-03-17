import numpy as np 
from generateIndividual import bestIndividual
from evaluate import evaluate_solution

def metrics(iteraciones=20):
    mejores_individuos = []
    fitness_scores = []
    
    print(f"Iniciando {iteraciones} iteraciones. ¡Paciencia, esto tomará un rato! ")
    
    for i in range(iteraciones):
        # 1. Obtenemos el mejor individuo de los 5 generados
        mejor_ind = bestIndividual()
        mejores_individuos.append(mejor_ind)
        
        fitness = evaluate_solution(mejor_ind)
        fitness_scores.append(fitness)
        
        print(f"Iteración {i+1}/{iteraciones} completada -> Fitness: {fitness:.4f}")
        
    # 3. Calcular métricas estadísticas usando numpy
    media = np.mean(fitness_scores)
    desviacion = np.std(fitness_scores)
    mejor_absoluto = np.max(fitness_scores)
    peor = np.min(fitness_scores)
    
    # 4. Mostrar los resultados
    print("\n" + "="*30)
    print("RESULTADOS ESTADÍSTICOS")
    print("="*30)
    print(f"Media del Accuracy:      {media:.4f}")
    print(f"Desviación Típica:       {desviacion:.4f}")
    print(f"Mejor Accuracy global:   {mejor_absoluto:.4f}")
    print(f"Peor Accuracy:           {peor:.4f}")
    
    # Devolvemos los datos por si quieres usarlos para hacer gráficas en tu memoria
    return mejores_individuos, fitness_scores