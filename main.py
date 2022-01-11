import tkinter as tk;
import math; from math import sqrt


# window configuration
window = tk.Tk();

window.columnconfigure(0, weight=1, minsize=50)
window.rowconfigure(0, weight=1, minsize=50)

window.title("Calcutator Fo Real")


# frame configurations
screenFrame = tk.Frame(window, relief=tk.RAISED, borderwidth = 1)

numberFrame = tk.Frame(window)

# establishes variables
equation = [];
prevAns = "";



# creates number functions
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

def doubleZero():
  equation.append("00");
  screenDisplay.configure(text=equation);

def decimal():
  equation.append('.');
  screenDisplay.configure(text=equation);



# creates operator functions
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

def leftParen():
  equation.append("(");
  screenDisplay.configure(text=equation);

#################################################### add so it auto adds right at end of equation if not in it
def rightParen():
  equation.append(")");
  screenDisplay.configure(text=equation);


# calculation functions

# calculates exisitng equation. if it can't, returns error
def equalSign():
  global equation
  global prevAns

  # checks if equation is empty
  if equation != []:
    
    # checks parenthesis capatability
    leftCount = equation.count("(");
    rightCount = equation.count(")");
    if leftCount != rightCount:
      screenDisplay.configure(text="ERROR: SYNTAX (PARENTHESES)");
      equation.clear();

    else:
      try:
        
        combEquation = ''.join(equation);
        combEquation = eval(combEquation);

        screenDisplay.configure(text=combEquation);
        equation.clear()
        prevAns = str(combEquation);
      except Exception:
        equation.clear();
        screenDisplay.configure(text="ERROR: SYNTAX")


# same function as equalSign except divides the answer by 100
def percentButton():
  global equation
  global prevAns
  
  if equation != []:

    # checks parenthesis capatability
    leftCount = equation.count("(");
    rightCount = equation.count(")");
    if leftCount != rightCount:
      screenDisplay.configure(text="ERROR: SYNTAX (PARENTHESES)");
      equation.clear();

    else:
      try:
        combEquation = ''.join(equation);
        combEquation = eval(combEquation);

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

    # checks parenthesis capatability
    leftCount = equation.count("(");
    rightCount = equation.count(")");
    if leftCount != rightCount:
      screenDisplay.configure(text="ERROR: SYNTAX (PARENTHESES)");
      equation.clear();

    else:
      try:
        combEquation = ''.join(equation);
        combEquation = eval(combEquation);

        combEquation = sqrt(combEquation);

        combEquation = str(combEquation);

        screenDisplay.configure(text=combEquation);
        equation.clear()
        prevAns = str(combEquation);
      except Exception:
        equation.clear();
        screenDisplay.configure(text="ERROR: SYNTAX")


# establishes off button
def offButton():
  global prevAns

  # checks state of button
  if buttonOff.cget("text") == "OFF":
    
    # changes button states
    button0.configure(state="disabled")
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    button4.configure(state="disabled")
    button5.configure(state="disabled")
    button6.configure(state="disabled")
    button7.configure(state="disabled")
    button8.configure(state="disabled")
    button9.configure(state="disabled")
    buttonDecimal.configure(state="disabled")
    buttonAdd.configure(state="disabled")
    buttonEqual.configure(state="disabled")
    buttonMinus.configure(state="disabled")
    buttonMult.configure(state="disabled")
    buttonDiv.configure(state="disabled")
    buttonPerc.configure(state="disabled")
    buttonSqrt.configure(state="disabled")
    buttonDoubleZero.configure(state="disabled")
    buttonLeftParen.configure(state="disabled")
    buttonRightParen.configure(state="disabled")
    buttonAns.configure(state="disabled")
    buttonClear.configure(state="disabled")

    # changes state (word) of power button
    buttonOff.configure(text="ON")
    
    # turns screen "off" and clears previous display
    equation.clear()
    prevAns = "";
    screenDisplay.configure(text=equation, bg="black")

  # checks state of button
  elif buttonOff.cget("text") == "ON":

    # changes button states
    button0.configure(state="normal")
    button1.configure(state="normal")
    button2.configure(state="normal")
    button3.configure(state="normal")
    button4.configure(state="normal")
    button5.configure(state="normal")
    button6.configure(state="normal")
    button7.configure(state="normal")
    button8.configure(state="normal")
    button9.configure(state="normal")
    buttonDecimal.configure(state="normal")
    buttonAdd.configure(state="normal")
    buttonEqual.configure(state="normal")
    buttonMinus.configure(state="normal")
    buttonMult.configure(state="normal")
    buttonDiv.configure(state="normal")
    buttonPerc.configure(state="normal")
    buttonSqrt.configure(state="normal")
    buttonClear.configure(state="normal")
    buttonDoubleZero.configure(state="normal")
    buttonRightParen.configure(state="normal")
    buttonLeftParen.configure(state="normal")
    buttonAns.configure(state="normal")


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
    screenDisplay.configure(text=equation);

