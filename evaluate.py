import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

# cargar dataset
data = pd.read_csv("winequality-red.csv", sep=";")

# convertir problema a clasificación binaria
data["quality"] = (data["quality"] >= 6).astype(int)

X = data.drop("quality", axis=1)
y = data["quality"]

def evaluate_solution(params):

    model = RandomForestClassifier(
        n_estimators=int(params.n_estimators),
        max_depth=int(params.max_depth),
        min_samples_split=int(params.min_samples_split),
        min_samples_leaf=int(params.min_samples_leaf),
        max_features=float(params.max_features),
        bootstrap=bool(params.bootstrap),
        criterion="gini" if params.criterion == 0 else "entropy",
        class_weight=None if params.class_weight == 0 else "balanced",
        max_leaf_nodes=int(params.max_leaf_nodes),
        min_impurity_decrease=float(params.min_impurity_decrease),
        random_state=42
    )
    
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    return scores.mean()