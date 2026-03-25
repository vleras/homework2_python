
def divisible_by_3(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            yield i

n = 20

for num in divisible_by_3(n):
    print(num) 