#Data jumlah siswa kelas 12 MIPA
data = [35, 30, 35, 30, 24]

# 1. Menghitung Modus
from collections import Counter

#Hitung frekuensi setiap nilai
frekuensi = Counter(data)

#Cari nilai dengan frekuensi tertinggi
modus = [nilai for nilai, jumlah in frekuensi.items() if jumlah == max(frekuensi.values())]

print(f"Modus: {modus}")


# 2. Menghitung Median
#Urutkan data terlebih dahulu
data.sort()

#Hitung median
n = len(data)
if n % 2 == 0:  # Jika jumlah data genap
    median = (data[n // 2 - 1] + data[n // 2]) / 2
else:  # Jika jumlah data ganjil
    median = data[n // 2]

print(f"Median: {median}")


# 3. Menghitung Mean
#Jumlahkan semua nilai dan bagi dengan banyaknya data
mean = sum(data) / len(data)

print(f"Mean: {mean}")