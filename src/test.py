import unittest
import tkinter as tk
from main import *
from calculate import  *

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = CalculatorApp(self.root)
        self.app.layout()

    def Down(self):
        self.root.destroy()

    def test_clear(self):
        self.app.entry.insert(tk.END, '6*9+sin(30)+log(12)+6^2')
        self.app.clear()
        self.assertEqual(self.app.entry.get(), '')
        self.assertEqual(self.app.calculatation_formula.get(), '')

    def test_backspace(self):
        self.app.entry.insert(tk.END, '6*9+sin(30)+log(12)+6^2+6/2')
        self.app.backspace()
        self.assertEqual(self.app.entry.get(), '6*9+sin(30)+log(12)+6^2+6/')

    def test_input(self):
        self.app.input('5')
        self.assertEqual(self.app.entry.get(), '5')

    def test_get_result(self):
        self.app.entry.insert(tk.END, '6*9+sin(30)+ln(e)+6^2+6/2-3*2')
        self.app.get_result()
        self.assertEqual(self.app.entry.get(), '88.5')
        self.assertEqual(self.app.calculatation_formula.get(), '6*9+sin(30)+ln(e)+6^2+6/2-3*2=')

    def test_expression_format(self):
        # 测试 formula_format 函数
        self.assertEqual(expression_format("-2+2-7*5"), ['-2', '+', '2','-','7','*','5'])
        self.assertEqual(expression_format("ln(e)+5"), ['ln', '(', 'e', ')', '+', '5'])
        self.assertEqual(expression_format("π*2"), ['π', '*', '2'])

    def test_calculate(self):
        # 测试 final_calc 函数
        self.assertEqual(calculate(['-2', '+', '2','-','7','*','5']), '-35')
        self.assertEqual(calculate(['ln', '(', 'e', ')', '+', '5']), '6')
        self.assertEqual(calculate(['π', '*', '2']), '6.283185307179586')

if __name__ == '__main__':
    unittest.main()


