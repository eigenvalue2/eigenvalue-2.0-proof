import numpy as np

letters = ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת']

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

# Start with single Aleph (index 0)
v = np.zeros(22)
v[0] = 1

print("Aleph Paleo - Gen 0: 1")
for n in range(1, 10):
    v = A @ v
    print(f"Gen {n}:", int(round(v.sum())))