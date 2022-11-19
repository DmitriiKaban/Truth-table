def my_func(expr, nums, arr_variables):
    for x in range(0, len(arr_variables)):
        expr = expr.replace(arr_variables[x], nums[x])
    expr = expr.replace("*", " and ").replace("+", " or ").replace("!", " not ")
    if eval(expr) == 1 or eval(expr) == "true":
        return "True"
    else:
        return "False"


# =========================MAIN=========================
expression = input()

count_variables = 0
array_of_variables = []
for i in range(len(expression)):
    if expression[i].isalpha() and not (expression[i] in array_of_variables):
        array_of_variables.append(expression[i])


binary_array = []
for x in range(pow(2, len(array_of_variables))):  # creates binary numbers, with the length of number of input elements
    binary_array.append(bin(x)[2:].zfill(len(array_of_variables)))

for x in array_of_variables:
    print(x + " | ", end='')
print("RESULT")

for values in binary_array:
    for x in values:
        print(x + " | ", end='')
    print(my_func(expression, values, array_of_variables))
