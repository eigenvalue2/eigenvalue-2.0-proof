import numpy as np

letters = ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת']
core_idx = [3, 11, 21, 9, 5]  # indices for ד, ל, ת, י, ו

paleo_milui = {
    'א':'אלף','ב':'בת','ג':'גמל','ד':'דלת','ה':'הה','ו':'וו',
    'ז':'זין','ח':'חת','ט':'טת','י':'יד','כ':'כף','ל':'למד',
    'מ':'מם','נ':'נן','ס':'סמכ','ע':'ענ','פ':'פה','צ':'צד',
    'ק':'קף','ר':'רש','ש':'שנ','ת':'תו'
}

final_map = {'ך':'כ','ם':'מ','ן':'נ','ף':'פ','ץ':'צ'}

A = np.zeros((22, 22))

for i, let in enumerate(letters):
    for char in paleo_milui[let]:
        ch = final_map.get(char, char)
        if ch in letters:
            j = letters.index(ch)
            A[j, i] += 1

# Restrict to 5-letter core
A_core = A[np.ix_(core_idx, core_idx)]

evals = np.linalg.eigvals(A_core)
print("5-Letter Core (Paleo) Dominant eigenvalue:", max(np.abs(evals).real))

v = np.ones(5)
print("Gen 0:", int(v.sum()))
for n in range(1, 9):
    v = A_core @ v
    print(f"Gen {n}:", int(round(v.sum())))