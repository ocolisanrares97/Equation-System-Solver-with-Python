from helperFunctions import *
import matplotlib.pyplot as plt
from generator import *



def boot(filename,pop_size,crossRate,mutationRate,fitTreshold,prec):

    equations = getFileContent(filename)
    coefficients, freeTerms = getCoefficientsAndFreeTerms(equations)

    population_size = pop_size #1000
    crossover_rate =  crossRate  #0.50 #25% chance to use current member for crossover
    mutation_rate =   mutationRate#0.2 #10% chance to mutate
    no_of_variables = len(coefficients[0])

    population = initializePopulation(population_size , no_of_variables)

    next_generation = population
    #
    # gen = Generator()
    # gen.print_sistem()
    bestFit = 3000
    while bestFit > fitTreshold:

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
        population_after_crossover = crossover(selected_chromosomes,crossover_rate,no_of_variables,coefficients,freeTerms)



        ''' mutate the population after crossover '''
        next_generation = mutate(population_after_crossover, mutation_rate,population_size,no_of_variables)



        fit_Previous_gen = []
        for sol in previous_generation:
            fit_Previous_gen.append(calcFitnessAbsValue(coefficients, freeTerms, sol))

        fit_Next_gen = []
        for sol in next_generation:
            fit_Next_gen.append(calcFitnessAbsValue(coefficients, freeTerms, sol))

        # best_sol_previous = find_best_solution(previous_generation)
        # best_sol_next = find_best_solution(next_generation)

        bestFitPrev = min(fit_Previous_gen)
        bestFitNew = min(fit_Next_gen)

        bestFit = bestFitNew
        if bestFitPrev < bestFitNew:
            for i in range(0,len(next_generation)):
                next_generation[i] = previous_generation[i]
            bestFit = bestFitPrev

        best_sol = find_best_solution(next_generation, coefficients,freeTerms)
        for i in range(0,2000):
            imporve_solution(best_sol,coefficients,freeTerms,prec)
        final_bestFitness = bestFit
        print(bestFit)
        #print(find_best_solution(next_generation))

    sol = find_best_solution(next_generation, coefficients, freeTerms)
    print(sol)
    final_solution = []
    for i in range(0,len(sol)):
        final_solution.append(sol[i])

    return final_solution, final_bestFitness




