import numpy as np
import random
#function that returns a list of strings, each one representing an equation

''' PARSING STAGE '''

#read contents of the file
def getFileContent(filename):
    # equations[] will contatin the raw equations from the file as strings
    equations = []

    with open(filename) as file:
        equations = file.readlines()

    # remove \n from the strings
    equations = [x.strip() for x in equations]
    return equations

'''

getCoefficients extracts the coefficients, free terms and variables from the strings
representing the equations

 '''

def getCoefficientsAndFreeTerms(equations):
    # leftHandSide and rightHandSide of the equations
    leftHandSides = []
    rightHandSides = []

    # we split the entire equation based on the "=" sign into lefths and righths

    for eq in equations:
        a = eq.split("=")
        leftHandSides.append(a[0])
        rightHandSides.append(a[1])

    #eliminate white space from the strings representing the free terms
    for i in range(0,len(rightHandSides)):
        rightHandSides[i] = rightHandSides[i].strip(" ")

    #in the Lhs we split the coefficients from the variables
    for i in range(0, len(leftHandSides)):
        leftHandSides[i] = leftHandSides[i].replace("*", " ").split(" ")
        del leftHandSides[i][-1] #eleminates white space char from the list of strings

    #we extract each coeffiecient of the variables, we convert it to float and add it to the
    #matrix
    coeff = []
    coefficients = []
    for i in range(0, len(leftHandSides)):
        eq = leftHandSides[i]
        coeff = []
        for i in range(0, len(eq), 2):
            singleCoeff = eq[i]
            coeff.append(float(singleCoeff))

        coefficients.append(coeff)


    #get free terms
    freeTerms = []
    for i in range(0,len(rightHandSides)):
        freeTerms.append(float(rightHandSides[i]))

    return coefficients,freeTerms

equations = getFileContent("sistem.txt")

coefficients, freeTerms = getCoefficientsAndFreeTerms(equations)

population_size = 8
no_of_variables = len(coefficients[0])




'''

- calcFitness calculates the fitness of a solution
- we compute the lefthandside of the equation by adding together (solution*coefficient)
- then we substract from this the free term fi = lhsEvaluation - freeTerm
- we add the abs(fi) to F, which has to be as small as possible for the approximation to be close
to the real value of the solution
- the resulting value is the fitness value of the solutions set

'''

def calcFitnessAbsValue(coefficients,freeTerms,variables):

    F = 0.0
    iterator = 0
    for coeffList in coefficients:

        lhsEvaluation = 0.0
        for i in range(0,len(coeffList)):
            lhsEvaluation = lhsEvaluation +(coeffList[i] * variables[i])


        freeTerm = freeTerms[iterator]
        iterator += 1

        fi = lhsEvaluation - freeTerm

        F = F + abs(fi)


    return F


def calcFitnessSquare(coefficients,freeTerms,variables):

    F = 0.0
    iterator = 0
    for coeffList in coefficients:

        lhsEvaluation = 0.0
        for i in range(0,len(coeffList)):
            lhsEvaluation = lhsEvaluation +(coeffList[i] * variables[i])


        freeTerm = freeTerms[iterator]
        iterator += 1

        fi = lhsEvaluation - freeTerm

        F = F + pow(fi,2)

    return float(truncate(F,3))



'''Truncates/pads a float f to n decimal places without rounding'''

def truncate(f, n):

    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])





'''

- initializePopulation generates the first population of solutions
- popoulation_size = the number of potential solutions in the population
- no_of_variables = number of unknowns matched to the coefficients

'''

def initializePopulation( population_size , no_of_variables ):

    population = []
    for i in range(0,population_size):

        solution = np.random.uniform(-20,20,no_of_variables)

        for j in range(0,len(solution)):
            solution[j] = solution[j]

        population.append(list(solution))

    return population



'''
Computes the distance between two points in the Euclidean Space
'''
def euclideanDistance(x1,y1,x2,y2):

    dist = ((x1-x2)**2 + (y1-y2)**2)**.5
    return dist



'''
Weighted distance used in the mating selection process
DW(p)
'''

