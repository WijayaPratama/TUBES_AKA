import random
import time
import matplotlib.pyplot as plt

def fpb_iteratif(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fpb_array_iteratif(arr):
    result = arr[0]
    for num in arr[1:]:
        result = fpb_iteratif(result, num)
        if result == 1:  # Jika FPB sudah 1, tidak perlu dilanjutkan
            break
    return result

# Fungsi untuk mencari FPB secara rekursif
def fpb_rekursif(a, b):
    if b == 0:
        return a
    return fpb_rekursif(b, a % b)

  # Fungsi untuk mencari FPB dari array menggunakan algoritma rekursif
def fpb_array_rekursif(arr):
    result = arr[0]
    for num in arr[1:]:
        result = fpb_rekursif(result, num)
        if result == 1:  # Jika FPB sudah 1, tidak perlu dilanjutkan
            break
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def non_prime(start, end):
    while True:
        num = random.randint(start, end)
        if not is_prime(num):
            return num
        
lengths = [1000, 10000, 100000, 1000000, 10000000]

iteratif_times = []
rekursif_times = []

print("Panjang Array | Waktu Eksekusi Iteratif | Waktu Eksekusi Rekursif | Hasil Iteratif | Hasil Rekursif")
print("--------------------------------------------------------")

for length in lengths:
      # Membuat array dengan angka random
      arr = [random.randint(10000,100000) for _ in range(length)]

      # Mengukur waktu eksekusi untuk algoritma iteratif
      start_time = time.perf_counter()
      result1 = fpb_array_iteratif(arr)
      end_time = time.perf_counter()
      iteratif_times.append(end_time - start_time)

      # Mengukur waktu eksekusi untuk algoritma rekursif
      start_time = time.perf_counter()
      result2 = fpb_array_rekursif(arr)
      end_time = time.perf_counter()
      rekursif_times.append(end_time - start_time)

      # Menampilkan hasil waktu
      print(f"{length:<14} | {iteratif_times[-1]:.10f} | {rekursif_times[-1]:.10f} | {result1} | {result2}")

  # Membuat grafik perbandingan waktu eksekusi antara iteratif dan rekursif
plt.figure(figsize=(10, 6))
plt.plot(lengths, iteratif_times, label='Iteratif', color='blue', marker='o')
plt.plot(lengths, rekursif_times, label='Rekursif', color='red', marker='x')

  # Gunakan skala logaritmik pada sumbu x (panjang array)
plt.xscale('log')  # Menggunakan skala logaritmik pada sumbu X

  # Menambah label dan judul
plt.xlabel('Panjang Array (log scale)')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Perbandingan Waktu Eksekusi FPB - Iteratif vs Rekursif')
plt.legend()
plt.grid(True)

  # Menampilkan grafik
plt.show()