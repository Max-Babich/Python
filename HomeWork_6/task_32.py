def indexes(list: list, a: int, b: int):
    return [i for i in range(len(list)) if list[i] in range(a, b+1)]


def main():
    print(indexes([-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7], 6, 12))


if __name__ == '__main__':
    main()