"""Automatic evaluation metrics.

Metrics:
  - Perplexity (PPL) — report separately for Tier 1 and Tier 2
  - Top-1 / Top-5 word accuracy
  - Keystroke Savings Rate (KSR) = (chars saved / total chars) × 100
  - Character Error Rate (CER) — for character-level completion
  - Tonal Accuracy — novel metric: correct ɔ/ɛ restoration from de-toned input
"""


def keystroke_savings_rate(predictions: list, targets: list) -> float:
    """KSR — standard industry metric for keyboard autocomplete."""
    raise NotImplementedError


def tonal_accuracy(predictions: list, targets: list) -> float:
    """Fraction of correctly predicted tonal diacritics (ɔ, ɛ)."""
    raise NotImplementedError
