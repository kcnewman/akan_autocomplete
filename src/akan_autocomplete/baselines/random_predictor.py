"""EXP-01: Uniform random predictor.

Sets the floor. Any model that beats this is learning something.
"""
import random
from typing import List


def predict(vocab: List[str], k: int = 5) -> List[str]:
    """Return k random words from vocabulary."""
    return random.choices(vocab, k=k)
