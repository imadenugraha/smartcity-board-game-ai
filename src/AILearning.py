import numpy as np

from typing import Dict


class AILearning:
    def __init__(self):
        self.difficulty = 1.0
        self.history = []
        self.learning_rate = 0.1
        
    def update_difficulty(self, performance_score: float):
        self.history.append(performance_score)
        
        if len(self.history) >= 3:
            trend = np.mean(self.history[-3:])
            
            if trend > 75:
                self.difficulty = min(2.0, self.difficulty + self.learning_rate)
            elif trend < 40:
                self.difficulty = max(0.5, self.difficulty - self.learning_rate)
    
    def get_modified_event(self, event: Dict) -> Dict:
        modified_event = event.copy()
        
        modified_event["efek"] = {
            k: int(v * self.difficulty) for k, v in event["efek"].items()
        }
        
        return modified_event
