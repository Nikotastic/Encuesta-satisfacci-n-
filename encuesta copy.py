
lista_usuarios={"david":12132,"nikol":14526,"leivis":145278,"luis":1234,"naydeth":198874}
usuario= input("Ingresa tu usuario: ")
largo = 10

while len(usuario) > largo:
    print("Usuario invalido, no puede exeder los 10 caracteres")
    usuario= input("Ingresa tu usuario: ")

while len(usuario) <= largo and usuario not in lista_usuarios:
    if usuario  not in lista_usuarios:
        print("Usuario no existe en la base de datos")
        usuario= input("Ingresa tu usuario: ")
        while len(usuario) > largo:
            print("Usuario invalido, no puede exeder los 10 caracteres")
            usuario= input("Ingresa tu usuario: ")
        
    else:
        while usuario not in lista_usuarios and contraseña != lista_usuarios[usuario]:
            contraseña= int(input("Ingresa tu contraseña: "))
            if contraseña == lista_usuarios[usuario]:
                print(f"Bienvenido {usuario}, favor realizar la siguiente encuesta")
            else:
                print("Usuario no existe en la base de datos")
                usuario= input("Ingresa tu usuario: ")
                contraseña= int(input("Ingresa tu contraseña: "))    
while len(usuario) <= largo and usuario not in lista_usuarios and contraseña!=lista_usuarios[usuario]:
    if usuario  not in lista_usuarios:
        print("Usuario no existe en la base de datos")
        usuario= input("Ingresa tu usuario: ")
    else:
        while usuario not in lista_usuarios and contraseña != lista_usuarios[usuario]:
            contraseña= int(input("Ingresa tu contraseña: "))
            if contraseña == lista_usuarios[usuario]:
                print(f"Bienvenido {usuario}, favor realizar la siguiente encuesta")
            else:
                print("Usuario no existe en la base de datos")
                usuario= input("Ingresa tu usuario: ")
                contraseña= int(input("Ingresa tu contraseña: "))
            if contraseña == lista_usuarios[usuario]:
                print(f"Bienvenido {usuario}, favor realizar la siguiente encuesta")

contraseña= int(input("Ingresa tu contraseña: "))
if contraseña==lista_usuarios[usuario]:
    print(f"Bienvenido {usuario}, favor realizar la siguiente encuesta")
else:
    while contraseña!=lista_usuarios[usuario]:
        print("Contraseña incorrecta")
        contraseña= int(input("Ingresa tu contraseña: "))
        if contraseña == lista_usuarios[usuario]:
            print(f"Bienvenido {usuario}, favor realizar la siguiente encuesta")

