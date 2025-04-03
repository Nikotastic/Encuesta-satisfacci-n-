
lista_usuarios={'david','nikol','leivis','luis','naydeth'}
usuario= input("Ingresa tu usuario: ")

coincidir= False
largo = 10

while len(usuario) > largo and coincidir==True:
    print("Usuario invalido, no puede exeder los 10 caracteres")
    usuario= input("Ingresa tu usuario: ")
    if usuario in lista_usuarios:
        contraseña= int(input("Ingresa tu contraseña: "))
    else:
        print("Usuario no existe en la base de datos")
        usuario= input("Ingresa tu usuario: ")

for numero in lista_usuarios:
    if numero==usuario:
        encontrado=True