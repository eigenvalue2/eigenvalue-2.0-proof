import numpy as np

letters = ['א','ב','ג','ד','ה','ו','ז','ח','ט','י','כ','ל','מ','נ','ס','ע','פ','צ','ק','ר','ש','ת']

mas_milui = {
    'א':'אלף','ב':'בית','ג':'גימל','ד':'דלת','ה':'הה','ו':'ויו',
    'ז':'זין','ח':'חית','ט':'טית','י':'יוד','כ':'כף','ל':'למד',
    'מ':'מם','נ':'נון','ס':'סמך','ע':'עין','פ':'פה','צ':'צדי',
    'ק':'קוף','ר':'ריש','ש':'שין','ת':'תו'
}

final_map = {'ך':'כ','ם':'מ','ן':'נ','ף':'פ','ץ':'צ'}

A = np.zeros((22, 22))

for i, let in enumerate(letters):
    for char in mas_milui[let]:
        ch = final_map.get(char, char)
        if ch in letters:
            j = letters.index(ch)
            A[j, i] += 1

# Start with single Aleph (index 0)
v = np.zeros(22)
v[0] = 1

print("Aleph Masoretic - Gen 0: 1")
for n in range(1, 11):
    v = A @ v
    print(f"Gen {n}:", int(round(v.sum())))