def dp_rekursif(tugas, pekerja):
    """
    Solusi Dynamic Programming Rekursif untuk distribusi beban kerja.
    Args:
        tugas (list): Daftar durasi tugas.
        pekerja (int): Jumlah pekerja.
    Returns:
        int: Makespan minimum (waktu yang diambil oleh pekerja dengan beban paling berat).
    """
    memo = {}

    def helper(i, k):
        if k == 1:
            return sum(tugas[:i])
        if (i, k) in memo:
            return memo[(i, k)]

        total_sekarang = 0
        hasil = float('inf')
        for j in range(i, 0, -1):
            total_sekarang += tugas[j - 1]
            hasil = min(hasil, max(helper(j - 1, k - 1), total_sekarang))

        memo[(i, k)] = hasil
        return hasil

    return helper(len(tugas), pekerja)

# Meminta input dari pengguna
tugas = list(map(int, input("Masukkan durasi tugas (pisahkan dengan spasi): ").split()))
pekerja = int(input("Masukkan jumlah pekerja: "))

# Menjalankan algoritma dan mencetak hasil
print("Dynamic Programming Rekursif Makespan Minimum:", dp_rekursif(tugas, pekerja))
