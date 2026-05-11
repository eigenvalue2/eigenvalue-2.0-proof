# Eigenvalue 2.0 — The Measurable Architecture of Hebrew Recursion

**Exact Doubling (Paleo/Sinai) · Cyclotomic Attractor (Masoretic) · Scale-Invariant Core**

A symbolic recursion system producing exact algebraic attractors under closed internal recursion.

This repository contains the complete mathematical framework and reproducible verification materials from Appendices H–J of the book *Eigenvalue 2.0 — The Miracle Is the Architecture*.

---

## Five Independent Verifications

| System | Eigenvalue | Description |
|---|---|---|
| Full 22-Letter Paleo/Sinai | **λ = 2.0** | Exact lossless doubling |
| Full 22-Letter Masoretic | **λ ≈ 2.8019377358** | \(1 + 2\cos(\pi/7)\) |
| Aleph (single-letter) Paleo | **λ = 2.0** | Scale-invariant recursion |
| Aleph (single-letter) Masoretic | **λ ≈ 2.8019377358** | Scale-invariant recursion |
| 5-Letter Core (ד, ל, ת, י, ו) | Same as above | Minimal invariant subsystem |

---

## Quick Start (20 seconds)

```bash
# 1. Install requirements
pip install numpy pandas

# 2. Run the verification scripts
python code/paleo_22.py
python code/masoretic_22.py
python code/paleo_aleph.py
python code/masoretic_aleph.py
python code/five_letter_core.py
python code/five_letter_core_masoretic.py
```

The scripts reproduce the matrices, seed vectors, eigenvalues, and growth tables contained in the `results/` folder.

---

## Repository Contents

| Folder | Description |
|---|---|
| `data/` | Raw milui spellings (Paleo and Masoretic) |
| `code/` | Reproducible Python scripts for matrix construction and eigenvalue computation |
| `results/` | Incidence matrices (`.csv`) and growth tables (`.txt`) |
| `docs/` | Mathematical appendices (H, I, J) |
| `images/` | Visual recursion charts and supporting graphics |

---

## The Appendices

| File | Description |
|---|---|
| `docs/appendix-h-sinai.md` | Paleo/Sinai recursion system — exact \( \lambda = 2.0 \) |
| `docs/appendix-i-masoretic.md` | Masoretic recursion system — \( \lambda = 1 + 2\cos(\pi/7) \) |
| `docs/appendix-j-invariant_core.md` | Aleph recursion and 5-letter invariant core |

---

## Reproducibility

All results are deterministic and fully reproducible.

The incidence matrices are constructed directly from the attested milui spellings contained in `data/`.

Running the scripts in `code/` regenerates the exact matrices, eigenvalues, and growth tables referenced throughout the appendices.

The architecture is measurable.

---

## Mathematical Framework

The recursive systems are represented by incidence matrices \( A \), where each entry \( A_{ij} \) counts the occurrences of letter \( i \) within the milui expansion of letter \( j \).

Recursive growth follows:

$$
\mathbf{v}_{n+1} = A \cdot \mathbf{v}_n
$$

Long-run behavior is governed by the dominant eigenvalue of the system matrix.

---

## Author

**S.C. Jones**  
Edition: 2026

---

## License

See `LICENSE.md`

---

## Additional Materials

For the full book, charts, media, and supplementary materials:

https://eigenvalue2.com