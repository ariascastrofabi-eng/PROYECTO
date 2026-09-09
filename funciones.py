from usuario import menu_usuario
from administrador import menu_administrador
usuarios=["fabian","sebas","kevin"]
contraseñas_nuevas=["1234","1235","ajajja"]
def validador_sistema(usuario,contraseña):

    if usuario == "ARIAS" and contraseña == "63":
        print(f"ACCESO CONDEDIO DE ADMINISTRADOR: {usuario}")
        menu_administrador()
    elif usuario in usuarios and contraseña in contraseñas_nuevas:
        i=0
        while i <= len(usuarios):
            if usuarios[i] == usuario and contraseñas_nuevas[i] == contraseña:
                print("ACCESO CONCEDIDO")
                menu_usuario()
                return True
            i+=1
        print("ACCESO DENEGADO")
        return False   
    else:
        print("ACCESO DENEGADO")

def registrar_usuario():
    usuario_nuevo=input("INGRESA TU USUARIO NUEVO: ").strip()
    contraseñas_nuevo=input("INGRESA TU CONTRASEÑA NUEVO: ").strip()

    if len(usuario_nuevo) == 0:
        print("no debe ver nada")
    elif usuario_nuevo in usuarios:
        print("no repetir nombres")
    else:
        usuarios.append(usuario_nuevo)
        contraseñas_nuevas.append(contraseñas_nuevo)
        print("CREADO EXITOSAMENTE")

def mostrar_usuarios():
    for i,j in zip(usuarios,contraseñas_nuevas):
        print(f"USUARIOS: {i} y su contraseña es {j}")

def buscar_usuarios():
    nombre_usuario=input("INGRESA EL NOMBRE DE USUARIO A BUSCAR: ").strip()
    i=0
    while i < len(usuarios):
        if nombre_usuario == usuarios[i]:
            print("=========ENCONTRADO USUARIO=======")
            print(f"USUARIO:{usuarios[i]} y su contraseña es {contraseñas_nuevas[i]} ")
            return True
        i+=1
    else:
        print("NO SE ENCONTRO EL USUARIO")
        return False

def modificar_usuarios():

    usuario_a_modificar=input("INGRESA EL NOMBRE DE USUARIO QUE QUIERE MODIFICAR: ").strip()
    if usuario_a_modificar in usuarios:
        for i in range(len(usuarios)):
            if usuario_a_modificar == usuarios[i]:
                usuario_modificado=input("INGRESA UN USUARIO MODIFICADO QUE QUIERES: ").strip()
                contraseña_modificada=input("INGRESA LA CONTRASEÑA A MODIFICAR: ").strip()
                usuarios[i] = usuario_modificado
                contraseñas_nuevas[i] = contraseña_modificada
                print("==========CAMBIADO CON EXITO==========")
    else:
        print("NO EXISTE ESE USUARIO PARA MODIFICARLO")

def eliminar_usuario():

    usuario_eliminar=input("INGRESA EL NOMBRE DE USUARIO A ELIMINAR: ").strip()

    if usuario_eliminar in usuarios:
        i=usuarios.index(usuario_eliminar)
        usuarios.pop(i)
        contraseñas_nuevas.remove(contraseñas_nuevas[i])
    else:
        print("NO HAY ESE USUARIO PARA ELIMINAR")