from main import *
from tkinter import *
import threading
dead = False


thread = threading.Thread()
#____BUTTON COMMANDS________


def startComputation():


    str = ""
    filename = inputTextField.get("1.0", END)
    str = filename.strip()

#If the "Use default values" box is checked we set the default parameters values
    if(checkBoxValue.get() == 1):
        try:

            if(radioButtuonValue.get() == 1):

                final_solution, fit, execTime = bootBasic(str, 1000, 0.5, 0.2, 0.4, 0.003)

            elif(radioButtuonValue.get() == 2):

                final_solution, fit, execTime = bootImproved(str, 1000, 0.5, 0.2, 0.4, 0.003)

            else:
                resultsTextField.delete("1.0", END)
                resultsTextField.insert(END, "Please select which algorithm you wish to use.")
                return

            crossoverRateTextField.delete("1.0", END)
            crossoverRateTextField.insert(END, 0.5)

            mutationRateTextField.delete("1.0", END)
            mutationRateTextField.insert(END, 0.2)

            fitnessTextField.delete("1.0", END)
            fitnessTextField.insert(END, 0.1)

            populationSizeTextField.delete("1.0", END)
            populationSizeTextField.insert(END, 1000)

            precisionTextField.delete("1.0", END)
            precisionTextField.insert(END, 0.003)

            sol = "x"
            egal = " = "
            backs = "\n"

            resultsTextField.delete("1.0", END)
            resultsTextField.insert(END, "Fitness values of the solution is: ")
            resultsTextField.insert(END, fit)
            resultsTextField.insert(END, backs)
            for i in range(0, len(final_solution)):
                resultsTextField.insert(END, sol)
                resultsTextField.insert(END, i + 1)
                resultsTextField.insert(END, egal)
                resultsTextField.insert(END, final_solution[i])
                resultsTextField.insert(END, backs)

            resultsTextField.insert(END, "Execution time: ")
            resultsTextField.insert(END, execTime)
            del final_solution[:]
        except:
            resultsTextField.delete("1.0", END)
            resultsTextField.insert(END, "Error. Something went wrong when proccesing the solution"
                                         "  \nMake sure that you have succesfully read the file."
                                         "\nCheck if you have filled the paramaters fields")

#If the "Use default parameters" is not checked we take the values from the parameters fields
    else:
        try:
            crossRate = float(crossoverRateTextField.get("1.0", END))


            mutationRate = float(mutationRateTextField.get("1.0", END))

            fitness = float(fitnessTextField.get("1.0", END))

            popSize = int(populationSizeTextField.get("1.0", END))

            precision = float(precisionTextField.get("1.0", END))

        except:
            resultsTextField.delete("1.0", END)
            resultsTextField.insert(END, "Please make sure that you completed the parameter fields.")
            return



        try:

            if(radioButtuonValue.get() == 1):

                final_solution,fit, execTime = bootBasic(str,popSize,crossRate,mutationRate,fitness,precision)

            elif (radioButtuonValue.get() == 2):

                final_solution, fit, execTime = bootImproved(str,popSize,crossRate,mutationRate,fitness,precision)

            else:
                resultsTextField.delete("1.0", END)
                resultsTextField.insert(END, "Please select which algorithm you wish to use.")
                return

            resultsTextField.delete("1.0",END)
            sol = "x"
            egal = " = "
            backs = "\n"

            resultsTextField.delete("1.0", END)
            resultsTextField.insert(END, "Fitness values of the solution is: ")
            resultsTextField.insert(END, fit)
            resultsTextField.insert(END, backs)
            for i in range(0,len(final_solution)):

                resultsTextField.insert(END, sol)
                resultsTextField.insert(END,i+1)
                resultsTextField.insert(END, egal)
                resultsTextField.insert(END, final_solution[i])
                resultsTextField.insert(END, backs)

            resultsTextField.insert(END, "Execution time: ")
            resultsTextField.insert(END, execTime)

            del final_solution[:]
        except:
            resultsTextField.delete("1.0",END)
            resultsTextField.insert(END,"Error. Something went wrong when proccesing the solution"
                                        "  \nMake sure that you have succesfully read the file."
                                        "\nCheck if you have filled the paramaters fields")


