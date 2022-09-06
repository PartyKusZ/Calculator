import string
import tkinter as tk





class calculator_t():
    input_data = " "
    numbers = []
    math_operations = []
    result = 0
    buttons_list = []

    def __init__(self):
        self.main_window = tk.Tk()
        self.label = tk.Label(self.main_window,width=50,text=self.input_data)
        self.label.grid(columnspan=4,ipadx=70)
        
        self.buttons_list.append(tk.Button(self.main_window, text="1",command = self.one_button))
        self.buttons_list.append(tk.Button(self.main_window, text="2",command =  self.two_button))
        self.buttons_list.append(tk.Button(self.main_window, text="3",command =  self.three_button))
        self.buttons_list.append(tk.Button(self.main_window, text="4",command =  self.four_button))
        self.buttons_list.append(tk.Button(self.main_window, text="5",command = self.five_button))
        self.buttons_list.append(tk.Button(self.main_window, text="6",command = self.six_button))
        self.buttons_list.append(tk.Button(self.main_window, text="7",command = self.seven_button))
        self.buttons_list.append(tk.Button(self.main_window, text="8",command =  self.eight_button))
        self.buttons_list.append(tk.Button(self.main_window, text="9",command = self.nine_button))
        self.buttons_list.append(tk.Button(self.main_window, text="0",command = self.zero_button))
        self.buttons_list.append(tk.Button(self.main_window, text=".",command = self.comma_button))
        self.buttons_list.append(tk.Button(self.main_window, text="c",command = self.clear_button))
        self.buttons_list.append(tk.Button(self.main_window, text="=",command = self.compute))
        self.buttons_list.append(tk.Button(self.main_window, text="+",command = self.add_button))
        self.buttons_list.append(tk.Button(self.main_window, text="-",command = self.subsract_button))
        self.buttons_list.append(tk.Button(self.main_window, text="*",command = self.multiply_button))
        self.buttons_list.append(tk.Button(self.main_window, text="/",command = self.divide_button))
        for i in range(4):
            for j in range(4):
                self.buttons_list[i * 4 + j].grid(row=i+1, column=j+1)
        self.buttons_list[16].grid(row=5, column=0)
       
    def init(self):
        self.main_window.mainloop()
    def update(self):
        self.label.config(text=self.input_data)

    def one_button(self):
        self.input_data += "1"
        self.update()
    def two_button(self):
        self.input_data += "2"
        self.update()
    def three_button(self):
        self.input_data += "3"
        self.update()
    def four_button(self):  
        self.input_data += "4"
        self.update()
    def five_button(self): 
        self.input_data += "5"
        self.update()
    def six_button(self):  
        self.input_data += "6"
        self.update()
    def seven_button(self):
        self.input_data += "7"
        self.update()
    def eight_button(self):
        self.input_data += "8"
        self.update()
    def nine_button(self):
        self.input_data += "9"
        self.update()
    def zero_button(self): 
        self.input_data += "0"    
        self.update()
    def add_button(self):
        if self.input_empty():
            if self.last_character():
                self.input_data += "+"
        self.update()
         
    def subsract_button(self):
            if self.last_character():
                self.input_data += "-"
            self.update()
    def multiply_button(self):
        if self.input_empty():
            if self.last_character():
                self.input_data += "*"
        self.update()
        
    def divide_button(self):
        if self.input_empty():
            if self.last_character():
                self.input_data += "/"
        self.update()
    def comma_button(self):
        if self.input_empty():
            if self.last_character():
                self.input_data += "."
        self.update()
    def clear_button(self):
        self.input_data = " "
        self.numbers.clear()
        self.math_operations.clear() 
        self.update()

    def input_empty(self):
        if self.input_data == " ":
            return False
        else:
            return True
    def last_character(self):
        if self.input_data[-1] == "+" or self.input_data[-1] == "-" or self.input_data[-1] == "*" or self.input_data[-1] == "/" or self.input_data[-1] ==  "." :
            return False
        else:
            return True
    def math_char(self,i):
        if i == "+" or i == "-" or i == "*" or i == "/" :
            return True
        else:
            return False
    def parse_input_data(self):
        last = 0
        if self.input_data[0] == " ":
            self.input_data = self.input_data[1:]
        while not self.last_character():
            self.input_data = self.input_data[:-1]
    
        for c, i in enumerate(self.input_data):            
            if self.math_char(i) and c > 0:
                self.numbers.append((self.input_data[last:c]))
                self.math_operations.append(self.input_data[c])
                last = c + 1
        self.numbers.append((self.input_data[last:]))


        
    def compute(self):
        index = 0
        if "/0" in self.input_data:
            self.input_data = "bład dzielenia: nie da się dzielć przez 0"
            self.clear_button()
        else:
            self.parse_input_data()
            for i in range(len(self.numbers)):
                self.numbers[i] = float(self.numbers[i])
            while "*" in self.math_operations:
                index = self.math_operations.index("*")
                self.numbers[index] = float(self.numbers[index] * self.numbers[index + 1])
                self.numbers.pop(index + 1)
                self.math_operations.pop(index)
            while "/" in self.math_operations:
                index = self.math_operations.index("/")
                self.numbers[index] = float(self.numbers[index] / self.numbers[index + 1])
                self.numbers.pop(index + 1)
                self.math_operations.pop(index)
            while "+" in self.math_operations:
                index = self.math_operations.index("+")
                self.numbers[index] = float(self.numbers[index] + self.numbers[index + 1])
                self.numbers.pop(index + 1)
                self.math_operations.pop(index)
            while "-" in self.math_operations:
                index = self.math_operations.index("-")
                self.numbers[index] = float(self.numbers[index] - self.numbers[index + 1])
                self.numbers.pop(index + 1)
                self.math_operations.pop(index)
            self.input_data = str(self.numbers[0])
            self.numbers.clear()
            self.math_operations.clear()
            self.update()
            
        
    def test(self):
        self.one_button()
        self.multiply_button()
        self.subsract_button()
        self.two_button()
        self.subsract_button()
        self.seven_button()
        self.compute()
        print(self.input_data)
        print(self.numbers)
        print(self.math_operations)