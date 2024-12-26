def dp_iteratif(tugas, pekerja):
    """
    Solusi Dynamic Programming Iteratif untuk distribusi beban kerja.
    Args:
        tugas (list): Daftar durasi tugas.
        pekerja (int): Jumlah pekerja.
    Returns:3
        int: Makespan minimum (waktu yang diambil oleh pekerja dengan beban paling berat).
    """
    n = len(tugas)
    dp = [[float('inf')] * (pekerja + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for k in range(1, pekerja + 1):
            total_sekarang = 0
            for j in range(i, 0, -1):
                total_sekarang += tugas[j - 1]
                dp[i][k] = min(dp[i][k], max(dp[j - 1][k - 1], total_sekarang))

    return dp[n][pekerja]

# Meminta input dari pengguna
tugas = list(map(int, input("Masukkan durasi tugas (pisahkan dengan spasi): ").split()))
pekerja = int(input("Masukkan jumlah pekerja: "))

# Menjalankan algoritma dan mencetak hasil
print("Dynamic Programming Iteratif Makespan Minimum:", dp_iteratif(tugas, pekerja))
