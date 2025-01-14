import tkinter as tk;
import math; from math import sin, asin, cos, acos, tan, atan, radians as r
import time
import warnings
import re

# When in degrees mode, 'r(' is necessary. Default calculation mode is radians. without the r it calculates in radians, hence why radians doesn't have the 'r('

# you *can* use keyboard numbers instead of clickable buttons for most buttons.
# exceptions include: sqrt, off, Deg, and Rad

# all buttons will be the same as they appear on the calculator except: C/AC is Del and 2nd is the space bar

warnings.filterwarnings('ignore')

# window configuration
window = tk.Tk();

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

window.title("Calcutator Fo Real")



# frame configurations
screenFrame = tk.Frame(window, pady=(5))

numberFrame = tk.Frame(window)



# establishes variables
equation = [];
prevAns = "";


# configures number display
screenDisplay = tk.Label(master=screenFrame, text=equation, relief = tk.SUNKEN, borderwidth=4, anchor="e", fg="black", bg="#B9FFEE", width=20)

screenDisplay.grid(row=0, column=1)

# second button state
secState = False

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
  if buttonMult.cget("text") == '×':
    equation.append('*');
  elif buttonMult.cget("text") == "^":
    equation.append("**")
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
  # checks what the state of btnDegRad is to determine whether to calculate in radians or degrees
  if not secState:
    if not btnDegRad.cget("text") == "Rad":
      equation.append("sin(");
    else:
      equation.append("sin(r(")

  elif secState:
    if not btnDegRad.cget("text") == "Rad":
      equation.append("asin(");
    else:
      equation.append("asin(r(")

  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def cosine():
  # checks what the state of btnDegRad is to determine whether to calculate in radians or degrees
  if not secState:
    if not btnDegRad.cget("text") == "Rad":
      equation.append("cos(");
    else:
      equation.append("cos(r(")

  elif secState:
    if not btnDegRad.cget("text") == "Rad":
      equation.append("acos(");
    else:
      equation.append("acos(r(")

  screenDisplay.configure(text=''.join(equation));
  buttonClear.configure(text="C");

def tangent():
  # checks what the state of btnDegRad is to determine whether to calculate in radians or degrees
  if not secState:
    if not btnDegRad.cget("text") == "Rad":
      equation.append("tan(");
    else:
      equation.append("tan(r(")

  elif secState:
    if not btnDegRad.cget("text") == "Rad":
      equation.append("atan(");
    else:
      equation.append("atan(r(")

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
    
    for i in range(leftPCount-rightPCount):
      equation.append(")")


    equation = ''.join(equation);
    equation = list(equation);

    count=0

    for i in range(len(equation)):
      if equation[i] == '(' and i > 0 :
        if equation[i-1] in '1234567890)':
          equation.insert(i+count,'*')
          count+=1
    
    try:
    
      combEquation = ''.join(equation)

      combEquation = eval(re.sub(r"((?<=^)|(?<=[^\.\d]))0+(\d+)", r"\1\2", str(combEquation)));

      screenDisplay.configure(text=str(combEquation));
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

    leftPCount = str(equation).count("(")
    rightPCount = str(equation).count(")")
    
    for i in range(leftPCount-rightPCount):
      equation.append(")")

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

    leftPCount = str(equation).count("(")
    rightPCount = str(equation).count(")")
    
    for i in range(leftPCount-rightPCount):
      equation.append(")")

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
    
    radLbl.configure(fg="gray")

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

    radLbl.configure(fg="black")

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

# toggles between radians and degrees
def DegRad():
  if btnDegRad.cget("text") == "Deg":
    btnDegRad.configure(text="Rad")
    radLbl.configure(text="D")
    
  elif btnDegRad.cget("text") == "Rad":
    btnDegRad.configure(text="Deg")
    radLbl.configure(text="R")


def btnSec():
  global secState

  if secState:
    secState = False
    btnSin.configure(text="sin", fg="#2D79F0")
    btnCos.configure(text="cos", fg="#2D79F0")
    btnTan.configure(text="tan", fg="#2D79F0")
    buttonMult.configure(text='×', fg="#2D79F0")

  elif not secState:
    secState = True
    btnSin.configure(text="sin⁻¹", fg="#2D79F0")
    btnCos.configure(text="cos⁻¹", fg="#2D79F0")
    btnTan.configure(text="tan⁻¹", fg="#2D79F0")
    buttonMult.configure(text="^", fg="#2D79F0")