def DW(pop, index, fitList1, fitList2):

    k = len(pop)
    p_x = fitList1[index]
    p_y = fitList2[index]

    dis_sum = 0
    for i in range(0,k):
        if i == index:
            continue
        else:
            x2 = fitList1[i]
            y2 = fitList2[i]
            dist = euclideanDistance(p_x,p_y,x2,y2)
            dis_sum += dist

    r_sum = 0
    for i in range(0,k):
        if i == index:
            continue
        else:
            x2 = fitList1[i]
            y2 = fitList2[i]
            dist = euclideanDistance(p_x,p_y,x2,y2)
            r_sum += 1/abs(dist-(dis_sum/k))

    dw_sum = 0
    for i in  range(0,k):
        if i == index:
            continue
        else:
            x2 = fitList1[i]
            y2 = fitList2[i]
            dist = euclideanDistance(p_x,p_y,x2,y2)
            dw_sum += ((1/abs(dist-(dis_sum/k)))/r_sum)*dist

    return dw_sum





''' 

-mating_selection using tournament criterion and knee point selection

'''

def mating_selection(population, set_of_KneePoints, pop_size, fitnessListAbs, fitnessListSquare):
    Q = []

    while len(Q) < pop_size:
        i = np.random.randint(0,pop_size)
        j = np.random.randint(0,pop_size)

        a = population[i]
        b = population[j]

        a_fitness = fitnessListAbs[i]
        b_fitness = fitnessListAbs[j]

        if a_fitness < b_fitness:
            Q.append(a)
        elif b_fitness < a_fitness:
            Q.append(b)
        else:
            if a in set_of_KneePoints and b not in set_of_KneePoints:
                Q.append(a)
            elif b in set_of_KneePoints and a not in set_of_KneePoints:
                Q.append(b)
            else:
                if DW(population,i,fitnessListAbs,fitnessListSquare) > DW(population,j,fitnessListAbs,fitnessListSquare):
                    Q.append(a)
                elif DW(population,j,fitnessListAbs,fitnessListSquare) > DW(population,i,fitnessListAbs,fitnessListSquare):
                    Q.append(b)
                else:
                    if np.random.rand(0,1) < 0.5:
                        Q.append(a)
                    else:
                        Q.append(b)

    return Q





'''
Non dominated sort
Sorts the population based on the dominantion criteria
(if we have solutions 'a' and 'b' and the fitness of solution 'a' < fitness of sol 'b', then
a dominates b)
'''

def non_dominated_sort(population, fitnessList):
    fitList = []
    for i in range(0,len(fitnessList)):
        fitList.append(fitnessList[i])

    fitList.sort()

    sortedPopulation = []
    for i in range(0,len(population)):
        for j in range(0,len(fitList)):
            if fitList[i] == fitnessList[j]:
                sortedPopulation.append(population[j])

    return sortedPopulation







'''
Computes the distance from point C(x3,y3) to the line determined by points A(x1,y1) and B(x2,y2)
'''

def distanceToLine(x1,y1,x2,y2,x3,y3):
    d = np.abs((x3-x2)*(y2-y1) - (x2-x1)*(y3-y2)) / np.sqrt(np.square(x3-x2) + np.square(y3-y2))
    return d






'''
Find best solution from current population
'''

def find_best_solution(population):
    fitnessList = []
    for pop in population:
        fitnessList.append(calcFitnessAbsValue(coefficients, freeTerms, pop))

    bestFit = min(fitnessList)

    for i in range(0,len(fitnessList)):
        if fitnessList[i] == bestFit:
            bestSol = population[i]

    return bestSol
'''

Finding_knee_points
Finds the knee points of the population and returns a set containing them

'''





'''
-Compute the probability that each solution will be selected for the next generation
based on the fitness value

-by generating random values between 0 and 1, and taking into account the values of the cumulative
probabilites we select the best solutions for the next generation
'''

