def evaluate_performance(percentage):
    # Memeriksa apakah persentase >= 90, jika iya, tampilkan "Excellent performance"
    if percentage >= 90:
        return "Excellent performance"
    # Memeriksa apakah persentase >= 80, jika iya, tampilkan "Very Good performance"
    elif percentage >= 80:
        return "Very Good performance"
    # Memeriksa apakah persentase >= 70, jika iya, tampilkan "Good performance"
    elif percentage >= 70:
        return "Good performance"
    # Memeriksa apakah persentase >= 60, jika iya, tampilkan "Average performance"
    elif percentage >= 60:
        return "Average performance"
    # Jika persentase di bawah 60, tampilkan "Needs Improvement"
    else:
        return "Needs Improvement"

# Contoh penggunaan
percentage = float(input("Masukkan persentase siswa: "))  # Input persentase dari pengguna
print(evaluate_performance(percentage))  # Cetak hasil evaluasi berdasarkan persentase

def find_largest(a, b, c):
    # Memeriksa apakah a adalah angka terbesar
    if a >= b and a >= c:
        return a
    # Memeriksa apakah b adalah angka terbesar
    elif b >= a and b >= c:
        return b
    # Jika tidak, c adalah angka terbesar
    else:
        return c

# Contoh penggunaan
a = float(input("Masukkan angka pertama: "))  # Input angka pertama
b = float(input("Masukkan angka kedua: "))  # Input angka kedua
c = float(input("Masukkan angka ketiga: "))  # Input angka ketiga

# Cetak angka terbesar di antara ketiganya
print("Angka terbesar adalah:", find_largest(a, b, c))

def fibonacci(n):
    # Inisialisasi dua angka pertama dalam deret Fibonacci
    a, b = 0, 1
    fib_series = []  # Daftar kosong untuk menyimpan deret Fibonacci
    # Loop selama a masih lebih kecil atau sama dengan n
    while a <= n:
        fib_series.append(a)  # Tambahkan angka Fibonacci ke dalam daftar
        a, b = b, a + b  # Hitung angka berikutnya dalam deret Fibonacci
    return fib_series  # Kembalikan deret Fibonacci sebagai daftar

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))  # Input batas deret Fibonacci
# Cetak deret Fibonacci hingga n
print("Deret Fibonacci hingga", n, ":", fibonacci(n))

def print_odd_numbers(n):
    # Loop dari 1 hingga n
    for i in range(1, n+1):
        if i % 2 != 0:  # Memeriksa apakah angka adalah ganjil
            print(i, end=" ")  # Cetak angka ganjil di satu baris

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))  # Input batas bilangan ganjil
print("Bilangan ganjil hingga", n, ":")
print_odd_numbers(n)  # Cetak bilangan ganjil hingga n

def print_pattern(n):
    # Loop untuk setiap baris dari 1 hingga n
    for i in range(1, n + 1):
        # Cetak angka i sebanyak i kali di setiap baris
        print((str(i) + " ") * i)

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))  # Input nilai n dari pengguna
print_pattern(n)  # Cetak pola angka berdasarkan nilai n
