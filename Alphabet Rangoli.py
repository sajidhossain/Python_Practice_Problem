import string


def print_rangoli(size):
    alpha = string.ascii_lowercase
    list = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        list.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    reversed_list = list[::-1]
    reversed_list.pop()
    print('\n'.join(reversed_list + list))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
