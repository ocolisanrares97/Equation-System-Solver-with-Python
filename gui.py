from main import *
from tkinter import *


#____BUTTON COMMANDS________
def startComputation():
    str = ""
    filename = inputTextField.get("1.0", END)
    str = filename.strip()


    final_solution,fit = boot(str)

    resultsTextField.delete("1.0",END)
    sol = "x"
    egal = " = "
    backs = "\n"

    resultsTextField.insert(END, "Fitness values of the solution is: ")
    resultsTextField.insert(END, fit)
    resultsTextField.insert(END, backs)
    for i in range(0,len(final_solution)):

        resultsTextField.insert(END, sol)
        resultsTextField.insert(END,i+1)
        resultsTextField.insert(END, egal)
        resultsTextField.insert(END, final_solution[i])
        resultsTextField.insert(END, backs)

    del final_solution[:]

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
top.geometry("1400x500")

#++++++++++++   WIDGETS   +++++

#___LABLES__
entryLable = Label(top,text="File name:")

S = Scrollbar(top)

#____TEXT FIELDS____
inputTextField = Text(top, height=1, bd=3,width=60)
resultsTextField = Text(top, height=20, width=60)
showSystemTextField = Text(top,height=20,width =60)

#____ENTRIES_____
crossoverRateTextField = Entry(top,bd = 2,width=10)
mutationRateTextField = Entry(top,bd = 2,width=10)
precisionTextField = Entry(top, bd = 2,width=10)
populationSizeTextField = Entry(top, bd = 2,width=10)
fitnessTextField = Entry(top, bd = 2,width=10)

#_____BUTTONS____
readFileButton = Button(top, text="Read File", command= displaySystem)
startButton = Button(top, text ="Find Solutions", command = startComputation)



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

# S.config(command=resultsTextField.yview)
# resultsTextField.config(yscrollcommand=S.set)




top.mainloop()
