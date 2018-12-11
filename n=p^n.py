

class Method1:

    def __init__(self, p: int, n: int, polynom):
        self.p = p
        self.n = n
        self.polynom = polynom
        self.fieldC = []
        self.fieldF = []
        self.q = p**n

    def generateField(self):
        # add first element
        elem = [0] * self.n
        self.fieldC.append(elem)

        # add initial elements
        for i in range(self.n-1, 0, -1):
            elem = [0] * self.n
            elem[i-1] = 1
            self.fieldC.append(elem)

        # calculate next element from polynom
        elem = [0] * self.n
        for i in range(1, len(self.polynom)):
            c = self.polynom[i]
            if c == 0:  # no point moving it
                continue
            c = -c
            while (c < 0):
                c += self.p
            elem[i-1] = c
        self.fieldC.append(elem)

        # self.multiply([0, 1, 2], [0, 1, 0])
        # calculate next elements
        for i in range(len(self.fieldC), self.q):
            nextElem = self.multiply(self.fieldC[i-1], self.fieldC[1])
            self.fieldC.append(nextElem)

        # generate F values
        self.calculateFValues()

    def calculateFValues(self):
        for _, coeff in enumerate(self.fieldC):
            value = 0
            for j, c in enumerate(coeff):
                value += c * (self.p**(self.n-j-1))
            self.fieldF.append(value)

    def multiply(self, p1, p2):
        # multiply
        coeffs = [0] * (len(p2)+len(p1)-1)
        for i1, coef1 in enumerate(p1):
            for i2, coef2 in enumerate(p2):
                coeffs[i1 + i2] += coef1 * coef2

        # replace previous term
        diff = len(coeffs) - self.n
        for i in range(diff):
            r = len(coeffs) - i - 1  # rank
            if coeffs[i] != 0:
                for _ in range(coeffs[i]):  # add it as needed
                    for j in range(0 + diff, len(coeffs)):
                        coeffs[j] += self.fieldC[r][j-diff]
                coeffs[i] = 0

        # mod p coefficients
        result = []
        for i in range(len(coeffs)-1, len(coeffs)-self.n-1, -1):
            result.append(coeffs[i] % self.p)
        result.reverse()

        return result

    def printField(self):
        for i in range(len(self.fieldC)):
            print("t^" + str(i) + " = (" + ', '.join(str(x) for x in self.fieldC[i])
                  + ")      f(" + str(i) + ") = " + str(self.fieldF[i]))


def main():
    # TODO:
    # print('p: ')
    # p = input('> ')

    # print('n: ')
    # n = input('> ')

    # print('Polynom Coefficients: ')  # t^3 + 2t +1 -> 1,0,2,1
    # polynom = [int(n) for n in input('> ').split(',')]

    m = Method1(int(3), int(3), [1, 0, 2, 1])

    m.generateField()
    m.printField()


if __name__ == '__main__':
    main()
