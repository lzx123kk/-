#四则运算2.4
#改进：1.增加图形化界面 2.用户可以指定题目个数和运算符个数 3.用户可以指定算式打印的列数 
######4.输出结果将*/符号转化为×÷ 5.控制台输出运算，图形界面不打印结果
import random
import string
from tkinter import *


#生成随机数组，数字范围为1-99。参数length：操作数数量（即操作符数量+1）
def random_list(length):
    if length>=0:
        length=int(length)
    random_list = []
    for i in range(length):
        random_list.append(random.randint(1, 99))
    return random_list
 
#生成随机的运算符，数字范围为0-3。参数length：操作符数量
def random_operator(length):
    operator = ['+','-','*','/']
    if length>=0:
        length=int(length)
    random_operator = []
    for i in range(length):
        random_operator.append(operator[random.randint(0, 3)])
    return random_operator
 
#参数：x个运算符，操作数列表，操作符列表
#设置flag检测不超过100且为正整数的约束条件
def flag(x,operations, operator):
    flag1= 0
    flag2= 0
    #判断是否符合各个位运算都不超过100且为正整数，循环检测
    for i in range(0,x):
        m = str(operations[i]) + operator[i] + str(operations[i+1])
        m = eval(m)
        if (0<m<100) & isinstance(m,int):
            flag1=1
        else:
            flag1=0
            break#!!!!!不能只写flag1=0,不然下一次的flag1就会覆盖上次的
    #判断运算结果在100以内且为正整数
    res = str(operations[0])
    for i in range(0,x):
        res = res + operator[i] + str(operations[i+1])
    res_right = eval(res)
    if (0<res_right<100) & isinstance(res_right,int):
        flag2=1
    flag=flag1+flag2
    return flag
 
#参数：x个运算符，操作数列表，操作符列表，i（打印算式个数的计数）
#打印算式及结果，累计算式数量
def print_result(x,operations, operator,loop):
    res = str(operations[0])
    for i in range(0,x):
        res = res + operator[i] + str(operations[i+1])
    res_right = eval(res)
    
    #*/转变成×÷
    res_left = str(operations[0])
    for i in range(0,x):
        if operator[i]=='*':
            operator[i]='×'
        if operator[i]=='/':
            operator[i]='÷'
        res_left = res_left + operator[i] + str(operations[i+1])
        
    print(res_left,'=',res_right)
    loop+=1
    txt.insert(END, res_left+'\t'+'=' + '\t')   # 追加显示运算结果
    return loop
 
#四则运算主函数。参数：num1为需打印算式个数，num2为操作符数量，col为列数。
def run(num1,num2,col):
    print("输出算式个数为："+ num1)
    num1 = int(num1)
    num1_ = num1 + 0 #字符串转换为整数
    num2 = int(num2)
    num2_ = num2 + 0 #字符串转换为整数
    col = int(col)
    col_ = col + 0 #字符串转换为整数
    i = 0
    while i<num1_:
        operations=random_list(num2_+1)
        operator=random_operator(num2_)
        if 2==flag(num2_,operations, operator): #判断flag
            i=print_result(num2_,operations, operator,i)
            if i % col_ ==0: #输出的列数
                txt.insert(END,'\n')
    
    #inp1.delete(0, END)  # 清空输入
 
root = Tk()
root.geometry('460x240')
root.title('简单四则运算')
 
lb1 = Label(root, text='输出算式个数：')
lb1.place(relx=-0.1, rely=0.1, relwidth=0.8, relheight=0.1)
lb2 = Label(root, text='运算符个数：')
lb2.place(relx=-0.1, rely=0.25, relwidth=0.8, relheight=0.1)
lb3 = Label(root, text='输出列数为：')
lb3.place(relx=-0.1, rely=0.4, relwidth=0.8, relheight=0.1)
 
# 输入框
inp1 = Entry(root)
inp1.place(relx=0.6, rely=0.1, relwidth=0.3, relheight=0.1)
inp2 = Entry(root)
inp2.place(relx=0.6, rely=0.25, relwidth=0.3, relheight=0.1)
inp3 = Entry(root)
inp3.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)
 
# lambda调用 run()
btn1 = Button(root, text='打印', command=lambda:run(inp1.get(),inp2.get(),inp3.get()))
btn1.place(relx=0.3, rely=0.55, relwidth=0.3, relheight=0.1)
 
# 在窗体垂直自上而下位置70%处起，布局相对窗体高度40%高的文本框
txt = Text(root)
txt.place(rely=0.7, relheight=0.4)
 
root.mainloop()
