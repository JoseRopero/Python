# Podemos declarar una variable con un tipo de datos para después más adelante usarla.

age: int
# age = 'twelve'  Nos daria error
age: 12

name: str
height: float
is_human: bool


# También podemos especificar el tipo de datos en una función y el tipo de retorno.

def police_check(edad: int) -> bool:
    if edad > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You can pass")
else:
    print("Pay a fine")
