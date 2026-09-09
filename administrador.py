def menu_administrador():
    while True:
        print("==========MENU DE ADMINISTRADOR=======")
        print("1.Registrar usuario")
        print("2.Mostrar usuario")
        print("3.Buscar usuario")
        print("4.Modificar usuario")
        print("5.Eliminar usuario")
        print("6.Cerrar sesion")

        opcion=input("INGRESA UN NUMERO CORRECTO(1-6): ").strip()
        match opcion:
            case "1":
                from funciones import registrar_usuario
                print("Registrar")
                registrar_usuario()
            case "2":
                from funciones import mostrar_usuarios
                print("Mostrar")
                mostrar_usuarios()
            case "3":
                from funciones import buscar_usuarios
                print("Buscar")
                buscar_usuarios()
            case "4":
                from funciones import modificar_usuarios
                print("Modificar")
                modificar_usuarios()
            case "5":
                from funciones import eliminar_usuario
                print("Eliminar")
                eliminar_usuario()
            case "6":
                print("SALIENDO")
                break
            case _:
                print("no hay mas opciones")
        