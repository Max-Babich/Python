def Next(start, delta, number):
    return [start+delta*(i-1) for i in range(1,number+1) ]

def main():
    print(Next(int(input()),int(input()),int(input())))


if __name__ == '__main__':
    main()