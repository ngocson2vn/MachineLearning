import matplotlib.pyplot as g
import sys

# houseSizes = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
# housePrices = [245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000]
SP = [(1400, 245000), (1600, 312000), (1700, 279000), (1875, 308000), (1100, 199000), (1550, 219000), (2350, 405000), (2450, 324000), (1425, 319000), (1700, 255000)]

def main():
    # SP = []
    # for i in range(0, len(houseSizes)):
    #     print(i)
    #     SP.append((houseSizes[i], housePrices[i]))

    # print(SP)

    SP.sort(key=lambda e: e[0])
    print(SP)
    X = []
    Y = []
    for e in SP:
        X.append(e[0])
        Y.append(e[1])

    g.plot(X, Y)
    g.xlabel("House Size (Sq. Ft.)")
    g.ylabel("House Price ($)")
    g.show()

if __name__ == "__main__":
    main()
