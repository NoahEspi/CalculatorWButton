import tkinter as tk;
import math; from math import sqrt

# off, ans, ac, sqrt

# window configuration
window = tk.Tk();

window.columnconfigure(0, weight=1, minsize=50)
window.rowconfigure(0, weight=1, minsize=50)

window.title("Calcutator Fo Real")

prevAns = "";

# frame configurations
screenFrame = tk.Frame(window, relief=tk.RAISED, borderwidth = 1)

numberFrame = tk.Frame(window)


equation = [];

# numbers
def numZero():
  equation.append('0');
  screenDisplay.configure(text=equation);

def numOne():
  equation.append('1');
  screenDisplay.configure(text=equation);

def numTwo():
  equation.append('2');
  screenDisplay.configure(text=equation);

def numThree():
  equation.append('3');
  screenDisplay.configure(text=equation);

def numFour():
  equation.append('4');
  screenDisplay.configure(text=equation);

def numFive():
  equation.append('5');
  screenDisplay.configure(text=equation);

def numSix():
  equation.append('6');
  screenDisplay.configure(text=equation);

def numSeven():
  equation.append('7');
  screenDisplay.configure(text=equation);

def numEight():
  equation.append('8');
  screenDisplay.configure(text=equation);

def numNine():
  equation.append('9');
  screenDisplay.configure(text=equation);

def decimal():
  equation.append('.');
  screenDisplay.configure(text=equation);


# operations
def addSign():
  equation.append('+');
  screenDisplay.configure(text=equation);

def minusSign():
  equation.append('-');
  screenDisplay.configure(text=equation);

def multSign():
  equation.append('*');
  screenDisplay.configure(text=equation);

def divSign():
  equation.append('/');
  screenDisplay.configure(text=equation);

def equalSign():
  global equation
  global prevAns

  if equation != []:
    try:
      combEquation = ''.join(equation);
      combEquation = eval(combEquation);

      screenDisplay.configure(text=combEquation);
      equation = combEquation;
      prevAns = combEquation;
    except SyntaxError:
      equation.clear();
      screenDisplay.configure(text="ERROR: SYNTAX")

def percentButton():
  global equation
  global prevAns

  if equation != []:
    try:
      combEquation = ''.join(equation);
      combEquation = eval(combEquation);

      combEquation = combEquation/100;

      combEquation = str(combEquation);

      screenDisplay.configure(text=combEquation);
      equation = combEquation;
      prevAns = combEquation;
    except SyntaxError:
      equation.clear();
      screenDisplay.configure(text="ERROR: SYNTAX")

def offButton():
  window.destroy();

def squareRoot():
  global equation
  if equation != []:
    try:
      global prevAns
      combEquation = ''.join(equation);
      combEquation = eval(combEquation);

      combEquation = sqrt(combEquation);

      combEquation = str(combEquation);

      screenDisplay.configure(text=combEquation);
      equation = combEquation;
      prevAns = combEquation;
    except SyntaxError:
      equation.clear();
      screenDisplay.configure(text="ERROR: SYNTAX")

def clearDisplay():
  global equation 

  equation = list(str(equation));
  equation.clear();
  screenDisplay.configure(text=equation);
  

# configures number display
screenDisplay = tk.Label(master=screenFrame, text=equation, anchor="e", fg="white", bg="black", width=25)

screenDisplay.grid(row=0, column=1)


# number buttons
button0 = tk.Button(master=numberFrame, text = "0", width = 3, height = 1, command = numZero);
button1 = tk.Button(master=numberFrame, text = "1", width = 3, height = 1, command = numOne);
button2 = tk.Button(master=numberFrame, text = "2", width = 3, height = 1, command = numTwo);
button3 = tk.Button(master=numberFrame, text = "3", width = 3, height = 1, command = numThree);
button4 = tk.Button(master=numberFrame, text = "4", width = 3, height = 1, command = numFour);
button5 = tk.Button(master=numberFrame, text = "5", width = 3, height = 1, command = numFive);
button6 = tk.Button(master=numberFrame, text = "6", width = 3, height = 1, command = numSix);
button7 = tk.Button(master=numberFrame, text = "7", width = 3, height = 1, command = numSeven);
button8 = tk.Button(master=numberFrame, text = "8", width = 3, height = 1, command = numEight);
button9 = tk.Button(master=numberFrame, text = "9", width = 3, height = 1, command = numNine);
buttonDecimal = tk.Button(master=numberFrame, text = ".", width = 3, height = 1, command = decimal)


# operation buttons
buttonAdd = tk.Button(master=numberFrame, text = "+", width = 3, height = 1, command = addSign);
buttonEqual = tk.Button(master=numberFrame, text = "=", width = 3, height = 1, command = equalSign)
buttonMinus = tk.Button(master=numberFrame, text = "-", width = 3, height = 1, command = minusSign)
buttonMult = tk.Button(master=numberFrame, text = "×", width = 3, height = 1, command = multSign)
buttonDiv = tk.Button(master=numberFrame, text = "÷", width = 3, height = 1, command = divSign)
buttonPerc = tk.Button(master=numberFrame, text = "%", width = 3, height = 1, command = percentButton)
buttonOff = tk.Button(master=numberFrame, text = "off", width = 3, height = 1, command = offButton)
buttonSqrt = tk.Button(master=numberFrame, text = "√", width = 3, height = 1, command = squareRoot);
buttonClear = tk.Button(master=numberFrame, text = "AC", width = 3, height = 1, command = clearDisplay);


# number button placements
button1.grid(row=3, column=0, padx=(10,0), pady=(0,10));
button2.grid(row=3, column=1, pady=(0,10));
button3.grid(row=3, column=2, padx=(0,28), pady=(0,10));
button4.grid(row=2, column=0, padx=(10,0), pady=(0,10));
button5.grid(row=2, column=1, pady=(0,10));
button6.grid(row=2, column=2, padx=(0,28), pady=(0,10));
button7.grid(row=1, column=0, padx=(10,0), pady=(0,10));
button8.grid(row=1, column=1, pady=(0,10));
button9.grid(row=1, column=2, padx=(0,28), pady=(0,10));
button0.grid(row=4, column=0, padx=(10,0), pady=(0,10));
buttonDecimal.grid(row=4, column=1, pady=(0,10));


# operation button placements
buttonAdd.grid(row=1, column=3, padx=(0,10), pady=(0,10));
buttonEqual.grid(row=4, column=2, padx=(0,28), pady=(0,10));
buttonMinus.grid(row=2, column=3, padx=(0,10), pady=(0,10));
buttonMult.grid(row=3,column=3, padx=(0,10), pady=(0,10));
buttonDiv.grid(row=4,column=3, padx=(0,10), pady=(0,10));
buttonPerc.grid(row=0, column=2, padx=(0,28), pady=(0,10));
buttonOff.grid(row=0, column=0, padx=(10,0), pady=(0,10));
buttonSqrt.grid(row=0, column=1, pady=(0,10));
buttonClear.grid(row=0, column=3, padx=(0,10), pady=(0,10));


screenFrame.grid(row=0)
numberFrame.grid(row=1)


window.mainloop();