# clears the existing display
def clearDisplay():
  global equation 

  equation.clear();
  screenDisplay.configure(text=equation);



# configures number display
screenDisplay = tk.Label(master=screenFrame, text=equation, anchor="e", fg="black", bg="#B9FFEE", width=25)

screenDisplay.grid(row=0, column=1)



# creates number buttons
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
buttonDoubleZero = tk.Button(master = numberFrame, text="00", width = 3, height = 1, command = doubleZero)
buttonDecimal = tk.Button(master=numberFrame, text = ".", width = 3, height = 1, command = decimal)


# creates operator buttons
buttonAdd = tk.Button(master=numberFrame, text = "+", width = 3, height = 1, command = addSign);
buttonEqual = tk.Button(master=numberFrame, text = "=", width = 3, height = 1, command = equalSign)
buttonMinus = tk.Button(master=numberFrame, text = "-", width = 3, height = 1, command = minusSign)
buttonMult = tk.Button(master=numberFrame, text = "×", width = 3, height = 1, command = multSign)
buttonDiv = tk.Button(master=numberFrame, text = "÷", width = 3, height = 1, command = divSign)
buttonPerc = tk.Button(master=numberFrame, text = "%", width = 3, height = 1, command = percentButton)
buttonOff = tk.Button(master=numberFrame, text = "OFF", width = 3, height = 1, command = offButton)
buttonSqrt = tk.Button(master=numberFrame, text = "√", width = 3, height = 1, command = squareRoot);
buttonClear = tk.Button(master=numberFrame, text = "C", width = 3, height = 1, command = clearDisplay);
buttonAns = tk.Button(master=numberFrame, text = "ans", width = 3, height = 1, command = answer)
buttonLeftParen = tk.Button(master=numberFrame, text = "(", width = 3, height = 1, command = leftParen)
buttonRightParen = tk.Button(master=numberFrame, text = ")", width = 3, height = 1, command = rightParen);



# places number buttons
button1.grid(row=4, column=0, padx=(10,0), pady=(0,5));
button2.grid(row=4, column=1, pady=(0,5));
button3.grid(row=4, column=2, padx=(0,18), pady=(0,5));
button4.grid(row=3, column=0, padx=(10,0), pady=(0,5));
button5.grid(row=3, column=1, pady=(0,5));
button6.grid(row=3, column=2, padx=(0,18), pady=(0,5));
button7.grid(row=2, column=0, padx=(10,0), pady=(0,5));
button8.grid(row=2, column=1, pady=(0,5));
button9.grid(row=2, column=2, padx=(0,18), pady=(0,5));
button0.grid(row=5, column=0, padx=(10,0), pady=(0,10));
buttonDecimal.grid(row=5, column=2, padx=(0,18), pady=(0,10));


# places operator buttons
buttonAdd.grid(row=1, column=3, padx=(0,10), pady=(0,5));
buttonEqual.grid(row=5, column=3, padx=(0,10), pady=(0,5));
buttonMinus.grid(row=2, column=3, padx=(0,10), pady=(0,5));
buttonMult.grid(row=3,column=3, padx=(0,10), pady=(0,5));
buttonDiv.grid(row=4, column=3, padx=(0,10), pady=(0,5));
buttonPerc.grid(row=0, column=2, padx=(0,18), pady=(0,5));
buttonOff.grid(row=0, column=0, padx=(10,0), pady=(0,5));
buttonSqrt.grid(row=0, column=1, pady=(0,5));
buttonClear.grid(row=0, column=3, padx=(0,10), pady=(0,5));
buttonDoubleZero.grid(row=5, column=1, pady=(0,10));
buttonLeftParen.grid(row=1, column=1, pady=(0,5));
buttonRightParen.grid(row=1, column=2, padx=(0,18), pady=(0,5));
buttonAns.grid(row=1, column=0, padx=(10,0), pady=(0,5));


# frame placements
screenFrame.grid(row=0)
numberFrame.grid(row=1)


window.mainloop();