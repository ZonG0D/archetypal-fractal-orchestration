import sys
from typing import List, Dict

class ArchetypalOrchestrator:
    def __init__(self, goal_embedding: List[float], epsilon=0.1):
        import numpy as np
        try:
            from afO_core.monitors.semantic_drift import SemanticDriftMonitor
        except ImportError:
            sys.path.append('/home/anonz/Projects/archetypal-fractal-orchestration/src')
            from afO_core.monitors.semantic_drift import SemanticDriftMonitor
        self._goal = np.array(goal_embedding)
        self.monitor = SemanticDriftMonitor(epsilon_threshold=epsilon)

    def observe_and_act(self, current_state: List[float]) -> Dict:
        res = self.monitor.calculate_drift(self._goal.tolist(), current_state)
        return {"metrics": res, "instruction": "MAINTAIN" if res["stable"] else "REFINE"}

if __name__ == "__main__":
    o = ArchetypalOrchestrator([1.0, 0.0], epsilon=0.2)
    print(f"TEST: {o.observe_and_act([0.98, 0.05])}")