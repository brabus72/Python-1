# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5

equation_split = equation.split()
num_x = float(equation_split[2].replace('x', '')) * x
y = num_x + float(equation_split[4])

print(y)
