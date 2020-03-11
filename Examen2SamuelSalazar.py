class usuario():
	def __init__(self,correo,contraseña,nombre,apellido):
		self.correo = correo
		self.contraseña = contraseña
		self.nombre = nombre
		self.apellido = apellido	
	def guardar(self):
		LogUsuarios = open('Registrados.txt','a')
		LogUsuarios.write(f'''Correo: {self.correo}
Contraseña: {self.contraseña}
Nombre: {self.nombre}
Apellido: {self.apellido}
''')
		LogUsuarios.close()
def ValidarUsuario(correo):
	LogUsuarios = open('Registrados.txt','a')
	LogUsuarios.close()
	LogUsuarios = open('Registrados.txt','r')
	Contenido = LogUsuarios.readlines()
	LogUsuarios.close()
	if correo == '':
		print('ERROR: Casilla vacia')
		return True
	for linea in Contenido:
		if linea == 'Correo: '+correo+'\n':
			print('ERROR: Correo ya existente')
			return True
	
salidaFinal= False
ValidarNumero = False
while salidaFinal == False:
	print('''Menu
1-Registrar nuevo usuario
2-Iniciar sesion
3-Salir''')
	opcion = input('Opcion: ')
	if opcion == '1':
		print('Ingrese "Salir" para salir al menu')
		correo = input('Correo: ')
		if ValidarUsuario(correo) == True or correo == 'Salir' or correo == 'salir':
			continue
		contraseña = input('Contraseña: ')
		if ValidarUsuario(correo) == True or contraseña == 'Salir' or contraseña == 'salir':
			continue
		nombre = input('Nombre: ')
		if ValidarUsuario(correo) == True or nombre =='Salir' or nombre == 'salir':
			continue
		apellido = input('Apellido: ')
		if ValidarUsuario(correo) == True or apellido == 'Salir' or apellido == 'salir':
			continue
		NuevoUsuario = usuario(correo,contraseña,nombre,apellido)
		NuevoUsuario.guardar()
		print('Usuario registrado!')
	elif opcion == '2':
		LogUsuarios = open('Registrados.txt','r')
		Contenido = LogUsuarios.readlines()
		LogUsuarios.close()
		correo = input('Ingrese su correo: ')
		if correo== 'admin':
			contraseña = input('Ingrese la contraseña: ')
			if contraseña == 'admin':
				LogUsuarios = open('Registrados.txt','r')
				print('Todos los usuarios registrados: ')
				print(LogUsuarios.read())
				LogUsuarios.close()
				continue
		for linea in Contenido:
			sesioninciada = False
			if linea == 'Correo: '+correo+'\n':
				contraseña = input('Ingrese la contraseña: ')
				for linea in Contenido:
					if linea == 'Contraseña: '+contraseña+'\n':
						salida = False
						sesioninciada = True
				if sesioninciada == True:
					print('Iniciaste sesion correctamente!')
					while salida == False:
						while ValidarNumero == False:
							print('-------------------CALCULADORA----------------')
							print('1-Sumar')
							print('2-Restar')
							print('3-Multiplicar')
							print('4-Dividir')				
							opcion2 = input('Opcion: ')
							try:
								num1 = int(input('Digite el primer numero: '))
								num2 = int(input('Digite el segundo numero: '))
								ValidarNumero = True
							except:
								print('necesita ingresar un numero amigo ; ) ')
						if opcion2 == '1':
							resultado = num1+num2
						elif opcion2 == '2':
							resultado = num1-num2
						elif opcion2== '3':
							resultado = num1*num2
						elif opcion2 == '4':
							try: 
								resultado = num1/num2
							except:
								print('Imposible dividir entre cero')
								ValidarNumero = False
								continue
						else:
							print('Opcion invalida')
						print('El resultado es: ',resultado)
						print('Desea cerra sesion? S/N')
						cerrar = input()
						if cerrar == 'S' or cerrar == 's':
							salida = True
							break
						elif cerrar == 'N' or cerrar == 'n':
							continue
	elif opcion == '3':
		break
	else:
		print('Opcion invalida')
