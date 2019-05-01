from main import *
from tkinter import *



top = Tk()
top.title("Equations System Solver")
top.geometry("1200x500")

S = Scrollbar(top)
inputTextField = Text(top, height=4, width=50)
resultsTextField = Text(top, height=4, width=60)

S.pack(side=RIGHT, fill=Y)
inputTextField.pack(padx = 10,pady = 10, side=LEFT, fill=Y)


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

B = Button(top, text ="Find Solutions", command = startComputation)

B.pack(padx = 10,pady = 10, side = LEFT)

resultsTextField.pack(padx = 10,pady = 10, side=LEFT, fill=Y)

S.config(command=inputTextField.yview)
inputTextField.config(yscrollcommand=S.set)




top.mainloop()
