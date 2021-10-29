while True:
    contraseña=int(input())
    if(contraseña==2002):
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
        


















"""

Entradas: un valor entero que va a ser nuesta contraseña
Contraseña --> int --> A 
Salidas: 2 cadenas de texto dependiendo si la contraseña es correcta o no
Correcta --> str --> B 
Incorreta --> str ---> C

# Entrada
A = int(input())

# Caja negra
while A != 2002:
    print("Senha Invalida") # Salida
    A = int(input())

# Salida
print("Acesso Permitido")
"""