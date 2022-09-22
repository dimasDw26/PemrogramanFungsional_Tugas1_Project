from functools import reduce
n, m = map(int, input("Masukkan angka & pangkatnya :").split())

try:
    if n < 0 or m < 0:
        raise AssertionError()
    else:
        a = []
        for i in range(0, m):
            if m != 0:
                a.append(n)
            else:
                break
            m -= 1
        sum = reduce(lambda x, y: x * y, a)
        print(f"Hasil = {sum}")
except AssertionError:
    print("nilai yang anda masukkan bernilai nagatif")