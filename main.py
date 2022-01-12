import tkinter as tk;
import math; from math import sin, cos, tan
import time
import warnings
import re

warnings.filterwarnings('ignore')

# window configuration
window = tk.Tk();

window.columnconfigure(0, weight=1, minsize=50)
window.rowconfigure(0, weight=1, minsize=50)

window.title("Calcutator Fo Real")



# frame configurations
screenFrame = tk.Frame(window, borderwidth = 1)

numberFrame = tk.Frame(window)


# establishes variables
equation = [];
prevAns = "";



# configures number display
screenDisplay = tk.Label(master=screenFrame, text=equation, relief = tk.SUNKEN, borderwidth=4, anchor="e", fg="black", bg="#B9FFEE", width=22)

screenDisplay.grid(row=0, column=1)



# creates number functions
def btn0():
  equation.append('0');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn1():
  equation.append('1');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn2():
  equation.append('2');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn3():
  equation.append('3');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn4():
  equation.append('4');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn5():
  equation.append('5');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn6():
  equation.append('6');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn7():
  equation.append('7');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn8():
  equation.append('8');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def btn9():
  equation.append('9');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def doubleZero():
  equation.append("00");
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def decimal():
  equation.append('.');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");



# creates operator functions
def addSign():
  equation.append('+');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def minusSign():
  equation.append('-');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def multSign():
  equation.append('*');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def divSign():
  equation.append('/');
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def leftParen():
  equation.append("(");
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def rightParen():
  equation.append(")");
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def sine():
  equation.append("sin(");
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def cosine():
  equation.append("cos(");
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def tangent():
  equation.append("tan(");
  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");


# calculation functions

# calculates exisitng equation. if it can't, returns error
def equalSign():
  global equation
  global prevAns

  # checks if equation is empty
  if equation != []:
    
    leftPCount = str(equation).count("(")
    rightPCount = str(equation).count(")")
    
    if leftPCount > rightPCount:
      equation.append(")")

    try:

      combEquation = ''.join(equation);

      if "cos(" in combEquation:
        
        cosCount = equation.count("cos(");
        
        print(cosCount);
        
        for i in range(cosCount):
          cosLoc = equation.index("cos(");

          equation = ''.join(equation)

          equation = equation[0:cosLoc] + "cos(math.degrees(" + equation[cosLoc+4] + ")" + equation[cosLoc+5:];

          combEquation = ''.join(equation);

          combEquation = eval(str(combEquation));

      combEquation = ''.join(equation)

      if "sin(" in combEquation:

        sinLoc = equation.index("sin(");

        equation = ''.join(equation)

        equation = equation[0:sinLoc] + "sin(math.degrees(" + equation[sinLoc+4] + ")" + equation[sinLoc+5:];


        combEquation = ''.join(equation);

        combEquation = eval(str(combEquation))

      combEquation = ''.join(equation)

      if "tan(" in combEquation:

        tanLoc = equation.index("tan(");

        equation = ''.join(equation)

        equation = equation[0:tanLoc] + "tan(math.degrees(" + equation[tanLoc+4] + ")" + equation[tanLoc+5:];


        combEquation = ''.join(equation);

        combEquation = eval(str(combEquation));


      if not "tan(" in equation or not "sin(" in equation or not "cos(" in equation:
        combEquation = eval(re.sub(r"((?<=^)|(?<=[^\.\d]))0+(\d+)", r"\1\2", str(combEquation)));

      screenDisplay.configure(text=str(combEquation));
      equation = list(equation)
      equation.clear()
      prevAns = str(combEquation);

    except Exception:
      equation = list(equation)
      equation.clear();
      screenDisplay.configure(text="ERROR: SYNTAX")


# same function as equalSign except divides the answer by 100
def percentButton():
  global equation
  global prevAns
  
  if equation != []:

    try:
      combEquation = ''.join(equation);
      combEquation = eval(re.sub(r"((?<=^)|(?<=[^\.\d]))0+(\d+)", r"\1\2", str(combEquation)));

      combEquation = combEquation/100;

      combEquation = str(combEquation);

      screenDisplay.configure(text=combEquation);
      equation.clear()
      prevAns = str(combEquation);
    except Exception:
      equation.clear();
      screenDisplay.configure(text="ERROR: SYNTAX")


