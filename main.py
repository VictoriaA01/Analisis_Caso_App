UsuContraseñas = []

try: 
    with open("Contraseñas.txt","r")as file:for line in file: 
        contraseñas.append(line)
 except: 
     print("")       


class Boveda_De_Contraseñas(object);
def_init_(selft,datos,usuario,consulta,credenciales, registro):
  self.datos = datos 
  self.usuario = usuario 
  self.consulta = consulta 
  self.credenciales = credenciales 
  self. registro = registro 
def Ingresardatos(selft): 
    UsuarioApp = selft.datos +""+selft.consulta +"" + str (self.credenciales)
    return datos
def ingresaUsuario(): 
    print("")
    print("USUARIO DE APP")
    usuario = input("Ingrese el usuario de App")
    objUsuario = Contraseñas(usuario)
def ConsultaTxt(): 
    print("")
    print("CONSULTA DE TXT")
    consulta = input("¿Es correcto?")
    objtUsuario = Contraseñas(consulta)
def ConsultaCredenciales(): 
    print("")
    print("CONSULTA DE CREDENCIALES")
    credenciales = input("Ingresa tus credenciales")
    objtUsuario = Contraseñas(credenciales)
def RegistroArchivo(): 
    print("REGISTRO DE ARCHIVO")
    registro= input("Deseas eliminar el registro de archivo")
    objtUsuario = Contraseñas(registro
def Salir(): 
    print("")
    print ("Saliendo del programa")
    print("")
    exit()
()
