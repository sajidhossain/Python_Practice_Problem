if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(n for n in integer_list)
    print(t)
    print(hash(t))
