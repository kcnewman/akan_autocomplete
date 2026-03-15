"""Experiment matrix runner — EXP-01 through EXP-09.

Each experiment writes results to experiments/EXP-XX/results.json.
Run via: python scripts/run_experiment.sh EXP-04
"""
EXP_REGISTRY = {
    "EXP-01": "ABENA zero-shot masked prediction on test set",
    "EXP-02": "mT5-small zero-shot on autocomplete prompts",
    "EXP-03": "mT5-small full fine-tuning on Tier 1 data",
    "EXP-04": "mT5-small + LoRA (r=8) on Tier 1 data",
    "EXP-05": "mT5-small + LoRA (r=16) on Tier 1 data",
    "EXP-06": "mT5-small + LoRA (r=16) on Tier 1+2 data",
    "EXP-07": "mT5-small + LoRA + custom tokenizer",
    "EXP-08": "EXP-05 on code-switched test subset",
    "EXP-09": "Dialect generalisation: Akuapem test set",
}
