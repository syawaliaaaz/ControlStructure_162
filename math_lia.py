import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r

#contoh penggunaan
jari_jari = 7
area = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari - jari {jari_jari} adalah {area:.2f}")