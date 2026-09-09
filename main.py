from funciones import validador_sistema
def main():
    usuario=input("INGRESA EL USUARIO CORRECTO: ").strip()
    contraseña=input("INGRESA LA CONTRASEÑA CORRECTA: ").strip()
    validador_sistema(usuario,contraseña)
main()