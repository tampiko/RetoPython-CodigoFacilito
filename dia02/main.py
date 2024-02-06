print('--------------------------------------------------------------------------')
print('--------------------------------------------------------------------------')
print('Bienvenido!')
print('')
cuantos = int(input('Cuantos usuarios deseas ingresar? '))
registros = 1

while registros <= cuantos:
    print('');
    print('Registro del Usuario ' + str(registros))
    print('');
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
        
    registros += 1
    print('')
    print('Bienvenido '+ name +' '+ ap +', en breve recibirás un correo en '+ mail +', y un mensaje al teléfono '+ phone +' para confirmar tu registro.');
    print('')
print('eof.')