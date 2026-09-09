
def menu_usuario(usuario):
    while True:
        print(f"==========MENU DE USUARIO=======")
        print("1.Ver informacion")
        print("2.Consultar datos")
        print("3.Realizar una operacion")
        print("4.Cerrar sesion")
        try:
            opcion1=int(input("INGRESA UN NUMERO CORRECTO(1-4): "))
            match opcion1:
                case 1:
                    from funciones import ver_usuarios_nomas
                    print("ver")
                    ver_usuarios_nomas()
                case 2:
                    from funciones import consultar_dato
                    print("consultar")
                    consultar_dato(usuario)
                case 3:
                    from funciones import operaciones
                    print("realizar")
                    operaciones()
                case 4:
                    print("SALIENDO")
                    break
                case _:
                    print("no hay mas opciones")
        except ValueError:
            print("no se puede decimal ni letras")
        