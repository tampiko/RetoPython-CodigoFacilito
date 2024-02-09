print('------------------------------ JUANMAN SOFTWARE ------------------------------')
print('')
# print('')
salir=False
usuarios=()
user={}

usuarios = usuarios + ({"nombre":"juan"},)

while salir==False:

    print('+----------------------------------- Menú -----------------------------------+')
    print('+----------------------------------------------------------------------------+')
    print('|  A.- Registrar nuevos usuario                                              |')
    print('|  B.- Listar usuarios                                                       |')
    print('|  C.- Consultar un usuario                                                  |')
    print('|  D.- Editar un usuario                                                     |')
    print('|  S.- Salir                                                                 |')
    print('+----------------------------------------------------------------------------+')

    menu = input('Elija una opción del menú: ')

    match menu:
        case 'A':
            print('')
            print('--------------------------- REGISTRAR NUEVO USUARIO --------------------------')
            nombre=input('Nombre del usuario: ')
            user['name']=nombre
            usuarios = usuarios + (user,)
            print('')
            print('')
        case 'B':
            print('')
            print('------------------------------- LISTAR USUARIOS ------------------------------')
            for i,usuario in enumerate(usuarios):
                print(str(i)+') '+usuario)
            print('')
            print('')
        case 'C':
            print('')
            print('---------------------------- CONSTULAR UN USUARIO ----------------------------')
            print('')
            print('')
        case 'D':
            print('')
            print('------------------------------ EDITAR UN USUARIO -----------------------------')
            print('')
            print('')
        case 'S':
            print('')
            print('------------------------------------ SALIR -----------------------------------')
            print('')
            print('')
            salir=True
        case _:
            print('*** OPCION NO VALIDA ')





# cuantos = int(input('Cuantos usuarios deseas ingresar? ')) 
# registros = 1
# listado = []
# while registros <= cuantos:
#     print('');
#     print('Registro del Usuario ' + str(registros))
#     print('');
#     name_valid = False
#     while(name_valid == False):
#         name        = input('Nombre: ')
#         name_length = 0
#         for i in name:
#             name_length += 1
#         if(name_length < 5 or name_length > 50):
#             print('*** NOMBRE NO VÁLIDO | El nombre debe tener mínimo 5 caracteres, pero no mas de 50 ***')
#             print('')
#         elif (name_length >= 5 and name_length <= 50):
#             name_valid=True
#     ap_valid = False;
#     while(ap_valid == False):
#         ap          = input('Apellidos: ')
#         ap_length   = 0
#         for i in ap:
#             ap_length += 1
#         if(ap_length < 5 or ap_length > 50):
#             print('*** APELLIDO NO VÁLIDO | El apellido debe tener mínimo 5 caracteres, pero no mas de 50 ***')
#             print('')
#         elif (ap_length >= 5 and ap_length <= 50):
#             ap_valid = True
#     mail_valid = False
#     while(mail_valid == False):
#         mail        = input('Correo Electrónico: ')
#         mail_length = 0
#         for i in mail:
#             mail_length += 1
        
#         if(mail_length < 5 or mail_length > 50):
#             print('*** CORREO NO VÁLIDO | El correo debe tener mínimo 5 caracteres, pero no mas de 50 ***')
#             print('');
#         elif (mail_length >= 5 and mail_length <= 50):
#             mail_valid = True
#     phone_valid = False
#     while(phone_valid == False):
#         phone = input('Teléfono: ')
#         phone_length = 0
#         for i in phone:
#             phone_length += 1
#         if(phone_length!=10):
#             print('*** TELÉFONO NO VALIDO | El teléfono debe ser de 10 caracteres, favor de omitir paréntesis, guiones u otros caracteres.')
#             print('');
#         elif (phone_length==10):
#             phone_valid = True
#     listado.append(str(registros)+'.- Nombre: '+ name +' '+ ap +', Correo: '+ mail +', Teléfono: '+ phone +'.')
#     registros += 1
#     print('')
#     print('Bienvenido '+ name +' '+ ap +', en breve recibirás un correo en '+ mail +', y un mensaje al teléfono '+ phone +' para confirmar tu registro.');
#     print('')
#     print('Listado de Registros')
#     for reg in listado:
#         print(reg)
# print('eof.')