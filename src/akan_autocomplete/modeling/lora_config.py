"""LoRA / QLoRA configuration.

Why LoRA:
  - Freezes pre-trained weights, trains <1% of parameters
  - Prevents catastrophic forgetting on small Akan datasets
  - Fits on a single T4 (Google Colab) via QLoRA 4-bit quantisation

Why NOT full fine-tuning of mT5-base:
  - Requires 40 GB+ VRAM
  - High risk of catastrophic forgetting on ~10 MB of Akan data
"""
from peft import LoraConfig, TaskType


def get_lora_config(r: int = 16, lora_alpha: int = 32) -> LoraConfig:
    return LoraConfig(
        task_type=TaskType.SEQ_2_SEQ_LM,
        r=r,
        lora_alpha=lora_alpha,
        target_modules=["q", "v"],   # query + value attention matrices
        lora_dropout=0.05,
        bias="none",
    )