# same function as equalSign but square roots the final answer
def squareRoot():
  global equation
  global prevAns

  if equation != []:
    try:
      combEquation = ''.join(equation);
      combEquation = eval(re.sub(r"((?<=^)|(?<=[^\.\d]))0+(\d+)", r"\1\2", str(combEquation)));

      combEquation = math.sqrt(combEquation);

      combEquation = str(combEquation);

      screenDisplay.configure(text=combEquation);
      equation.clear();
      prevAns = str(combEquation);
    except Exception:
      equation.clear();
      screenDisplay.configure(text="ERROR: SYNTAX");


# establishes off button
def offButton():
  global prevAns
  global buttonNames

  # checks state of button
  if buttonOff.cget("text") == "OFF":

    # changes button states
    for b in buttonNames:
      b.configure(state="disabled");
    
    # changes state (word) of power button
    buttonOff.configure(text="ON")
    
    # changes state of clear button
    buttonClear.configure(text="AC")

    # turns screen "off" and clears previous display
    equation.clear()
    prevAns = "";
    screenDisplay.configure(text=equation, bg="black")

  # checks state of button
  elif buttonOff.cget("text") == "ON":

    # changes button states
    for b in buttonNames:
      b.configure(state="normal")

    # changes state (word) of power button
    buttonOff.configure(text="OFF")

    # turns screen "on"
    screenDisplay.configure(bg="#B9FFEE")



# extra functions

# finds and displays answer to previous equation
def answer():
  global prevAns

  if prevAns != "":
    equation.append(prevAns);
    screenDisplay.configure(text=''.join(equation));
    buttonClear.configure(text="C");

def backspace():
  global equation

  try:

    # combines equation into a string and puts each individual char into a list
    equation = ''.join(equation)
    equation = list(equation)

    # removes last char of equation
    equation.pop();


    screenDisplay.configure(text=''.join(equation));

  except IndexError:
    pass
  

# clears the existing display
def clearDisplay():
  global equation
  global prevAns

  if buttonClear.cget("text") == "C":
    buttonClear.configure(text="AC")
    equation.clear();
    screenDisplay.configure(text=''.join(equation));

  elif buttonClear.cget("text") == "AC":
    prevAns = ""
    equation.clear();
    screenDisplay.configure(text=''.join(equation));



# creates number buttons
btn0 = tk.Button(master=numberFrame, text = "0", width = 3, height = 1, command = btn0);
btn1 = tk.Button(master=numberFrame, text = "1", width = 3, height = 1, command = btn1);
btn2 = tk.Button(master=numberFrame, text = "2", width = 3, height = 1, command = btn2);
btn3 = tk.Button(master=numberFrame, text = "3", width = 3, height = 1, command = btn3);
btn4 = tk.Button(master=numberFrame, text = "4", width = 3, height = 1, command = btn4);
btn5 = tk.Button(master=numberFrame, text = "5", width = 3, height = 1, command = btn5);
btn6 = tk.Button(master=numberFrame, text = "6", width = 3, height = 1, command = btn6);
btn7 = tk.Button(master=numberFrame, text = "7", width = 3, height = 1, command = btn7);
btn8 = tk.Button(master=numberFrame, text = "8", width = 3, height = 1, command = btn8);
btn9 = tk.Button(master=numberFrame, text = "9", width = 3, height = 1, command = btn9);
buttonDoubleZero = tk.Button(master = numberFrame, text="00", width = 3, height = 1, command = doubleZero)

buttonDecimal = tk.Button(master=numberFrame, text = ".", width = 3, height = 1, command = decimal)


# creates operator buttons
buttonAdd = tk.Button(master=numberFrame, text = "+", width = 3, height = 1, command = addSign);
buttonEqual = tk.Button(master=numberFrame, text = "=", width = 3, height = 1, command = equalSign)
buttonMinus = tk.Button(master=numberFrame, text = "-", width = 3, height = 1, command = minusSign)
buttonMult = tk.Button(master=numberFrame, text = "×", width = 3, height = 1, command = multSign)
buttonDiv = tk.Button(master=numberFrame, text = "÷", width = 3, height = 1, command = divSign)

