import numpy as np
from typing import List

class SemanticDriftMonitor:
    def __init__(self, epsilon_threshold: float = 0.1):
        self.epsilon = epsilon_threshold

    def calculate_drift(self, goal_vec: List[float], current_vec: List[float]) -> float:
        if len(goal_vec) != len(current_vec):
            raise ValueError("Dimensional mismatch")
        v1 = np.array(goal_vec)
        v2 = np.array(current_vec)
        n1, n2 = np.linalg.norm(v1), np.linalg.norm(v2)
        if n1 == 0 or n2 == 0: return 1.0
        return float(np.clip(1.0 - (np.dot(v1, v2)/(n1 * n2)), 0, 1))

    def check_stability(self, goal: List[float], current: List[float]) -> dict:
        d = self.calculate_drift(goal, current)
        return {"drift": d, "stable": d <= self.epsilon}