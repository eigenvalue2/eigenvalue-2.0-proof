import numpy as np
import pandas as pd

letters = ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת']

# Core letters: ד ל ת י ו
core_idx = [3, 11, 21, 9, 5]

mas_milui = {
    'א':'אלף',
    'ב':'בית',
    'ג':'גימל',
    'ד':'דלת',
    'ה':'הה',
    'ו':'ויו',
    'ז':'זין',
    'ח':'חית',
    'ט':'טית',
    'י':'יוד',
    'כ':'כף',
    'ל':'למד',
    'מ':'מם',
    'נ':'נון',
    'ס':'סמך',
    'ע':'עין',
    'פ':'פה',
    'צ':'צדי',
    'ק':'קוף',
    'ר':'ריש',
    'ש':'שין',
    'ת':'תו'
}

final_map = {
    'ך':'כ',
    'ם':'מ',
    'ן':'נ',
    'ף':'פ',
    'ץ':'צ'
}

A = np.zeros((22,22), dtype=int)

for i, let in enumerate(letters):
    for char in mas_milui[let]:
        ch = final_map.get(char, char)
        if ch in letters:
            j = letters.index(ch)
            A[j,i] += 1

# Restrict to 5-letter core
A_core = A[np.ix_(core_idx, core_idx)]

core_letters = ['ד','ל','ת','י','ו']

# Save matrix CSV
df = pd.DataFrame(A_core, index=core_letters, columns=core_letters)
df.to_csv("results/five_letter_core_masoretic_matrix.csv")

# Eigenvalue
evals = np.linalg.eigvals(A_core)
dominant = max(np.abs(evals).real)

# Growth recursion
v = np.ones(5, dtype=int)

lines = []
lines.append(f"Dominant eigenvalue: {dominant}")
lines.append("")
lines.append("Generation | Total Letters")
lines.append("-----------|--------------")
lines.append(f"Gen 0: {int(v.sum())}")

for n in range(1, 11):
    v = A_core @ v
    lines.append(f"Gen {n}: {int(round(v.sum()))}")

# Save output txt
with open("results/five_letter_core_masoretic_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# Console print
print("\n".join(lines))