def roulette_wheel_selection(fitnessList,next_generation):

    Fitness = []
    Total = 0.0

    for i in range(0,len(fitnessList)):
        val = 1/(1+fitnessList[i])
        Fitness.append(float(val))
        Total = Total + float(val)


    Prob = [] # probability values of the solutions
    s = 0

    for i in range(0,len(Fitness)):
        val = float(Fitness[i]/Total)  # the probability of the solution i based on its fitness score
        Prob.append(val)
        s = s+ (val)


    C = [] #cumulative probabilities values

    for i in range(0,len(Prob)):
        sum = 0
        for j in range(0,i+1):
            sum = sum + Prob[j]
        C.append(sum)


    selected_chromosomes = [] #list containing the selected solutions for next gen

    for i in range(0, len(next_generation)):

        RandNR = random.random() #generate random nr between 0 -> 1

        if RandNR < C[0]:
            selected_chromosomes.append(next_generation[0]) #if the random nr is smaller than the
                                                            # probability of first solution, then
                                                            # we add this to the selected chromosomes
        else:
            for j in range(0, len(C) - 1):
                if RandNR >= C[j] and RandNR < C[j + 1]:
                    selected_chromosomes.append(next_generation[j + 1])
                    # based on the random nr we find the solution whose cumulative prob interval
                    # contains this random number and we add it to the selected_chromosomes list


    return selected_chromosomes







''' 
Crossover function
'''

def crossover(selected_chromosomes, crossover_rate):
    selected_for_crossover = []

    for i in range(0, len(selected_chromosomes)):
        RandNR = random.random()
        if RandNR <= crossover_rate:
            selected_for_crossover.append(selected_chromosomes[i])



    new_solutions = []
    for i in range(0, len(selected_for_crossover)):
        crossover_point = random.randrange(1, no_of_variables)

        s1 = selected_for_crossover[i]
        s2 = selected_for_crossover[len(selected_for_crossover) - i - 1]

        new_sol = []
        for i in range(0, crossover_point):
            new_sol.append(s1[i])

        for i in range(crossover_point, no_of_variables):
            new_sol.append(s2[i])

        new_solutions.append(new_sol)


    fitness_selected_chromosomes = []
    for sol in selected_chromosomes:
        fitness_selected_chromosomes.append(calcFitnessAbsValue(coefficients, freeTerms, sol))


    j = 0
    for i in range(len(selected_chromosomes) - len(selected_for_crossover), len(selected_chromosomes)):
        selected_chromosomes[i] = new_solutions[j]
        j = j + 1

    return selected_chromosomes






'''
Mutation function
'''

def mutate(population_after_crossover, mutation_rate):
    total_gen = population_size * no_of_variables
    nr_of_chromosomes_mutated = round(mutation_rate * total_gen)
    # print(nr_of_chromosomes_mutated)

    # print("_________________________________________________")

    # print(selected_chromosomes)
    for i in range(0, nr_of_chromosomes_mutated):
        # print("i ",i)
        RandNR = random.randrange(0, len(population_after_crossover))
        # print(RandNR)
        population_after_crossover[RandNR][1] = random.uniform(-10, 10)
        # solution_to_be_mutated = selected_chromosomes[RandNR]

        # selected_chromosomes[RandNR] = mutateSol(solution_to_be_mutated)


    return population_after_crossover






'''
Function to improve the fitness of a solution by adding/substracting some value < 1.0
'''

def imporve_solution(sol):
    fitness = calcFitnessAbsValue(coefficients,freeTerms,sol)

    new_sol = []
    for i in range(0,len(coefficients)):

        new_sol.append(sol[i])

    for i in range(0,len(coefficients)):
        auxSolution = []
        for j in range(0, len(coefficients)):
            auxSolution.append(sol[j])

        auxSolution[i] = auxSolution[i] + 0.001
        tempFitness = calcFitnessAbsValue(coefficients,freeTerms,auxSolution)

        if tempFitness < fitness:
            new_sol[i] = auxSolution[i]
        else:
            auxSolution[i] = auxSolution[i] - 0.002
            tempFitness = calcFitnessAbsValue(coefficients,freeTerms,auxSolution)

            if tempFitness < fitness:
                new_sol[i] = auxSolution[i]

    for i in range(0,len(new_sol)):
        sol[i] = new_sol[i]
    newFit = calcFitnessAbsValue(coefficients,freeTerms,sol)
    #if newFit < fitness:
    #    print("OK")
    #print("{0} --> {1}".format(fitness,newFit))