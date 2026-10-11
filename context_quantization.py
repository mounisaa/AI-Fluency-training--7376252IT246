"""
Day 4 - Context Length and Quantization Experiment

This script demonstrates how changing context length
and quantization affects estimated memory usage.
"""

# 8B model
PARAMS_B = 8.0

# Memory budget from the Day 4 hardware estimator
MEMORY_BUDGET = 10.8

# Weight bytes per parameter used by the Day 4 estimator
BYTES_PER_PARAM = {
    "Q3_K_M": 0.43,
    "Q4_K_M": 0.57,
    "Q5_K_M": 0.68,
    "Q8_0": 1.0,
    "FP16": 2.0,
}

# KV cache for the 8B model at 8K context
# Based on the Day 4 estimator:
# 8K = 1.28 GB
KV_AT_8K = 1.28


def calculate_weights(params_b, precision):
    """Calculate approximate weight memory."""
    return params_b * BYTES_PER_PARAM[precision]


def calculate_kv(context_k):
    """Calculate approximate KV cache.

    The Day 4 estimator uses approximately linear growth
    with context length.
    """
    return KV_AT_8K * (context_k / 8)


def calculate_total(weights, kv):
    """Calculate estimated total memory including overhead."""
    overhead = 0.58
    return weights + kv + overhead


print("=" * 70)
print("DAY 4 - CONTEXT LENGTH EXPERIMENT")
print("=" * 70)

precision = "Q4_K_M"
weights = calculate_weights(PARAMS_B, precision)

for context in [4, 8, 32, 128]:
    kv = calculate_kv(context)
    total = calculate_total(weights, kv)

    fits = "YES" if total <= MEMORY_BUDGET else "NO"

    print(
        f"Context: {context:>3}K | "
        f"Quantization: {precision:<6} | "
        f"Weights: {weights:>5.2f} GB | "
        f"KV: {kv:>5.2f} GB | "
        f"Total: {total:>5.2f} GB | "
        f"Fits: {fits}"
    )


print()
print("=" * 70)
print("DAY 4 - QUANTIZATION EXPERIMENT")
print("=" * 70)

context = 8

for precision in ["Q3_K_M", "Q4_K_M", "Q5_K_M", "Q8_0", "FP16"]:
    weights = calculate_weights(PARAMS_B, precision)
    kv = calculate_kv(context)
    total = calculate_total(weights, kv)

    fits = "YES" if total <= MEMORY_BUDGET else "NO"

    print(
        f"Quantization: {precision:<6} | "
        f"Context: {context:>2}K | "
        f"Weights: {weights:>5.2f} GB | "
        f"KV: {kv:>5.2f} GB | "
        f"Total: {total:>5.2f} GB | "
        f"Fits: {fits}"
    )

print("=" * 70)