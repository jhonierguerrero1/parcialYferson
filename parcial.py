import mysql.connector
print('Iniciando')
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='parcial1',
    port=3306
)
menuprincipal= int(input("menu principal: \n 1- INICIAR SESION \n 2- REGISTRARSE"))

while menuprincipal != 0:
    if menuprincipal == 1: 
        print("_INICIAR SESION_")
        email=input("INGRESE SU EMAIL: ")
        contraseña=input("INGRESE SU CONTRASEÑA: ")

        cursor =db.cursor()
        cursor.execute('select nombre from usuario where email = "'+ email+'" and contraseña = "'+contraseña+'"' )
        usuario = cursor.fetchall()
        

        if len(usuario) > 0 :
            print("INICIO DE SESION EXITOSO ")
            print(usuario)
            menuprincipal= int(input("menu principal: \n 1- INICIAR SESION \n 2- REGISTRARSE"))
            
              

        else :
            print("CREDENCIALES INCORRECTAS")
            menuprincipal= int(input("menu principal: \n 1- INICIAR SESION \n 2- REGISTRARSE"))
            


    elif menuprincipal == 2: 
        print("_REGISTRARSE_")

        nombree=input("ingrese el nombre")
        correoo=input("ingrese un correo")
        contraseñaaa=input("Ingrese una contraseña, minimo 8 caracteres")

        def crearUsuario(nombre,email,contraseña):
            cursor=db.cursor()
            cursor.execute('''
                insert into usuario(nombre,email,contraseña)
                values (%s,%s,%s)''',
                (nombre,
                email,
                contraseña))

            db.commit()
            cursor.close()
        crearUsuario(nombree,correoo,contraseñaaa)
        print("registrado")

    else:
        print("por favor digita una opcion correcta")
    
    menuprincipal= int(input("menu principal: \n 1- INICIAR SESION \n 2- REGISTRARSE " ))