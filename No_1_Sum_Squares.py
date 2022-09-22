from functools import reduce

print("-Pisahkan number dgn space-")
numbers_list = [int(item) for item in input("Enter num :").split()]

doubled_numbers = [x*x for x in numbers_list]
sum = reduce(lambda x,y: x+y, doubled_numbers)

print(f'Hasil = {sum}')