# Architectural & Research Decisions

## Task Framing
- **Primary:** Word-level autocomplete — P(w_t | w_1...w_{t-1})
- **Secondary:** Code-switching experiment (Twi-English mixed input)

## Dialect
- **Primary:** Asante Twi (larger speaker population; cleaner Bible corpus)
- **Secondary:** Akuapem Twi (dialect generalisation experiment, EXP-09)

## Tonal Diacritics
- Model tones (ɔ U+0254, ɛ U+025B) — do NOT strip diacritics
- Rationale: tonal accuracy is a novel evaluation metric; de-toned input is
  a separate inference mode, not a data preprocessing step

## Model Architecture
- mT5-small + QLoRA (r=16) — see modeling/lora_config.py for rationale
- Custom SentencePiece tokenizer trained on Tier 1 data
- Full fine-tuning (EXP-03) run only as upper bound

## Data Tiers
- Tier 1 (clean): fine-tuning + evaluation
- Tier 2 (noisy): pre-training only
- Tier 3 (code-switched): secondary experiment only
- **Never mix tiers without explicit labelling**
