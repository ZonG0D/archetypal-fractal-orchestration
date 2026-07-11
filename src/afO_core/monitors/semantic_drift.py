import numpy as np
from typing import List, Dict

class SemanticDriftMonitor:
    def __init__(self, epsilon_threshold=0.1):
        self.epsilon = epsilon_threshold
    def calculate_drift(self, goal_vec: List[float], current_vec: List[float]) -> Dict:
        if len(goal_vec) != len(current_vec): return {"drift": 1.0, "stable": False}
        v1 = np.array(goal_vec); v2 = np.array(current_vec)
        n = (np.linalg.norm(v1) * np.linalg.norm(v2)) or 0.001
        s = float(np.dot(v1, v2) / n)
        d = max(0.0, min(1.0, 1.0 - s))
        return {"drift": d, "stable": d <= self.epsilon}