# allows keyboard presses to work
def onKeyPress(event):
  if event.char in "1234567890()+*-/.":
    equation.append(event.char)
    screenDisplay.configure(text=''.join(equation))
    buttonClear.configure(text="C");
  elif event.char.lower() == 'c':
    cosine();
  elif event.char.lower() == 's':
    sine();
  elif event.char.lower() == 't':
    tangent();
  elif event.char.lower() == "a":
    answer()
  elif event.keysym == "Return":
    equalSign();
  elif event.keysym == "BackSpace":
    backspace()
  elif event.keysym == "space":
    btnSec()
  elif event.keysym == "Delete":
    clearDisplay()
  elif event.char == "%":
    percentButton()
  elif event.char == "^":
    equation.append("**")
    screenDisplay.configure(text=''.join(equation))
  

window.bind('<KeyPress>', onKeyPress)



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

buttonDecimal = tk.Button(master=numberFrame, text = ".", width = 3, height = 1, command = decimal)


# creates operator buttons
buttonAdd = tk.Button(master=numberFrame, text = "+", width = 3, height = 1, command = addSign);
buttonEqual = tk.Button(master=numberFrame, text = "=", width = 3, height = 1, command = equalSign)
buttonMinus = tk.Button(master=numberFrame, text = "-", width = 3, height = 1, command = minusSign)
buttonMult = tk.Button(master=numberFrame, text = "×",fg="#2D79F0", width = 3, height = 1, command = multSign)
buttonDiv = tk.Button(master=numberFrame, text = "/", width = 3, height = 1, command = divSign)


buttonPerc = tk.Button(master=numberFrame, text = "%", width = 3, height = 1, command = percentButton)

buttonOff = tk.Button(master=numberFrame, text = "OFF", width = 3, height = 1, bg="red", fg="white", command = offButton)

buttonSqrt = tk.Button(master=numberFrame, text = "√", width = 3, height = 1, command = squareRoot);

buttonClear = tk.Button(master=numberFrame, text = "AC", width = 3, height = 1, command = clearDisplay);

buttonAns = tk.Button(master=numberFrame, text = "ans", width = 3, height = 1, command = answer)

buttonLeftParen = tk.Button(master=numberFrame, text = "(", width = 3, height = 1, command = leftParen)
buttonRightParen = tk.Button(master=numberFrame, text = ")", width = 3, height = 1, command = rightParen);

buttonBack = tk.Button(master=screenFrame, height = 1, width = 1, text="⌫", command=backspace)

btnCos = tk.Button(master=numberFrame, text="cos", width=3, height=1, fg="#2D79F0", command=cosine)
btnSin = tk.Button(master=numberFrame, text="sin", width=3, height=1, fg="#2D79F0", command=sine)
btnTan = tk.Button(master=numberFrame, text="tan", width=3, height=1, fg="#2D79F0", command=tangent)

btnSecond = tk.Button(master=numberFrame, text="2nd",width=3, height=1, bg="#2D79F0", fg="white", command=btnSec)

btnDegRad = tk.Button(master=numberFrame, text="Deg", width=3, height=1, command=DegRad)


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

buttonDecimal.grid(row=6, column=1, pady=(0,10));


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

buttonAns.grid(row=6, column=2, padx=(0,18), pady=(0,10));

buttonBack.grid(row=0, column = 5)

btnSin.grid(row=2, column=0, padx=(10,0), pady=(0,5))
btnCos.grid(row=2, column=1, pady=(0,5))
btnTan.grid(row=2, column=2, pady=(0,5),padx=(0,18))

btnSecond.grid(row=1, column=0, padx=(10,0),pady=(0,5))

btnDegRad.grid(row=1, column=3, padx=(0,10), pady=(0,5))


# frame placements
screenFrame.grid(row=0)
numberFrame.grid(row=1)


# keeps a list of button names
buttonNames = [btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,buttonDecimal,buttonAdd,buttonEqual,buttonMinus,buttonMult,buttonDiv,buttonPerc,buttonSqrt,buttonLeftParen,buttonRightParen,buttonAns,buttonClear, buttonBack, btnSin, btnCos, btnTan, btnSecond, btnDegRad]

# removes bg highlight for all buttons
# adds fg highlight
for b in buttonNames:
  b["activeforeground"] = "#625E61"
  b["activebackground"] = b["bg"]

# removes bg highlight for colored buttons
# adds fg highlight
buttonOff["activebackground"] = buttonOff["bg"]
buttonOff["activeforeground"] = "lightgray"
btnSecond["activeforeground"] = "lightgray"

# adds fg highlight for colored-text buttons
btnSin["activeforeground"] = "blue"
btnCos["activeforeground"] = "blue"
btnTan["activeforeground"] = "blue"

# creates label displaying radian/degree state
radLbl = tk.Label(master=screenFrame, text="R", font=("Arial", 6), anchor="ne", height=1, width=1)
radLbl.grid(row=0, column=0)


window.mainloop();