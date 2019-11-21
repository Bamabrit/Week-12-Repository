# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(2,100):

        fibs.append(fibs[i-2]+fibs[i-1])

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
