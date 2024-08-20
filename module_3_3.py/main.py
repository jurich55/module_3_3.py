def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list_2 = [54.32, 'Базар']
print_params(values_list_2, 45)
print_params(*values_list_2, 45)
print()
values_dict = {'a' : 15, 'b' : 'волна', 'c' : True}
print_params(values_dict)
print_params(*values_dict)
print_params(**values_dict)
