# i = 1
# while i <= 5:
#     print("*")
#     i += 1

n=5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))