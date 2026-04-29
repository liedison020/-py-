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

4. 编写一个函数prime_num(rg)，找出0~rg范围内的素数，并统计一共有多少个素数。

def prime_num(rg):
    primes = []

    for num in range(2, rg + 1):
        is_prime = True
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    print(f"0~{rg} 范围内的素数：", primes)
    print("素数个数：", len(primes))


rg = int(input("请输入rg（找出0~rg的素数）："))
prime_num(rg)


5. 自定义Person类，描述姓名、年龄、性别、专业和学时。

class Person:
    major = "计算机"
    __hours = 64

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

    def play_game(self):
        print(self.name, self.age, self.__gender, "在宿舍玩游戏")

    def __study(self):
        print(self.name, self.age, self.__gender, "在宿舍学习")


person1 = Person("张三", 18, "男")
person2 = Person("李四", 19, "女")

person1.play_game()
person2.play_game()


6. 创建test.txt写入100行内容，再读取文件并用异常处理确保关闭文件。

file = open("test.txt", "w", encoding="utf-8")
for i in range(100):
    file.write("I love python\n")
file.close()

file = None
try:
    file = open("test.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("文件不存在，读取失败。")
finally:
    if file is not None:
        file.close()
    print("文件已关闭。")


# 7. 创建User类，打印用户信息摘要并进行个性化问候。

class User:
    def __init__(self, first_name, last_name, age, city, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        print("用户信息摘要：")
        print("姓名：", self.first_name + self.last_name)
        print("年龄：", self.age)
        print("城市：", self.city)
        print("邮箱：", self.email)

    def greet_user(self):
        print("你好，" + self.first_name + self.last_name + "，欢迎回来！")


user1 = User("张", "三", 18, "北京", "zhangsan@example.com")
user2 = User("李", "四", 20, "上海", "lisi@example.com")
user3 = User("王", "五", 19, "广州", "wangwu@example.com")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

