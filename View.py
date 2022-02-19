
def interfaz():
    
    print("""\n*** Bienvenido al administrador de Usuarios ***\n
    ¿Qué deseas hacer?\n
    1)Crear un usuario
    2) Ver los usuarios creados
    3) Buscar Usuario
    4) Modificar usuario
    5) Eliminar usuario
    6) Salir del programa\n """)

def mostrarListaUsuariosVista(datos):
    for usuario in datos:
        print("""
    Nombres: {}
    Apellidos: {}
    Edad: {}
    Email: {}
            """.format(usuario['Nombres'], usuario['Apellidos'], usuario['Edad'], usuario['Email']))

def mostrarUsuarioVista(usuario):
    print("""
    Nombres: {}
    Apellidos: {}
    Edad: {}
    Email: {}
            """.format(usuario['Nombres'], usuario['Apellidos'], usuario['Edad'], usuario['Email']))