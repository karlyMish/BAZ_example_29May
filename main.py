# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# Crear una lista en la que cuentes las veces que aparece cada nombre en 'dogs'
# Imprime la cantidad de perros que se llaman 'Rocky' y 'Sparky'
# Imprime la lista con los diferentes nombres de perros (Evadir los iguales)

# Utilizar funciones, de manera entera para contabilidad, keys , count
# Recorrer la colección de los datos con un for
# SE necesita instancia
# Podemos usar contatenación,

from collections import defaultdict

dogs = ['Sparky', 'Hunter', 'Loki', 'Sparky', 'Rocky', 'Toby', 'Rocky', 'Sparky', 'Sparky']

dog_dict = defaultdict(int)
for dog in dogs:
    dog_dict[dog] += 1

print('Rocky->', dog_dict['Rocky'])
print('Rocky->', dog_dict['Sparky'])
print(list(dog_dict.keys()))
#Comment