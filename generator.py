import random

class Generator:
    def __init__(self):
        self.n= int(input("Give number of equations/unknowns"))
        self.solutions = []
        self.coef = []
        self.results = []
        self.boot()

    def boot(self):

        for i in range(self.n):
            self.solutions.append(random.randint(-10,10))

        for i in range(self.n):
            aux = []
            for j in range(self.n):
                aux.append(random.randint(-10,10))

            self.coef.append(aux)

        for i in range(self.n):
            sum = 0
            for j in range(self.n):
                sum = sum+ self.coef[i][j]*self.solutions[j]
            self.results.append(sum)

    def print_sistem(self):

        for i in range(self.n):
            for j in range(self.n):
                if(self.coef[i][j] > 0):
                    print("+" + str(self.coef[i][j]) + "*x"+str(j), end =" ")

                else:
                    print(str(self.coef[i][j]) + "*x"+str(j), end =" ")
            print("= " + str(self.results[i]))

        print(self.solutions)