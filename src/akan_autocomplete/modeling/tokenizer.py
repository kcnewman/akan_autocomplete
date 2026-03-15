"""Custom SentencePiece tokenizer training and loading.

mT5's built-in tokenizer over-segments Akan words because Akan was not
in its pretraining data. A dedicated BPE tokenizer reduces sequence
length and OOV rate (ABENA blog, 2021).
"""
