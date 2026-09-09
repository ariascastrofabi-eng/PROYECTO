def menu_usuario():
    while True:
        print("==========MENU DE USUARIO=======")
        print("1.Ver informacion")
        print("2.Consultar datos")
        print("3.Realizar una operacion")
        print("4.Cerrar sesion")

        opcion1=input("INGRESA UN NUMERO CORRECTO(1-4): ").strip()
        match opcion1:
            case "1":
                print("ver")
            case "2":
                print("consultar")
            case "3":
                print("realizar")
            case "4":
                print("SALIENDO")
                break
            case _:
                print("no hay mas opciones")
        