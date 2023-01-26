# List Comprehension
# new_list = [new_item for item in list]
import random

# Una lista de numeros y creamos otra lista incrementando cada valor.
# Forma normal:
numbers = [1, 2, 3]
new_list = []
for num in numbers:
    num += 1
    new_list.append(num)
print(f"Forma normal: {new_list}")

# List Comprehension
new_list2 = [n + 1 for n in numbers]
print(f"List Comprehension: {new_list2}")

# No solo se usan para trabajar con listas:
name = "Jose"
new_list3 = [letra for letra in name]
print(new_list3)

# Crear una lista con un rango donde cada valor sea el doble:
new_list4 = [x * 2 for x in range(1, 5)]
print(new_list4)

# Conditional list comprehension:
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

# Asigna una puntuación aleatoria a cada estudiante y almacena en un diccionario.
names2 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Jose", "Mercedes"]
students_score = {name: random.randint(1, 100) for name in names2}
print(students_score)

# Crea un diccionario con los estudiantes con nota >= a 60.
passed_students = {students: score for (students, score) in students_score.items() if score >= 60}
print(passed_students)
