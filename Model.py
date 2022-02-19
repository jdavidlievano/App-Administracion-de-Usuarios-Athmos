import json
import time

data = {}
data['Usuarios_Creados'] = []

class Usuario():

    def __init__(self, nombres=None, apellidos=None, edad=None, email=None):
        self.nombres = nombres
        self.apellidos =apellidos
        self.edad = edad
        self.email =email

    def configurarUsuario(self):
        nombres = input("Ingrese los nombres del usuario:")
        apellidos = input("Ingrese los apellidos del usuario:")
        edad = int(input("Ingrese la edad del usuario:"))
        email = input("Ingrese el email del usuario:")

        self.crearUsuario(nombres, apellidos, edad, email)

    def mostrarUsuarios(self):
        return data['Usuarios_Creados']
    
    def crearUsuario(self, nombres, apellidos, edad, email):
        nuevo_usuario = Usuario(nombres=nombres, apellidos=apellidos,edad=edad,email=email)

        datos = {
            'Nombres': nuevo_usuario.nombres,
            'Apellidos': nuevo_usuario.apellidos,
            'Edad': nuevo_usuario.edad,
            'Email': nuevo_usuario.email
        }
        self.guardarUsuario(datos)
        print('\nEl usuario {} ha sido creado'.format(datos['Nombres']))

    def guardarUsuario(self, datos):
        data['Usuarios_Creados'].append(datos)
        usuarios = data['Usuarios_Creados']
        archivo = open('Usuarios.json', 'w')
        json.dump(usuarios, archivo, indent=4)

    def buscarUsuario(self, correo):
        datos = {}
        for key in data['Usuarios_Creados']:
            if correo.lower() == key['Email'].lower():
                datos = {
                    'Nombres': key['Nombres'],
                    'Apellidos': key['Apellidos'],
                    'Edad': key['Edad'],
                    'Email': key['Email']
                }
                return datos
        return datos
    
    def modificarUsuario(self, email, datos):
        datos_usuario = self.buscarUsuario(email)

        if not datos_usuario:
            print("No se ha encontrado el usuario con email {}".format(email))
        
        for key, value in datos.items():
            datos_usuario[key] = value

        self.eliminarUsuario(email)
        self.guardarUsuario(datos_usuario)

    def eliminarUsuario(self, email):
        if self.buscarUsuario(email):
            for key in data['Usuarios_Creados']:
                if email.lower() == key['Email'].lower():
                    data['Usuarios_Creados'].remove(key)
                    
                    usuarios = data['Usuarios_Creados']
                    archivo = open('Usuarios.json', 'w')
                    json.dump(usuarios, archivo, indent=4)
                    return True
        else:
            return False
            
    def cargarUsuarios(self):
        try:
            archivo = open('Usuarios.json')
            data['Usuarios_Creados'] = json.load(archivo)
        except FileNotFoundError:
            print("\nCreando registro de usuarios...")
            time.sleep(1)
            archivo = open('Usuarios.json', 'a+')
        except json.decoder.JSONDecodeError:
            print("\nNo hay usuarios, crea nuevos usuarios a partir de ahora")