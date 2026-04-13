py函数作业
1.编写一个函数，实现功能：接受用户输入一个字符串，输出字符串中的英文字母、空格、数字和其他字符的个数。要求编写完函数，调用函数产生结果

def count_characters(s):
    letters = 0
    spaces = 0
    digits = 0
    others = 0

    for ch in s:
        if ch.isalpha() and ch.isascii():
            letters += 1
        elif ch.isspace():
            spaces += 1
        elif ch.isdigit():
            digits += 1
        else:
            others += 1

    print("英文字母个数：", letters)
    print("空格个数：", spaces)
    print("数字个数：", digits)
    print("其他字符个数：", others)

2.编写一个函数，实现功能：接受用户输入一个字符串，输出字符串中的英文字母、空格、数字和其他字符的个数。要求编写完函数，调用函数产生结果
def sum_and_product(n):
    total_sum = 0
    total_product = 1
    for i in range(1, n + 1):
        total_sum += i
        total_product *= i
    print("1+2+...+n 的结果：", total_sum)
    print("1*2*...*n 的结果：", total_product)


n = int(input("请输入一个整数n："))
sum_and_product(n)

3.编写一个函数，实现功能：用户输入三个数，输出最大值和最小值。要求编写完函数，调用函数产生结果，将代码和运行结果截图
def max_and_min_of_three(a, b, c):
    max_value = max(a, b, c)
    min_value = min(a, b, c)
    print("最大值：", max_value)
    print("最小值：", min_value)


a, b, c = map(float, input("请输入三个数（用空格分隔）：").split())
max_and_min_of_three(a, b, c)
