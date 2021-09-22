import math
def mathf(x):
    try:
        if x == 0 or x == -1:
            print("Не знаю что тут должно быть")
        else:
            y = (1/math.sqrt(x)+math.cos(math.exp(x))+(math.cos(x) ** 2))/(((math.log(1+x) ** 2) + math.sqrt((math.exp(math.cos(x))) + (math.sin(3.14 *x ) ** 2)))**1/3)
            print(y)
    except:
        print("Error")

mathf(x = float(input("Введите X")))