def displaySystem():
    str = ""
    filename = inputTextField.get("1.0", END)
    str = filename.strip()

    fileContent = []

    try:
        with open(str) as f:
            fileContent = f.readlines()

        showSystemTextField.delete("1.0", END)
        for i in fileContent:

            showSystemTextField.insert(END,i)
    except(OSError):
        showSystemTextField.delete("1.0", END)
        showSystemTextField.insert("1.0","Invalid filename/file does not exist")



#++++++++++++++++++++++++++++   GUI LAYOUT   +++++++++++++++++++++++++++

top = Tk()
top.title("Equations System Solver")
top.geometry("1600x500")

checkBoxValue = IntVar()
radioButtuonValue = IntVar()

#++++++++++++   WIDGETS   +++++

#___LABLES__
entryLable = Label(top,text="File name:")

S = Scrollbar(top)

#____TEXT FIELDS____
inputTextField = Text(top, height=1, bd=3,width=60)
resultsTextField = Text(top, height=20,bd=3, width=60)
showSystemTextField = Text(top,height=20,bd=3,width =60)



#____ENTRIES_____
crossoverRateTextField = Text(top,bd = 2,width=10 ,height = 1)
mutationRateTextField = Text(top,bd = 2,width=10,height = 1)
precisionTextField = Text(top,bd = 2,width=10,height = 1)
populationSizeTextField = Text(top, bd = 2,width=10,height = 1)
fitnessTextField = Text(top,bd = 2,width=10,height = 1)

#_____BUTTONS____
readFileButton = Button(top, text="Read File", command= displaySystem)
startButton = Button(top, text ="Find Solutions", command = startComputation)
#stopButton = Button(top,text = "Stop",width=10)
defaultValuesCheckbox = Checkbutton(top, text ="Use default parameter values", variable = checkBoxValue,height = 4)
normalGA_RadioButton = Radiobutton(top,text = "Use Basic Genetic Algorithm", value=1, variable = radioButtuonValue)
improvedGA_RadioButton = Radiobutton(top,text = "Use Improved Genetic Algorithm", value=2, variable = radioButtuonValue)

#-------------LAYOUT------------
entryLable.grid(row=0,column=2, sticky=W,pady=10,padx = 5)
inputTextField.grid(row=0,column=3)
readFileButton.grid(row=0,column=4,sticky=W)

Label(top,text="Population Size:").grid(row=1,sticky=E,pady=5,padx = 5)
populationSizeTextField.grid(row=1,column =1)

Label(top,text="Fitness treshold:").grid(row=2,sticky=E,pady=5,padx = 5)
fitnessTextField.grid(row=2,column =1)

Label(top,text="Crossover Rate:").grid(row=3,sticky=E,pady=5,padx = 5)
crossoverRateTextField.grid(row=3,column =1)

Label(top,text="Mutation Rate:").grid(row=4,sticky=E,pady=5,padx = 5)
mutationRateTextField.grid(row=4,column =1)

Label(top,text="Precision:").grid(row=5,sticky=E,pady=5,padx = 10)
precisionTextField.grid(row=5,column =1)

showSystemTextField.grid(row=1,column=3,rowspan=4)
Label(top,text="System of equations to be solved").grid(row=5,column=3,pady=5)
startButton.grid(row=2,column = 4,padx = 20)

resultsTextField.grid(row=1,column = 5, rowspan=4)
Label(top,text="Solutions").grid(row=5,column=5,pady=5)

defaultValuesCheckbox.grid(row=6,column=1,pady=10)

normalGA_RadioButton.grid(row=6, column = 3, sticky=E)
improvedGA_RadioButton.grid(row=6, column = 5, sticky =W)

#stopButton.grid(row=3,column=4,padx=20)

top.mainloop()
