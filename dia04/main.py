import os

def clear():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Unix/Linux/MacOS
        os.system('clear')

clear()
print('------------------------------ JUANMAN SOFTWARE ------------------------------')
print('')
salir=False
usuarios=()
while salir==False:
    print('+----------------------------------- Menú -----------------------------------+')
    print('+----------------------------------------------------------------------------+')
    print('|  R.- Registrar nuevo usuario                                               |')
    print('|  L.- Listar usuarios                                                       |')
    print('|  C.- Consultar un usuario                                                  |')
    print('|  E.- Editar un usuario                                                     |')
    print('|  S.- Salir                                                                 |')
    print('+----------------------------------------------------------------------------+')
    menu = input('Elija una opción del menú: ').upper()
    clear()
    match menu:
        case 'R':
            print('')
            print('--------------------------- REGISTRAR NUEVO USUARIO --------------------------')
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
                    usuarios = usuarios + (user,)   
            print('')
            print('')
        case 'L':
            print('')
            print('------------------------------- LISTA DE USUARIOS ----------------------------')
            print('')
            for index, usuario in enumerate(usuarios):
                print(str(index)+')'+' '+usuario['nombre']+' '+usuario['ap']+' | '+usuario['correo']+' | '+usuario['telefono'])
            print('')
            print('')
            input('Presione ENTER para continuar...')
        case 'C':
            print('')
            print('---------------------------- CONSTULAR UN USUARIO ----------------------------')
            valid_id=False
            while valid_id==False:
                id = input('Indique el ID del usuario a consultar (X para regresar al menú): ')
                if(id=='X'):
                    valid_id=True
                else:
                    id=int(id)
                    if(id>=len(usuarios)):
                        clear()
                        print('*** ERROR! | Ese ID de usuario '+str(id)+ ' NO existe.')
                        print('')
                    else:
                        valid_id=True
                        print('')
                        print('Nombre Completo: '+usuarios[id]['nombre']+' '+usuarios[id]['ap'])
                        print('         Correo: '+usuarios[id]['correo'])
                        print('       Teléfono: '+usuarios[id]['telefono'])
                        print('')
                        print('')
                        input('Presione ENTER para continuar...')
        case 'E':
            print('')
            print('------------------------------ EDITAR UN USUARIO -----------------------------')
            valid_id=False
            while valid_id==False:
                id = input('Indique el ID del usuario a editar (X para regresar al menú): ')
                if(id=='X'):
                    valid_id=True
                else:
                    id=int(id)
                    if(id>=len(usuarios)):
                        clear()
                        print('*** ERROR! | Ese ID de usuario '+str(id)+ ' NO existe.')
                        print('')
                    else:
                        valid_id=True
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
                                usuarios = usuarios[:id] + (user,) + usuarios[id+1:]   
            print('')
            print('')
        case 'S':
            print('')
            clear()
            print('------------------------------------ SALIR -----------------------------------')
            print('')
            print('')
            salir=True
        case _:
            print('*** OPCION NO VALIDA ')