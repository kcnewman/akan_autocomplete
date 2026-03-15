"""Unicode normalisation for Akan text.

Critical codepoints:
    ɔ  U+0254  LATIN SMALL LETTER OPEN O
    ɛ  U+025B  LATIN SMALL LETTER OPEN E

Run unicodedata.normalize('NFC', text) before any tokenization.
"""
import unicodedata


def normalize(text: str) -> str:
    """NFC-normalize and strip leading/trailing whitespace."""
    return unicodedata.normalize("NFC", text).strip()
