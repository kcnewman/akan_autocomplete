"""QLoRA fine-tuning loop for mT5-small + PEFT.

Stack: transformers + peft + bitsandbytes + accelerate + unsloth (2-4x speedup)
Log: wandb (free tier, log PPL / loss / LR / KSR per epoch)
Checkpoint: every 500 steps — loss of a training run = weeks lost.
"""
# TODO: implement Trainer subclass or use HuggingFace Trainer with callbacks
# TODO: pin seeds — transformers.set_seed(42), numpy, torch, random
