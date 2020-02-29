class Auto():
	def __init__(self,modelo):
		self.encendido = False
		self.abierto = False
		self.modelo = modelo
		self.manejando= False
	def EncenderAuto(self):
		if self.abierto == False:
			print('El',self.modelo,'esta cerrado!')
		elif self.abierto == True:
			if self.encendido == False:
				print('El',self.modelo,'esta apagado')
				print('Encendiendo........')
				self.encendido= True
				print('Encendido')
			else:
				print('El',self.modelo,'ya esta encendido!')
	def AbrirAuto(self):
		if self.abierto == False:
			print('Abriendo',self.modelo,'.....')
			self.abierto = True
			print('Abierto!')
		else:
			print('El',self.modelo,'ya esta abierto')
	def Manejar(self):
		if self.encendido == True and self.abierto == True:
			print('Tenga un buen viaje!')
			self.manejando = True
		elif self.abierto == False:
			print('El auto esta cerrado!')
		elif self.abierto == True and self.encendido == False:
			print('El auto esta apagado!')
Carros = list()
SalidaFinal= False
contador = 0
NoEncontrado = False
while SalidaFinal == False:
	Salida = False
	print('Vamos a manejar!')
	print('')
	if Carros != []:
		print('Lista de autos:')
		for modelos in Carros:
			contador += 1
			print('')
			print('Auto numero',contador,':',modelos.modelo)
			print('')
		print('''Escriba el nombre del auto que quiere 
o escriba un nuevo nombre para agregarlo

''')			
		seleccion = input()
		if seleccion != MiCarroPuntoCom.modelo:
			if 	MiCarroPuntoCom.abierto == True and MiCarroPuntoCom.encendido == False:
				print('Saliste de tu otro auto! Ahora tu '+MiCarroPuntoCom.modelo+' esta cerrado')
			elif MiCarroPuntoCom.encendido == True:
				print('Saliste de tu otro auto! Ahora tu '+MiCarroPuntoCom.modelo+' esta apagado y cerrado')
			else :
				print('Te alejaste de tu'+MiCarroPuntoCom.modelo)
			MiCarroPuntoCom.encendido = False
			MiCarroPuntoCom.manejando = False
			MiCarroPuntoCom.abierto = False
		for modelos in Carros:
			if seleccion == modelos.modelo:
				MiCarroPuntoCom = modelos
				contador= 0
				NoEncontrado = False
				break
			else:
				NoEncontrado= True
	
	elif Carros == []:
		print('Ingrese que auto desea manejar')
		print('')
		Carrito = input()
		print('')
		MiCarroPuntoCom = Auto(Carrito)
		Carros.append(MiCarroPuntoCom)
	if NoEncontrado == True:
		print('')
		MiCarroPuntoCom = Auto(seleccion)
		Carros.append(MiCarroPuntoCom)
		print('Modelo Agragado!!')
		print('')
		contador = 0
	print('Que hacer con tu',MiCarroPuntoCom.modelo,'?')
	while Salida== False:
		print('''
1-Abrirlo
2-Encenderlo
3-Manejarlo
4-Olvidalo, ya no quiero manejar este auto
			
		''')
		opcion = input()
		print('')
		if opcion == '1':
			MiCarroPuntoCom.AbrirAuto()
		elif opcion == '2':
			MiCarroPuntoCom.EncenderAuto()
		elif opcion =='3':
			MiCarroPuntoCom.Manejar()
			if MiCarroPuntoCom.manejando == True:
				print('''Bruuum bruum Manejando.......
......
......
......''')
				print('Ya manejaste! quiere manejar otra vez? S/N')
				Final = input()
				if Final == 'n' or Final == 'N':
					Salida = True
					SalidaFinal = True
				elif Final == 's' or Final == 'S':
					Salida = True
				else:
					print('Ingrese S o N para confirmar!')
		elif opcion == '4':
			print('Entendido!')
			Salida= True
			print('')
		else: 
			print('Seleccione una opcion valida')	
		
		
		
