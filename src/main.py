import tkinter as tk
from functools import partial
from calculate import *
import re


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title('科学计算器')
        self.root.resizable(0, 0)
        self.calculatation_formula = tk.StringVar()
        self.root.configure(bg='#B3E5FC')
        self.screen = None
        self.entry = None

    def layout(self):
        self.screen = tk.Label(self.root, width=31, height=2,  bg='#BDBDBD', anchor='center',
                              textvariable=self.calculatation_formula,relief = 'sunken', font=('微软雅黑', 17))
        self.screen.grid(row=0, columnspan=6,pady=(5,5))
        self.entry = tk.Entry(self.root, width=33, bd=3,bg='#F5F5F5', justify="right", font=('微软雅黑', 17),insertbackground="#757575")
        self.entry.grid(row=1, columnspan=6, padx=5, pady=5)
        myButton = partial(tk.Button, self.root, width=7,height=3,bd=3,pady=10,padx=10, cursor='hand2', activebackground='#B3E5FC',relief='sunken')

        buttons = [
            ('(', '('), (')', ')'), ('^', '^'), ('/', '/'), ('*', '*'),('删除', 'backspace'),
            ('log', 'log('), (' cos ', 'cos('), ('7', '7'), ('8', '8'), ('9', '9'),('清空', 'clear'),
            (' ln ', 'ln('), (' sin ', 'sin('), (' 6 ', '6'), (' 5 ', '5'), ('4', '4'),('+', '+'),
            (' e ', 'e'), (' tan ', 'tan('), (' 3 ', '3'), (' 2 ', '2'), ('1', '1'),('-', '-'),
            (' √ ', '√('),(' π ', 'π'), (' % ', '%'), (' 0 ', '0'), (' . ', '.'), (' \n = \n ', 'calculate')
        ]
        row = 2
        col = 0
        for (text, command) in buttons:
            if text == ' \n = \n ':
                button = myButton(text=text, command=lambda cmd=command: self. get_result(),bg='#BDBDBD')
                button.grid(row=row, column=col)
            else:
                button = myButton(text=text, command=lambda cmd=command: self.input(cmd),bg='#F5F5F5',font=('微软雅黑',9))
                button.grid(row=row, column=col)
            col += 1
            if col > 5:
                col = 0
                row += 1

    def backspace(self):
        self.entry.delete(len(self.entry.get()) - 1)

    def clear(self):
        self.entry.delete(0, tk.END)
        self.calculatation_formula.set('')

    def input(self, argu):
        formula = self.entry.get()
        if argu == 'backspace':
            self.backspace()
        elif argu == 'clear':
            self.clear()
        else:
            self.entry.insert(tk.INSERT, argu)

    def get_result(self):
        try:
            formula = self.entry.get()
            result = calculate(expression_format(formula))
            self.clear()
            self.entry.insert(tk.END, result)
            self.calculatation_formula.set(''.join(formula + '='))
        except Exception as e:# 捕获更具体的异常，以便排除错误
            self.clear()
            self.entry.insert(tk.END, '出错')

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    app.layout()
    root.mainloop()
