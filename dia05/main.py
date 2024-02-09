import os

salir = False
usuarios = ()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def titulo(texto):
    if texto != '':
        espacios = (80-(len(texto)+2)) // 2
        entera   = (80-(len(texto)+2)) % 2
    else:
        espacios = 40
        entera   = 0
    cadena  = ''
    cadena2 = ''
    for i in range(1,espacios):
        cadena = cadena + '-'
    if(entera == 1):
        cadena2 = cadena + '-'
    else:
        cadena2 = cadena
    if texto != '':
        print(str(cadena)+' '+str(texto)+' '+str(cadena2))
    else:
        print(str(cadena)+''+str(texto)+''+str(cadena2))


def elementoMenu(texto):
    espacios = (80 - len(texto)) - 5
    cadena = ''
    for i in range(1,espacios):
        cadena = cadena + ' '

    txt = '|  ' + texto + cadena + '|'
    print(txt)


def show_menu():
    saludo()
    titulo('MENU')
    titulo('')
    elementoMenu('L.- Listar usuarios')
    elementoMenu('R.- Registrar nuevo usuario')
    elementoMenu('C.- Consultar un usuario')
    elementoMenu('E.- Editar un usuario')
    elementoMenu('B.- Borrar un usuario')
    elementoMenu('S.- Salir')
    titulo('')
    menu = input('Elija una opción del menú: ').upper()
    return menu
    

def new_user():
    global usuarios
    saludo()
    titulo('REGISTRAR NUEVO USUARIO')
    user_data = data_request()
    usuarios  = usuarios + (user_data,)
    saludo()
    titulo('USUARIO REGISTRADO')
    list_users()
    input('Presione ENTER para continuar...')


def show_user():
    global usuarios
    id = getIdUsuario('CONSULTAR UN USUARIO')
    saludo()
    print('')
    print('Nombre Completo: '+usuarios[id]['nombre']+' '+usuarios[id]['ap'])
    print('         Correo: '+usuarios[id]['correo'])
    print('       Teléfono: '+usuarios[id]['telefono'])
    print('')
    print('')
    input('Presione ENTER para continuar...')


def edit_user():
    global usuarios
    id = getIdUsuario('EDITAR UN USUARIO')
    user_data = data_request()
    usuarios  = usuarios[:id] + (user_data,) + usuarios[id+1:]   
    saludo()
    titulo('USUARIO ACTUALIZADO')
    print('')
    input('Presione ENTER para continuar...')


def delete_user():
    global usuarios 
    id = getIdUsuario('ELIMINAR UN USUARIO')
    usuarios = usuarios[:id] + usuarios[id+1:]
    saludo()
    titulo('USUARIO ELIMINADO')
    print('')
    input('Presione ENTER para continuar...')


def list_users():
    global usuarios
    saludo()
    titulo('LISTA DE USUARIOS')
    print('')
    for index, usuario in enumerate(usuarios):
        print(str(index)+')'+' '+usuario['nombre']+' '+usuario['ap']+' | '+usuario['correo']+' | '+usuario['telefono'])
    print('')
    print('')
    

def end():
    print('')
    clear()
    print('------------------------------------- EOF ------------------------------------')
    print('')
    print('')


def welcome():
    clear()
    titulo("RETO PYTHON")
    titulo("JUANMAN")
    print('')


def data_request():
    name_valid = False
    while(name_valid == False):
        name        = input('Nombre: ')
        name_length = 0
        for i in name:
            name_length += 1
        if(name_length < 5 or name_length > 50):
            print('*** NOMBRE NO VÁLIDO | El nombre debe tener mínimo 5 caracteres, pero no mas de 50 ***')
            print('')
        elif (name_length >= 5 and name_length <= 50):
            name_valid=True
    ap_valid = False;
    while(ap_valid == False):
        ap          = input('Apellidos: ')
        ap_length   = 0
        for i in ap:
            ap_length += 1
        if(ap_length < 5 or ap_length > 50):
            print('*** APELLIDO NO VÁLIDO | El apellido debe tener mínimo 5 caracteres, pero no mas de 50 ***')
            print('')
        elif (ap_length >= 5 and ap_length <= 50):
            ap_valid = True
    mail_valid = False
    while(mail_valid == False):
        mail        = input('Correo Electrónico: ')
        mail_length = 0
        for i in mail:
            mail_length += 1
        
        if(mail_length < 5 or mail_length > 50):
            print('*** CORREO NO VÁLIDO | El correo debe tener mínimo 5 caracteres, pero no mas de 50 ***')
            print('');
        elif (mail_length >= 5 and mail_length <= 50):
            mail_valid = True
    phone_valid = False
    while(phone_valid == False):
        phone = input('Teléfono: ')
        phone_length = 0
        for i in phone:
            phone_length += 1
        if(phone_length!=10):
            print('*** TELÉFONO NO VALIDO | El teléfono debe ser de 10 caracteres, favor de omitir paréntesis, guiones u otros caracteres.')
            print('');
        elif (phone_length==10):
            phone_valid = True
            user={"nombre":name,"ap":ap,"correo":mail,"telefono":phone}
            return user;


def getIdUsuario(texto):
    valid_id = False
    while valid_id == False:
        saludo()
        titulo(texto)
        list_users()
        id = int(input('Indique el ID del usuario: '))
        if(id >= len(usuarios)):
            clear()
            print('*** ERROR! | Ese ID de usuario '+str(id)+ ' NO existe.')
            print('')
        else:
            valid_id = True
    return int(id);


def saludo():
    clear()
    welcome()

saludo()
while salir == False:
    menu = show_menu()
    match menu:
        case 'R':
            new_user()
        case 'L':
            list_users()
            input('Presione ENTER para continuar...')
        case 'C':
            show_user()
        case 'E':
            edit_user()
        case 'S':
            salir=True
            end()
        case 'B':
            delete_user()
        case _:
            print('*** OPCION NO VALIDA ')

