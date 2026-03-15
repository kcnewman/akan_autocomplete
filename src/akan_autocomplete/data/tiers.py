"""Data tier labelling and separation.

Tier 1 — clean: manually verified, native-speaker-validated.
          Use for: fine-tuning AND evaluation.
Tier 2 — noisy: JW300, web-scraped.
          Use for: pre-training ONLY. Never use as eval gold.
Tier 3 — code-switched: Twi-English mixed (WhatsApp-style).
          Use for: code-switching experiment (EXP-08) only.

RULE: Never mix tiers without explicit labelling.
"""
