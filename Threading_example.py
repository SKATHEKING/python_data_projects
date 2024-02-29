import threading
import time


def long_square(num):
    time.sleep(1)
    results = {num: num ** 3}
    return results


def main():
    print([long_square(n) for n in range(0, 10)])
    #Threading
    results = {}
    t1 = [threading.Thread(target=long_square, args=(n, results)) for n in range(0, 10)]
    t2 = [threading.Thread(target=long_square, args=(n, results)) for n in range(10, 20)]

    [t.start() for t in t1]
    [t.join() for t in t1]

    print(results)

    [t.start() for t in t2]
    [t.join() for t in t2]

    print(results)

main()
