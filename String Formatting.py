def print_formatted(number):
    w = len("{0:b}".format(number))
    for i in range(1, n + 1):
        o = oct(i)[2:]
        h = hex(i)[2:]
        b = bin(i)[2:]
        print(str(i).rjust(w), o.rjust(w), h.upper().rjust(w), b.rjust(w))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
