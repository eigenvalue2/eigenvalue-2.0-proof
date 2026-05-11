# Appendix H — The Paleo/Sinai Recursion Engine  
**Exact Doubling and the λ = 2.0 Attractor**

**Author:** S.C. Jones **Edition:** 2026

## H.0 — Overview

This appendix presents the Paleo/Sinai form of the Hebrew recursion system. Using attested milui (spelled-out) forms of the 22 letters, the system produces **exact, lossless doubling** governed by:

$$
\lambda = 2.0
$$

Visual recursion traces, letter-by-letter substitution patterns, and higher-generation detail are provided in the accompanying **Eigenvalue 2.0 SRT Chart** (see `images/chart.png`).

## H.1 — Structural Claim

The Paleo/Sinai Hebrew alphabet forms a closed recursive system whose growth is governed by an exact dominant eigenvalue:

$$
\lambda = 2.0
$$

This value appears in the full 22-letter system, reduced subsystems, and single-letter recursion (see Appendix J).

## H.2 — Methods

The recursion is defined by the internal spelling (milui) of each letter.

Let \( \mathbf{v}_n \) be the letter-count vector at generation \( n \), and let \( A \) be the \(22 \times 22\) incidence matrix where \( A_{ij} \) is the number of occurrences of letter \( i \) in the milui expansion of letter \( j \).

The recursive update rule is:

$$
\mathbf{v}_{n+1} = A \cdot \mathbf{v}_n
$$

By the Perron–Frobenius theorem, long-run growth is governed by the dominant eigenvalue of \( A \).

## H.3 — Paleo/Sinai Milui Definitions

See `data/spellings_paleo.csv`.

## H.4 — Growth Evidence

Initial condition:

- Gen 0 = 22

Recursive expansion:

22 → 50 → 112 → 249 → 550 → 1,207 → 2,632 → 5,705 → …

Growth ratios converge exactly to 2.0.

## H.5 — Eigenvalue Verification

Dominant eigenvalue:

$$
\lambda = 2.0
$$

Computed directly from the incidence matrix in:

`results/paleo_22_matrix.csv`

## H.8 — Python Verification (Reproducible)

```python
# See code/paleo_22.py
# Running this script builds the matrix,
# computes the eigenvalue,
# and saves results/
```

## H.9 — Reproducibility Statement

All results are deterministic.

The incidence matrix is built directly from the milui spellings in:

`data/spellings_paleo.csv`

Running `code/paleo_22.py` regenerates everything in the `results/` folder.

## H.10 — Conclusion

One system. One governing constant. Exact convergence.

The dominant eigenvalue is invariant across scale. The architecture is measurable.

Full results:

- `results/paleo_22_matrix.csv`
- `results/paleo_22_output.txt`