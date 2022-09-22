def cd(n):
    sum = int()
    for i in range(1, n + 1):
        sum += i
        n -= 1
    print(f'= {sum}')

cd(int(input("Masukkan angkanya :")))