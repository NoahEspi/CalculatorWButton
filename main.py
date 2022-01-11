import tkinter as tk;

window = tk.Tk();

window.columnconfigure(0, minsize=50)
window.rowconfigure([0, 1], minsize=50)

equation = [];

# numbers
def numZero():
  equation.append('0');
def numOne():
  equation.append('1');
def numTwo():
  equation.append('2');
def numThree():
  equation.append('3');
def numFour():
  equation.append('4');
def numFive():
  equation.append('5');
def numSix():
  equation.append('6');
def numSeven():
  equation.append('7');
def numEight():
  equation.append('8');
def numNine():
  equation.append('9');

# operations
def addSign():
  equation.append('+');

def minusSign():
  equation.append('-');

def multSign():
  equation.append('*');

def divSign():
  equation.append('/');

def equalSign():
  try:
    combEquation = ''.join(equation);
    combEquation = eval(combEquation);
    print(combEquation);
    equation.clear();
  except SyntaxError:
    equation.clear();

# numbers
button0 = tk.Button(window, text = "0", width = 3, height = 1, command = numZero);
button1 = tk.Button(window, text = "1", width = 3, height = 1, command = numOne);
button2 = tk.Button(window, text = "2", width = 3, height = 1, command = numTwo);
button3 = tk.Button(window, text = "3", width = 3, height = 1, command = numThree);
button4 = tk.Button(window, text = "4", width = 3, height = 1, command = numFour);
button5 = tk.Button(window, text = "5", width = 3, height = 1, command = numFive);
button6 = tk.Button(window, text = "6", width = 3, height = 1, command = numSix);
button7 = tk.Button(window, text = "7", width = 3, height = 1, command = numSeven);
button8 = tk.Button(window, text = "8", width = 3, height = 1, command = numEight);
button9 = tk.Button(window, text = "9", width = 3, height = 1, command = numNine);

# operations
buttonAdd = tk.Button(window, text = "+", width = 3, height = 1, command = addSign);
buttonEqual = tk.Button(window, text = "=", width = 3, height = 1, command = equalSign)
buttonMinus = tk.Button(window, text = "-", width = 3, height = 1, command = minusSign)
buttonMult = tk.Button(window, text = "×", width = 3, height = 1, command = multSign)
buttonDiv = tk.Button(window, text = "÷", width = 3, height = 1, command = divSign)


# numbers
button1.grid(row=0, column=0)
button2.grid(row=0, column=1);
button3.grid(row=0, column=2);
button4.grid(row=1, column=0);
button5.grid(row=1, column=1);
button6.grid(row=1, column=2);
button7.grid(row=2, column=0);
button8.grid(row=2, column=1);
button9.grid(row=2, column=2);
button0.grid(row=3, column=1);

# operations
buttonAdd.grid(row=0, column=3);
buttonEqual.grid(row=4, column=3);
buttonMinus.grid(row=1, column=3);
buttonMult.grid(row=2,column=3);
buttonDiv.grid(row=3,column=3);


window.mainloop();