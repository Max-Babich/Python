def setValues():
    d = dict()
    s = 'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'.replace(
        ', ', '')
    d[s] = 1  # points
    s = 'D, G, Д, К, Л, М, П, У'.replace(', ', '')
    d[s] = 2  # points
    s = 'B, C, M, P, Б, Г, Ё, Ь, Я'.replace(', ', '')
    d[s] = 3  # points
    s = 'F, H, V, W, Y, Й, Ы'.replace(', ', '')
    d[s] = 4  # points
    d['KЖЗХЦЧ'] = 5  # points
    d['JXШЭЮ'] = 8  # points
    d['QZФЩЪ'] = 10  # points

    return d


def calcValue(word, valset):
    d = list(valset.keys())
    s = word.upper()
    value = 0
    for i in s:
        for j in d:
            if j.count(i) > 0:
                value += valset[j]
    return value


def main():
    print(calcValue(input("Please, print the word to assume = "), setValues()))


if __name__ == "__main__":
    main()