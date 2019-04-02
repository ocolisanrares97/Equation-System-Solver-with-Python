from helperFunctions import *
import matplotlib.pyplot as plt



equations = getFileContent("sistem.txt")

coefficients, freeTerms = getCoefficientsAndFreeTerms(equations)

population_size = 2500
crossover_rate = 0.50 #25% chance to use current member for crossover
mutation_rate = 0.2 #10% chance to mutate
no_of_variables = len(coefficients[0])

population = initializePopulation(population_size , no_of_variables)

# sol = [1,2,3]
#
#
# for i in range(0,10000):
#     imporve_solution(sol)
#     print(sol)
# print(sol)
next_generation = population


bestFit = 1000
while bestFit > 0.05:

    previous_generation = next_generation.copy()

    ''' compute the fitness value for each solution '''
    fitnessList = []
    for pop in next_generation:
        fitnessList.append(calcFitnessAbsValue(coefficients, freeTerms, pop))

    fitList2 = []
    for pop in next_generation:
        fitList2.append(calcFitnessSquare(coefficients,freeTerms,pop))

    #K =[]
    #selected_chromosomes = mating_selection(population,K,population_size,fitnessList,fitList2)
    ''' select the best solutions for the next generation '''
    selected_chromosomes = roulette_wheel_selection(fitnessList, next_generation)


    ''' apply the crossover on the selected chromosomes '''
    population_after_crossover = crossover(selected_chromosomes,crossover_rate)



    ''' mutate the population after crossover '''
    next_generation = mutate(population_after_crossover, mutation_rate)


    # fit_Previous_gen = []
    # for sol in previous_generation:
    #     fit_Previous_gen.append(calcFitnessAbsValue(coefficients,freeTerms,sol))

    fit_Next_gen = []
    for sol in next_generation:
        fit_Next_gen.append(calcFitnessAbsValue(coefficients,freeTerms,sol))


    # best_sol_previous = find_best_solution(previous_generation)
    best_sol_next = find_best_solution(next_generation)

    for i in range(0,10000):
        imporve_solution(best_sol_next)

    # bestFitPrev = min(fit_Previous_gen)

    # bestFitNew = min(fit_Next_gen)
    # bestFit = bestFitNew
    # if bestFitPrev < bestFitNew:
    #     next_generation = previous_generation.copy()
    #     bestFit = bestFitPrev

    bestFit = min(fit_Next_gen)
    print(bestFit)
    #print(find_best_solution(next_generation))

sol = find_best_solution(next_generation)
print(sol)

# K = []
# Q = mating_selection(population,K,population_size,fitList1,fitList2)
#
# print(Q)

