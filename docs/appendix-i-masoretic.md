# Appendix I — The Masoretic Recursion Engine  
**Stable Transformation and the λ = 1 + 2cos(π/7) Attractor**

**Author:** S.C. Jones **Edition:** 2026

## I.0 — Overview

This appendix presents the Masoretic form of the Hebrew recursion system. After the historical introduction of internal vowel letters, the system converges to the precise algebraic attractor:

$$
\lambda = 1 + 2\cos\left(\frac{\pi}{7}\right) \approx 2.8019377358
$$

Visual recursion traces are provided in the accompanying **Eigenvalue 2.0 SRT Chart**.

## I.1 — Structural Claim

The Masoretic Hebrew alphabet forms a closed recursive system whose growth is governed by the exact dominant eigenvalue above.

This value appears in the full 22-letter system, reduced subsystems, and single-letter recursion (see Appendix J).

## I.2 — Methods

The recursion is defined identically to Appendix H using the incidence matrix method.

Let \( \mathbf{v}_n \) be the letter-count vector at generation \( n \), and let \( A \) be the \(22 \times 22\) incidence matrix where \( A_{ij} \) is the number of occurrences of letter \( i \) in the milui expansion of letter \( j \).

The recursive update rule is:

$$
\mathbf{v}_{n+1} = A \cdot \mathbf{v}_n
$$

By the Perron–Frobenius theorem, long-run growth is governed by the dominant eigenvalue of \( A \).

## I.3 — Masoretic Milui Definitions

See `data/spellings_masoretic.csv`.

## I.4 — Growth Evidence

Initial condition:

- Gen 0 = 22

Recursive expansion:

22 → 62 → 168 → 456 → 1,245 → 3,425 → 9,487 → 26,419 → …

Growth ratios converge to:

$$
\lambda \approx 2.8019377358
$$

## I.5 — Eigenvalue Verification

Dominant eigenvalue:

$$
\lambda = 1 + 2\cos\left(\frac{\pi}{7}\right)
\approx 2.8019377358
$$

Computed directly from the incidence matrix in:

`results/masoretic_22_matrix.csv`

## I.6 — Structural Interpretation

The Masoretic refinements introduce minimal orthographic changes that shift the dominant eigenvalue from exact doubling (\(\lambda = 2.0\)) to the 7th-cyclotomic attractor while preserving closure and rapid stabilization.

## I.7 — Subsystem Link

The same eigenvalue appears in:

- Single-letter recursion (Aleph)
- Reduced 5-letter core
- Full 22-letter recursion

The governing constant is preserved across scale.

## I.8 — Cyclotomic Structure of the Eigenvalue

The value:

$$
\lambda = 1 + 2\cos\left(\frac{\pi}{7}\right)
$$

belongs to the 7th cyclotomic field and encodes seven-fold rotational symmetry.

## I.9 — Python Verification

```python
# See code/masoretic_22.py
# Running this script reproduces the matrix and growth table.
```

## I.10 — Reproducibility Statement

All results are deterministic and reproducible from the milui spellings in:

`data/spellings_masoretic.csv`

Running `code/masoretic_22.py` regenerates the matrices, eigenvalues, and growth tables contained in the `results/` folder.

## I.11 — Conclusion

Two historical forms. Two stable attractors.

The system remains coherent under transformation. The governing constant is preserved across scale.

Full results:

- `results/masoretic_22_matrix.csv`
- `results/masoretic_22_output.txt`