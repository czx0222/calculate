import time

import math
import re
from math import *

def performance_analysis():
    start_time = time.time()  # 记录开始时间

    def expression_format(expression):
        expression = re.sub(' ', '', expression)
        expression_parts = re.split('(-[\d+,π,e]\.?\d*)', expression)
        expression_list = [part for part in expression_parts if part]
        final_expression = []
        for item in expression_list:
            if len(final_expression) == 0 and re.match('-[\d+,π,e]\.?\d*$', item):
                final_expression.append(item)
                continue
            if len(final_expression) > 0 and re.match('[\+\-\*\/\(\)\%\^\√]$', final_expression[-1]):
                final_expression.append(item)
                continue
            item_parts = re.split('([\+\-\*\/\(\)\%\^\√])', item)
            final_expression += [part for part in item_parts if part]
        return final_expression

    def is_operator(expression):
        operators = ['+', '-', '*', '/', '(', ')', '%', '^', '√', 'sin', 'cos', 'ln', 'tan', 'log']
        return True if expression in operators else False

    def rate(op, now_op):
        rate1 = ['+', '-']
        rate2 = ['*', '/', '%']
        rate3 = ['^', '√', 'sin', 'cos', 'ln', 'log', 'tan']
        rate4 = ['(']
        rate5 = [')']

        if op in rate1:
            if now_op in rate2 or now_op in rate3 or now_op in rate4:
                return -1
            else:
                return 1
        elif op in rate2:
            if now_op in rate3 or now_op in rate4:
                return -1
            else:
                return 1
        elif op in rate3:
            if now_op in rate4:
                return -1
            else:
                return 1
        elif op in rate4:
            if now_op in rate5:
                return 0
            else:
                return -1

    def calculate1(n1, n2, op):
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '%': lambda x, y: x % y,
            '^': lambda x, y: x ** y
        }
        result = operations[op](n1, n2)
        return result

    def calculate2(op_stack, num_stack):
        num2 = num_stack.pop()
        if op_stack[-1] == '√':
            op = op_stack.pop()
            num_stack.append(sqrt(num2))
        elif op_stack[-1] == 'sin':
            op = op_stack.pop()
            num_stack.append(round(sin(num2 * math.pi / 180), 3))
        elif op_stack[-1] == 'cos':
            op = op_stack.pop()
            num_stack.append(round(cos(num2 * math.pi / 180), 3))
        elif op_stack[-1] == 'tan':
            op = op_stack.pop()
            num_stack.append(round(tan(num2 * math.pi / 180), 3))
        elif op_stack[-1] == 'ln':
            op = op_stack.pop()
            num_stack.append(log(num2))
        elif op_stack[-1] == 'log':
            op = op_stack.pop()
            num_stack.append(log10(num2))

    def calculate(list):
        num_stack = []
        op_stack = []
        for item in list:
            operator = is_operator(item)
            if not operator:
                if item == 'π':
                    num_stack.append(pi)
                elif item == '-π':
                    num_stack.append(-pi)
                elif item == 'e':
                    num_stack.append(e)
                elif item == '-e':
                    num_stack.append(-e)
                else:
                    num_stack.append(float(item))
            else:
                while True:
                    if len(op_stack) == 0:
                        op_stack.append(item)
                        break
                    tag = rate(op_stack[-1], item)
                    if tag == -1:
                        op_stack.append(item)
                        break
                    elif tag == 0:
                        op_stack.pop()
                        calculate2(op_stack, num_stack)
                        break
                    elif tag == 1:
                        if item in ['√', 'sin', 'cos', 'tan', 'log', 'ln']:
                            op_stack.append(item)
                            break
                        op = op_stack.pop()
                        num2 = num_stack.pop()
                        num1 = num_stack.pop()
                        num_stack.append(calculate1(float(num1), float(num2), op))
        while len(op_stack) != 0:
            op = op_stack.pop()
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num_stack.append(calculate1(float(num1), float(num2), op))
        result = str(num_stack[0])
        if result[len(result) - 1] == '0' and result[len(result) - 2] == '.':
            result = result[0:-2]
        return result

    result = calculate(formula_format("2 + 2"))

    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算执行时间

    print(f"执行时间: {elapsed_time} 秒")
    return result

if __name__ == '__main__':
    result = performance_analysis()