buttonPerc = tk.Button(master=numberFrame, text = "%", width = 3, height = 1, command = percentButton)

buttonOff = tk.Button(master=numberFrame, text = "OFF", width = 3, height = 1, bg="red", fg="white", command = offButton)

buttonSqrt = tk.Button(master=numberFrame, text = "√", width = 3, height = 1, command = squareRoot);

buttonClear = tk.Button(master=numberFrame, text = "AC", width = 3, height = 1, command = clearDisplay);

buttonAns = tk.Button(master=numberFrame, text = "ans", width = 3, height = 1, command = answer)

buttonLeftParen = tk.Button(master=numberFrame, text = "(", width = 3, height = 1, command = leftParen)
buttonRightParen = tk.Button(master=numberFrame, text = ")", width = 3, height = 1, command = rightParen);

buttonBack = tk.Button(master=screenFrame, height = 1, width = 1, text="⌫", command=backspace)

btnCos = tk.Button(master=numberFrame, text="cos", width=3, height=1, command=cosine)
btnSin = tk.Button(master=numberFrame, text="sin", width=3, height=1, command=sine)
btnTan = tk.Button(master=numberFrame, text="tan", width=3, height=1, command=tangent)

btnSec = tk.Button(master=numberFrame, text="2nd",width=3, height=1, bg="#0CC717", fg="white")

# places number buttons
btn1.grid(row=5, column=0, padx=(10,0), pady=(0,5));
btn2.grid(row=5, column=1, pady=(0,5));
btn3.grid(row=5, column=2, padx=(0,18), pady=(0,5));
btn4.grid(row=4, column=0, padx=(10,0), pady=(0,5));
btn5.grid(row=4, column=1, pady=(0,5));
btn6.grid(row=4, column=2, padx=(0,18), pady=(0,5));
btn7.grid(row=3, column=0, padx=(10,0), pady=(0,5));
btn8.grid(row=3, column=1, pady=(0,5));
btn9.grid(row=3, column=2, padx=(0,18), pady=(0,5));
btn0.grid(row=6, column=0, padx=(10,0), pady=(0,10));
buttonDoubleZero.grid(row=6, column=1, pady=(0,10));

buttonDecimal.grid(row=6, column=2, padx=(0,18), pady=(0,10));


# places operator buttons
buttonAdd.grid(row=2, column=3, padx=(0,10), pady=(0,5));
buttonEqual.grid(row=6, column=3, padx=(0,10), pady=(0,10));
buttonMinus.grid(row=3, column=3, padx=(0,10), pady=(0,5));
buttonMult.grid(row=4,column=3, padx=(0,10), pady=(0,5));
buttonDiv.grid(row=5, column=3, padx=(0,10), pady=(0,5));

buttonPerc.grid(row=0, column=2, padx=(0,18), pady=(0,5));

buttonOff.grid(row=0, column=0, padx=(10,0), pady=(0,5));

buttonSqrt.grid(row=0, column=1, pady=(0,5));

buttonClear.grid(row=0, column=3, padx=(0,10), pady=(0,5));

buttonLeftParen.grid(row=1, column=1, pady=(0,5));
buttonRightParen.grid(row=1, column=2, padx=(0,18), pady=(0,5));

buttonAns.grid(row=1, column=3, padx=(0,10), pady=(0,5));

buttonBack.grid(row=0, column = 5)

btnSin.grid(row=2, column=0, padx=(10,0), pady=(0,5))
btnCos.grid(row=2, column=1, pady=(0,5))
btnTan.grid(row=2, column=2, pady=(0,5),padx=(0,18))

btnSec.grid(row=1, column=0, padx=(10,0),pady=(0,5))


# frame placements
screenFrame.grid(row=0)
numberFrame.grid(row=1)


# keeps a list of button names
buttonNames = [btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,buttonDecimal,buttonAdd,buttonEqual,buttonMinus,buttonMult,buttonDiv,buttonPerc,buttonSqrt,buttonDoubleZero,buttonLeftParen,buttonRightParen,buttonAns,buttonClear, buttonBack, btnSin, btnCos, btnTan, btnSec]


window.mainloop();

#sin cos tan second function