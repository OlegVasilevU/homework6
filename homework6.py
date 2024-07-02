# Практическое задание по теме: "Словари и множества"
my_dict = {'Oleg': 1990, 'Ekaterina': 1998, 'Maksim': 2017}
print(my_dict)
print(my_dict['Oleg'])
print(my_dict.get('Anastasia'))
my_dict.update({'Valeria': 2002, 'Pavel': 2000})
a = my_dict.pop('Ekaterina')
print(a)
print(my_dict)

my_set = {1, 2, 3, 2, 1, 3, 'Home', 'Room', 'Home', 'Bedroom', 'Room'}
print(my_set)
my_set.add('Kitchen')
my_set.add(4)
my_set.discard('Home')
print(my_set)