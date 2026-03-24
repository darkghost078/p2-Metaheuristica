class Param:
    def __init__(
        self,
        n_estimators: int = 100,
        max_depth: int = 10,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        max_features: float = 1.0,
        bootstrap: int = 1,
        criterion: int = 0,
        class_weight: int = 0,
        max_leaf_nodes: int = 50,
        min_impurity_decrease: float = 0.0
    ):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.bootstrap = bootstrap
        self.criterion = criterion
        self.class_weight = class_weight
        self.max_leaf_nodes = max_leaf_nodes
        self.min_impurity_decrease = min_impurity_decrease

        self._validate_params()

    def _validate_params(self):
        
        if not isinstance(self.n_estimators, int) or not (10 <= self.n_estimators <= 300):
            raise ValueError(f"n_estimators debe ser un entero entre 10 y 300. Recibido: {self.n_estimators}")
            
        if not isinstance(self.max_depth, int) or not (2 <= self.max_depth <= 30):
            raise ValueError(f"max_depth debe ser un entero entre 2 y 30. Recibido: {self.max_depth}")
            
        if not isinstance(self.min_samples_split, int) or not (2 <= self.min_samples_split <= 20):
            raise ValueError(f"min_samples_split debe ser un entero entre 2 y 20. Recibido: {self.min_samples_split}")
            
        if not isinstance(self.min_samples_leaf, int) or not (1 <= self.min_samples_leaf <= 20):
            raise ValueError(f"min_samples_leaf debe ser un entero entre 1 y 20. Recibido: {self.min_samples_leaf}")
            
        if not isinstance(self.max_features, (int, float)) or not (0.1 <= self.max_features <= 1.0):
            raise ValueError(f"max_features debe ser un real entre 0.1 y 1.0. Recibido: {self.max_features}")
            
        if self.bootstrap not in [0, 1]:
            raise ValueError(f"bootstrap debe ser binario (0 o 1). Recibido: {self.bootstrap}")
            
        if self.criterion not in [0, 1]:
            raise ValueError(f"criterion debe ser 0 (gini) o 1 (entropy). Recibido: {self.criterion}")
            
        if self.class_weight not in [0, 1]:
            raise ValueError(f"class_weight debe ser 0 (None) o 1 (balanced). Recibido: {self.class_weight}")
            
        if not isinstance(self.max_leaf_nodes, int) or not (10 <= self.max_leaf_nodes <= 200):
            raise ValueError(f"max_leaf_nodes debe ser un entero entre 10 y 200. Recibido: {self.max_leaf_nodes}")
            
        if not isinstance(self.min_impurity_decrease, (int, float)) or not (0.0 <= self.min_impurity_decrease <= 0.1):
            raise ValueError(f"min_impurity_decrease debe ser un real entre 0 y 0.1. Recibido: {self.min_impurity_decrease}")

    def to_sklearn_dict(self) -> dict:
        
        return {
            "n_estimators": self.n_estimators,
            "max_depth": self.max_depth,
            "min_samples_split": self.min_samples_split,
            "min_samples_leaf": self.min_samples_leaf,
            "max_features": self.max_features,
            "bootstrap": bool(self.bootstrap),
            "criterion": "entropy" if self.criterion == 1 else "gini",
            "class_weight": "balanced" if self.class_weight == 1 else None,
            "max_leaf_nodes": self.max_leaf_nodes,
            "min_impurity_decrease": self.min_impurity_decrease
        }