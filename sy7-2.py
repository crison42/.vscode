import random
import math
from statistics import variance


def intxt():
    f1 = open(
        "sjs.txt",
        "w",
    )
    for i in range(20):
        i = random.randint(1, 100)
        string = str(i)
        f1.write(string)
        f1.write("\n")
    f1.close()


def fc():
    f2 = open("sjs.txt", "r+")
    lines = f2.read()
    lines = lines.split()
    sum = 0.0
    num = 0
    for i in lines:
        sum = sum + int(i)
    average = sum / 20.0
    for j in lines:
        num = num+(int(j) - average)**2
    FC = math.sqrt(num/20)
    f2.write(str(FC))
    f2.close()


intxt()
fc()
