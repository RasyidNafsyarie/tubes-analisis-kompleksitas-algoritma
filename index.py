import time
import matplotlib.pyplot as plt
import random
from dp_iterative import dp_iteratif
from dp_recursive import dp_rekursif

# Fungsi untuk mengukur waktu eksekusi
def ukur_waktu(algoritma, tugas, pekerja):
    start_time = time.time()
    algoritma(tugas, pekerja)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Waktu eksekusi untuk {algoritma.__name__}: {runtime:.6f} detik")
    return runtime

# Ukuran masukan yang akan diuji
ukuran_masukan = [1, 10, 20, 50, 100, 200, 500, 1000, 2000]
pekerja = 5  # Jumlah pekerja tetap untuk semua pengujian

# Hasil waktu eksekusi untuk masing-masing algoritma
waktu_iteratif = []
waktu_rekursif = []

for n in ukuran_masukan:
    # Membuat tugas secara acak
    tugas = [random.randint(1, 100) for _ in range(n)]
    
    print(f"\nMengukur untuk n={n} tugas")
    
    # Mengukur waktu untuk DP Iteratif
    waktu_iteratif.append(ukur_waktu(dp_iteratif, tugas, pekerja))
    
    # Mengukur waktu untuk DP Rekursif
    waktu_rekursif.append(ukur_waktu(dp_rekursif, tugas, pekerja))

# Plot hasil
plt.figure(figsize=(10, 6))
plt.plot(ukuran_masukan, waktu_iteratif, label="DP Iteratif", marker="o")
plt.plot(ukuran_masukan, waktu_rekursif, label="DP Rekursif", marker="o")
plt.xlabel("Jumlah Tugas (n)")
plt.ylabel("Waktu Eksekusi (detik)")
plt.title("Perbandingan Running Time: Iteratif vs Rekursif")
plt.legend()
plt.grid()
plt.show()
