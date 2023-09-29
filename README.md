

 作业基本信息
|这个作业属于哪个课程  | [<2301-计算机学院-软件工程>](https://bbs.csdn.net/forums/ssynkqtd-05) |
|--|--|
| 这个作业要求在哪里 |  [软件工程实践第一次作业](https://bbs.csdn.net/topics/617294583)|
| 这个作业的目标 | <完成一个具有可视化界面的计算器>|
|其他参考文献|[tkinter教程](http://c.biancheng.net/tkinter/button-widget.html) [Math库](https://blog.csdn.net/weixin_45082954/article/details/104949877)|


## Gitcode项目地址
[Python实现简易图形化计算器](https://gitcode.net/chenzhixin0302/python)
## PSP表格

| PSP |Personal Software Process Stages  |预估耗时（分钟）|实际耗时（分钟）|
|--|--|--|--|
| Planning |计划 |10|15|
|• Estimate|• 估计这个任务需要多少时间|10|15|
|Development |开发 |410|570|
|• Analysis|• 需求分析 (包括学习新技术）|120|80|
|• Design Spec |• 生成设计文档 |20|10|
|• Design Review |•  设计复审 |30|20|
|• Coding Standard|• 代码规范 (为目前的开发制定合适的规范) |15|20|
|• Design |• 具体设计 |20|30|
|• Coding |• 具体编码 |180|200|
|• Code Review |• 代码复审  |15|20|
|• Test |	• 测试（自我测试，修改代码，提交修改） |40|30|
|Reporting |报告 |160|180|
|• Test Repor |• 测试报告 |70|80|
|• Size Measurement |• 计算工作量 |40|30|
|• Postmortem & Process Improvement Plan |• 事后总结, 并提出过程改进计划 |50|70|
| |合计 |610|785|
## 解题思路描述

 - 本次作业是使用**Python**和**tkinter库**来实现具有可视化界面的计算器。
 - **创建图形化界面：** 通过tkinter库创建了一个GUI窗口，同时创建显示数学表达式的标签、输入数学表达式和显示算式结果的文本框和一个包含数字、运算符的按钮网格，每个按钮都与一个函数相关，单击按钮时调用改命令。
 - **数学表达式计算：** 本次作业中花费时间最多是在实现复杂数学表达式的计算，通过查阅相关资料，我将输入的数学表达式进行拆分，然后使用两个堆栈（一个用于运算符，一个用于数字）来解析和计算表达式。
## 接口设计和实现过程
 **类 class CalculatorApp**：

> 表示主应用程序窗口。它初始化图形化窗口，并创建了计算器所需的部件和实现一些基本功能
	

 - **窗口布局**

> layout 方法用于初始化计算器的用户界面，经创建了一个标签（Label）来显示计算结果和一个文本框（Entry）来接收输入，然后通过循环创建了一个按钮矩阵，并为每个按钮关联了相应的功能。

```python
    def layout(self):
    	#初始化界面
        self.screen = tk.Label(self.root, width=31, height=2,  bg='#BDBDBD', anchor='center',
                              textvariable=self.calculatation_formula,relief = 'sunken', font=('微软雅黑', 17))
        self.screen.grid(row=0, columnspan=6,pady=(5,5))
        self.entry = tk.Entry(self.root, width=33, bd=3,bg='#F5F5F5', justify="right", font=('微软雅黑', 17),insertbackground="#757575")
        self.entry.grid(row=1, columnspan=6, padx=5, pady=5)
        myButton = partial(tk.Button, self.root, width=7,height=3,bd=3,pady=10,padx=10, cursor='hand2', activebackground='#B3E5FC',relief='sunken')
		#按钮矩阵
        buttons = [
            ('(', '('), (')', ')'), ('^', '^'), ('/', '/'), ('*', '*'),('删除', 'backspace'),
            ('log', 'log('), (' cos ', 'cos('), ('7', '7'), ('8', '8'), ('9', '9'),('清空', 'clear'),
            (' ln ', 'ln('), (' sin ', 'sin('), (' 6 ', '6'), (' 5 ', '5'), ('4', '4'),('+', '+'),
            (' e ', 'e'), (' tan ', 'tan('), (' 3 ', '3'), (' 2 ', '2'), ('1', '1'),('-', '-'),
            (' √ ', '√('),(' π ', 'π'), (' % ', '%'), (' 0 ', '0'), (' . ', '.'), (' \n = \n ', 'calculate')
        ]
        row = 2
        col = 0
        #按钮关联对应功能
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
```

 - **处理输入的字符**

>&ensp;&ensp;&ensp;&ensp;根据用户点击的按钮，执行不同的操作。如果 argu 是 "backspace"，则删除最后一个字符；如果是 "clear"，则清空文本框；否则，在文本框中插入 argu。

```python
    def input(self, argu):
        formula = self.entry.get()
        if argu == 'backspace':
            self.backspace()
        elif argu == 'clear':
            self.clear()
        else:
            self.entry.insert(tk.INSERT, argu)
```

 - **点击'='式计算结果**
 

> &ensp;&ensp;&ensp;&ensp;计算结果：获取文本框中的输入表达式。将表达式传递给calculate 函数进行计算。如果计算成功，清空文本框并将计算结果插入到文本框中，并将计算结果显示在标签上。如果计算失败，清空文本框并显示"出错"。

```python
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
```

 - **将公式字符串拆分为标记方便后续计算**

>  &ensp;&ensp;&ensp;&ensp;将字符串分割成多个部分,创建一个空列表 final_expression 用于存储最终的表达式列表,迭代处理分割后的部分。
```python
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

```

 - **结果计算**

> 	初始化一个空的数字栈 **num_stack** 和一个空的运算符栈 **op_stack**，用于在计算过程中存储数字和运算符。遍历输入的表达式列表 list 中的每个元素 item。
> 对于每个元素 item，首先检查它是否是运算符（使用 is_operator(item) 函数）。
> 1、如果不是运算符，则将其视为数字或特殊常数（如π和e）
> 2、如果 item 是运算符，进入循环，
> &ensp;&ensp;（1）如果运算符栈  为空，或者运算符栈顶的运算符的优先级低于当前运算符，则将 item 压入运算符栈 
&ensp;&ensp;（2）如果运算符栈顶的运算符的优先级高于等于当前运算符，或者是'√'、'sin' 等，则从运算符栈 弹出一个运算符，并从数字栈  弹出两个数值进行计算，然后将计算结果压入数字栈 num_stack。
&ensp;&ensp;（3）如果当前运算符是一元运算符（如 '√'、'sin' 等），则将其压入运算符栈。
循环结束后，如果运算符栈 中还有剩余的运算符，依次从运算符栈中弹出运算符，并从数字栈 弹出两个数值进行计算，然后将计算结果压入数字栈 。
最后，将数字栈  中的最终结果转换为字符串，然后将结果返回。

```python
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
                    if item in ['√', 'sin', 'cos','tan','log','ln']:
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
    if result.endswith('.0'):
        result = result[:-2]
    return result
```

## 关键功能展示

 - **加减乘除运算**
![](https://img-blog.csdnimg.cn/b48bc6eceaa14fad81a2c06dc11f2452.gif#pic_center)

 - **三角函数、对数等运算**
![在这里插入图片描述](https://img-blog.csdnimg.cn/bcc1d54427d648a3907e205738665b3f.gif#pic_center)

 - **删除、清空功能**
![在这里插入图片描述](https://img-blog.csdnimg.cn/09c36492a52748068702138f15d49268.gif#pic_center)


## 异常处理

> 当用户输入错误的表达式时会通过输出错误及时提醒用户

 - **案例1：除数为0**

![](https://img-blog.csdnimg.cn/69cefdacd5be4961958e214fbcb405f8.gif#pic_center)
 - **案例2：三角函数等运算时为加右括号**

 -![](https://img-blog.csdnimg.cn/49a0f4b70742437f8141584965fa2708.gif#pic_center)
 
 - **处理代码**

```python
     try:
            formula = self.entry.get()
            result = calculate(expression_format(formula))
            self.clear()
            self.entry.insert(tk.END, result)
            self.calculatation_formula.set(''.join(formula + '='))
        except Exception as e:# 捕获更具体的异常，以便排除错误
            self.clear()
            self.entry.insert(tk.END, '出错')
```





 
