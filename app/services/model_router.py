from dataclasses import dataclass
from enum import Enum


class TaskComplexity(str, Enum):
    FAST = "fast"
    STRONG = "strong"


@dataclass(frozen=True)
class ModelDecision:
    task: TaskComplexity
    model: str
    reason: str


class ModelRouter:
    """Keeps provider/model choice out of business logic."""

    def __init__(self, fast_model: str, strong_model: str) -> None:
        self.fast_model = fast_model
        self.strong_model = strong_model

    def choose(self, task: TaskComplexity) -> ModelDecision:
        if task is TaskComplexity.STRONG:
            return ModelDecision(task, self.strong_model, "complex generation or critique")
        return ModelDecision(task, self.fast_model, "classification, extraction, or lightweight rewrite")
