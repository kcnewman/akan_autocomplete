"""Top-k next-word prediction and prefix completion."""
from typing import List


def predict_next_words(prefix: str, model, tokenizer, k: int = 5) -> List[str]:
    """Given a prefix, return the top-k predicted next words."""
    raise NotImplementedError


def complete_word(partial: str, model, tokenizer, k: int = 5) -> List[str]:
    """Given a partial word (e.g. 'Mek'), return top-k completions."""
    raise NotImplementedError
