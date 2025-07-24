# made by the one and only eyad
print('tool_TTJ %%% Tool Text To JSON')

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
exp = input("Enter expression: ")

json = f'{{"n1": {n1}, "n2": {n2}, "exp": "{exp}" }}'
print("Copy and paste this code into Node_RED:")
print(json)
