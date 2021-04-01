nama = input("Masukkan nama anda")
nilai = int(input('Berapa nilai anda?'))

if nilai >= 85 and nilai <= 100:
    grade = 'A'
elif nilai >= 80 and nilai <= 84:
    grade = 'A-'
elif nilai >= 75 and nilai <= 79:
    grade = 'B+'
elif nilai >= 70 and nilai <= 74:
    grade = 'B'
elif nilai >= 65 and nilai <= 69:
    grade = 'C+'
elif nilai >= 60 and nilai <= 64:
    grade = 'C'
elif nilai < 60:
    grade = 'E'
else:
    grade = "tidak valid"
print('Halo,',nama, '! Nilai anda setelah dikonversikan adalah {}'.format(grade))