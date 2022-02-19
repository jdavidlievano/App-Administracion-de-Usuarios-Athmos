import os
import time
import View
from Model import Usuario


def iniciar():
    os.system("cls")
    Usuario().cargarUsuarios()
    while True:
        View.interfaz()

        opcion = input(">")
        if opcion == '1':
            Usuario().configurarUsuario()

        elif opcion == '2':
            datos = Usuario().mostrarUsuarios()
            if datos == []:
                print("\nNo se encuentran usuarios registrados")
            View.mostrarListaUsuariosVista(datos)
        elif opcion == '3':
            email = input("Ingrese el email del usuario a buscar:")
            datos = Usuario().buscarUsuario(email)
            if datos == {}:
                print("\nNo se encuentra el usuario con el email {} ".format(email))
            else:
                View.mostrarUsuarioVista(datos)
        elif opcion == '4':
            email = input("Ingrese el email del usuario a modificar:")
            datos = Usuario().buscarUsuario(email)

            if datos != {}:
                nombre = input("Desea modificar el nombre? Marque S para Sí o de Enter para No: ").upper()
                if nombre == 'S':
                    valor_nombre = input("Ingrese el nuevo nombre:")
                    datos['Nombres'] = valor_nombre
                # else:
                #     continue
                
                apellido = input("Desea modificar el apellido? Marque S para Sí o de Enter para No: ").upper()
                if apellido == 'S':
                    valor_apellido = input("Ingrese el nuevo apellido:")
                    datos['Apellidos'] = valor_apellido
                # else:
                #     continue

                edad = input("Desea modificar la edad? Marque S para Sí o de Enter para No: ").upper()
                if edad == 'S':
                    valor_edad = input("Ingrese el nuevo nombre:")
                    datos['Edad'] = valor_edad
                # else:
                #     continue
                
                Usuario().modificarUsuario(email, datos)
                print("\nEl usuario con email {} fue modificado exitosamente".format(email))
            else:
                print("\nNo ingresó ningún email para modificar")
        elif opcion == '5':
            email = input("Ingrese el email del usuario a eliminar:")
            if Usuario().eliminarUsuario(email):
                print("\nEl usuario con email {} ha sido eliminado".format(email))
            else:
                print("\nEl usuario con email {} no existe".format(email))

        elif opcion == '6':
            print("\nGracias por usar el programa")
            time.sleep(2)
            quit()
        else:
            print("\nHas introducido un comando inválido")

if __name__ == "__main__":
    iniciar()
