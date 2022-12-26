n, m = input().split()
m = int(m)
n = int(n)

# Upper Portion
for i in range(n // 2):
    print('-' * ((m - 3) // 2 - (i * 3)) + '.|.' * (2 * i + 1) + '-' * ((m - 3) // 2 - (i * 3)))

# Middle Portion
print('-' * ((m - 7) // 2) + 'WELCOME' + '-' * ((m - 7) // 2))

# Lower Portion
for i in range(n // 2):
    print('-' * ((i + 1) * 3) + '.|.' * (n - 2 - 2 * i) + '-' * ((i + 1) * 3))
