# Appendix J — The Invariant Core of Hebrew Recursion  
**Aleph Systems and the 5-Letter Attractor Substructure**

**Author:** S.C. Jones **Edition:** 2026

## J.0 — Overview

This appendix isolates the internal engine of Hebrew recursion:

- Single-letter recursion (Aleph)
- The minimal 5-letter core (ד, ל, ת, י, ו)

Both converge to the same dominant eigenvalue as the full alphabet in each historical form.

## J.1 — Structural Claim

The dominant eigenvalue is scale-invariant across:

- Single-letter recursion (Aleph)
- Reduced 5-letter core
- Full 22-letter system

The same governing constant appears at multiple scales of the recursive architecture.

## J.2 — Scale Invariance

The recurrence behavior observed in the full Hebrew recursion systems is already encoded in the smallest stable subsystems.

This demonstrates that the governing attractor is not a large-scale averaging artifact, but an intrinsic property of the recursive structure itself.

## J.3 — Recursive Stability

Removing transient outer structures does not destroy the dominant attractor.

The governing eigenvalue persists within the minimal internally connected core.

This stability across scale is one of the defining properties of the system.

## J.4 — Aleph (Paleo) Recursion

Growth sequence:

1 → 3 → 8 → 20 → 48 → 112 → 256 → 576 → 1,280 → …

Convergence:

$$
\lambda = 2.0
$$

## J.5 — Aleph (Masoretic) Recursion

Growth sequence:

1 → 3 → 8 → 20 → 48 → 113 → …

Convergence:

$$
\lambda = 1 + 2\cos\left(\frac{\pi}{7}\right)
\approx 2.8019377358
$$

## J.6 — 5-Letter Core (Paleo)

Growth sequence:

5 → 11 → 25 → 56 → 124 → 272 → 592 → 1,280 → …

Convergence:

$$
\lambda = 2.0
$$

## J.7 — 5-Letter Core (Masoretic)

Growth sequence:

5 → 13 → 35 → 95 → 261 → 723 → …

Convergence:

$$
\lambda \approx 2.8019377358
$$

## J.8 — Python Verification

```python
# See:
# code/paleo_aleph.py
# code/masoretic_aleph.py
# code/five_letter_core.py
```

## J.9 — Reproducibility Statement

All results are deterministic.

Matrices, eigenvalues, and growth tables are generated directly from the recursive spellings and stored in the `results/` folder.

Running the associated scripts reproduces the complete outputs.

## J.10 — Conclusion

The governing constant is encoded at every level of the structure.

The smallest recursive units already contain the full attractor behavior of the larger system.

The architecture remains coherent across scale, reduction, and historical transformation.