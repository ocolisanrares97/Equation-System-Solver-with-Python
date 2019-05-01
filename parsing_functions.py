
''' PARSING STAGE '''
#function that returns a list of strings, each one representing an equation
#read contents of the file

def getFileContent(filename):
    # equations[] will contatin the raw equations from the file as strings
    equations = []

    try:
        with open(filename) as file:
            equations = file.readlines()
    except OSError:
         print("Invalid filename/file does not exist")

    # remove \n from the strings
    equations = [x.strip() for x in equations]
    return equations

'''

getCoefficients extracts the coefficients, free terms and variables from the strings
representing the equations

 '''

def getCoefficientsAndFreeTerms(equations):
    try:
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
    except OSError:
        print("Cannot divide lists because of the invalid equations format")

    return coefficients,freeTerms

