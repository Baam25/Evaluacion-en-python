from os import system
class paciente():
	def __init__(self,nombre,apellido,nacimiento,pais,genero,edad,ide):
		self.nombre = nombre
		self.apellido = apellido
		self.nacimiento = nacimiento
		self.pais = pais
		self.edad = edad
		self.ide = ide
		if genero == "1":
			self.genero = "Masculino"
		elif genero == "2":
			self.genero = "Femenino"
		self.estatus = "Sospechoso"
	def mostrar(self):
		return f"""\nGenero: {self.genero}
Nombre: {self.nombre}
Apellido: {self.apellido}
Fecha de Nacimiento: {self.nacimiento}
Pais: {self.pais}
Edad: {self.edad}
id: {self.ide}
Estatus: {self.estatus}\n"""
class InfectadosEnPaises():
	def __init__(self,nombrepais):
		self.nombrepais = nombrepais
		self.descartados = 0
		self.sospechosos = 0
		self.activos = 0
		self.fallecidos = 0
		self.curados = 0
	def mostrarInfectados(self):
		return f"""\nPais: {self.nombrepais}
Descartados: {self.descartados}
Sospechosos: {self.sospechosos}
Infectado: {self.activos}
Fallecidos: {self.fallecidos}
Curados: {self.curados}\n"""
Lpacientes = list()
Lpaises = list()
def ValidarCamposVacios(revisar):
	while revisar == '':
		revisar = input('No puedes colocar campos vacios!!!!!!\nCambia tu ingreso de datos: ')
	return revisar
def diagnostico(respuesta):
	if respuesta.upper() == 'S':
		return True
	elif respuesta.upper() == 'N':
		return False
	else:
		print('ERROR: Colocaste una opcion erronea. ENTER para continuar')
		input()
		modificarEstatus(pacientes)
def agregar():
	while True:
		system('cls')
		genero = input('Genero\n1-Masculino\n2-Femenino\n3-Volver\n\nOpcion: ')
		if genero!= "1" or genero!= "2":
			while genero!= "1" and genero!= "2" :
				if genero == "3":
					menu()
				genero=input('Opcion incorrecta, elija una opcion valida o escriba 3 para volver: ')	
			nombre = input('Nombre: ')
			nombre = ValidarCamposVacios(nombre)
			apellido = input('Apellido: ')
			apellido = ValidarCamposVacios(apellido)
			fecha = input('Fecha de nacimiento: ')
			fecha = ValidarCamposVacios(fecha)
			pais = input('Pais de procedencia: ')
			pais = ValidarCamposVacios(pais)
			ide = input('Ingrese identificacion (cedula,pasaporte,nombreclave,etc): ')
			ide = ValidarCamposVacios(ide)
			for persona in Lpacientes:
				while ide == persona.ide:
					ide = input('Esa identificacion ya esta registrada!\nIngresa otra: ')
					ide = ValidarCamposVacios(ide)
			while True:
				try:		
					edad= int(input('Edad: '))
					if edad>0:
						break
					else:
						print('Ingrese una edad valida')
						print('')
				except:
					print('Ingresaste una letra/caracter!')		
			NuevoPaciente = paciente(nombre,apellido,fecha,pais,genero,edad,ide)
			return NuevoPaciente
def modificarEstatus(pacientes):
	sintomas = 0
	NuevoPaciente = paciente('','','','','','','')
	if pacientes == []:
		print('Actualmente no hay pacientes en el registro. ENTER para continuar')
		input()
		menu()
	else:
		while True:
			print('1-Hacer un diagnostico')
			print('2-Cambiar estatus a Facellecido')
			print('3-Cambiar estatus a Curado')
			print('4-Cambiar estatus manualmente (sospechoso/activo/descartado)')
			print('5-Volver')
			try:
				opc = int(input('Opcion: '))
				if opc>0 and opc<5:
					ide = input('Ingrese la identificacion registrada: ')
					break
				elif opc == 5:
					opc = 0
					menu()
			except:
				system('cls')
				print('Opcion invalida')
		recorrer = 0
		while ide!= NuevoPaciente.ide:
			try:
				NuevoPaciente = pacientes[recorrer]
				recorrer+= 1
			except:
				system('cls')
				print('No se encontro!')
				print('')
				modificarEstatus(pacientes)
		if ide == NuevoPaciente.ide:
			if opc == 1:
				try:
					tos = diagnostico(input('Tiene con tos seca? S/N\n'))
					if tos == False:
						tos2 = diagnostico(input('Tiene con flema? S/N\n'))
					else:
						 tos2 = False
					respirar= diagnostico(input('Tiene problemas al tratar de respirar? S/N\n'))
					fiebre= diagnostico(input('Tiene fiebre? S/N\n'))
					if tos == True and respirar == True and fiebre == True:
						print('OH NO, TIENE CORONAVIRUS!')
						if NuevoPaciente.estatus== "Sospechoso":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
									PaisDelPaciente.sospechosos -= 1
						elif NuevoPaciente.estatus== "Fallecido":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.fallecidos -= 1
						elif NuevoPaciente.estatus== "Activo":
							system('cls')
							print('Este paciente ya esta en el estatus de Infectado!')
							print('')
							modificarEstatus(pacientes)
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.descartados -= 1
						elif NuevoPaciente.estatus== "Curado":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.curados -= 1
						NuevoPaciente.estatus = "Activo"
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
								PaisDelPaciente.activos += 1
					elif tos2== True and fiebre == True or tos2== True and fiebre == False:
						print('Tiene una gripe')
						if NuevoPaciente.estatus== "Sospechoso":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.sospechosos -= 1
						elif NuevoPaciente.estatus== "Fallecido":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.fallecidos -= 1
						elif NuevoPaciente.estatus== "Activo":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.activos -= 1
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							system('cls')
							print('Tiene una gripe')
							print('Este paciente ya esta en el estatus de Descartado!')
							print('')
							modificarEstatus(pacientes)
						elif NuevoPaciente.estatus== "Curado":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.curados -= 1
						NuevoPaciente.estatus = "Activo"
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
								PaisDelPaciente.descartados += 1
						NuevoPaciente.estatus = "Descartado (gripe)"
					elif tos== False and tos2 == False and respirar == False and fiebre == False:
						print('Presenta ningun sintoma')		
						if NuevoPaciente.estatus== "Sospechoso":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.sospechosos -= 1
						elif NuevoPaciente.estatus== "Fallecido":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.fallecidos -= 1
						elif NuevoPaciente.estatus== "Activo":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.activos -= 1
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							system('cls')
							NuevoPaciente.estatus = "Descartado (sin sintomas)"
							print('Presenta ningun sintoma')
							print('Este paciente ya esta en el estatus de Descartado!')
							print('')
							modificarEstatus(pacientes)
						elif NuevoPaciente.estatus== "Curado":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.curados -= 1
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
						PaisDelPaciente.descartados += 1
						
						NuevoPaciente.estatus = "Descartado (sin sintomas)"
					else:
						print('Tiene una alergia')
						if NuevoPaciente.estatus== "Sospechoso":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
									PaisDelPaciente.sospechosos -= 1
						elif NuevoPaciente.estatus== "Fallecido":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.fallecidos -= 1
						elif NuevoPaciente.estatus== "Activo":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.activos -= 1
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							system('cls')
							NuevoPaciente.estatus = "Descartado (alergia)"	
							print('Tiene una alergia')
							print('Este paciente ya esta en el estatus de Descartado!')
							print('')
							modificarEstatus(pacientes)
						elif NuevoPaciente.estatus== "Curado":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.curados -= 1
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
								PaisDelPaciente.descartados += 1
						NuevoPaciente.estatus = "Descartado (alergia)"			
					print(' \nENTER para continuar')
					input()
					modificarEstatus(pacientes)
				except:
					system('cls')
	
					modificarEstatus(pacientes)
			if opc == 2:
				while True:
					respuesta= input('Esta seguro que quiere cambiar el estatus a Fallecido? S/N\nActualmente esta en: '+NuevoPaciente.estatus+'\nOpcion: ')
					if respuesta.upper() == 'S':	
						if NuevoPaciente.estatus== "Sospechoso":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
									PaisDelPaciente.sospechosos -= 1
						elif NuevoPaciente.estatus== "Fallecido":
							system('cls')
							print('Este paciente ya esta en el estatus de Fallecido!')
							print('')
							modificarEstatus(pacientes)
						elif NuevoPaciente.estatus== "Activo":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.activos -= 1
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.descartados -= 1
						elif NuevoPaciente.estatus== "Curado":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.curados -= 1
						system('cls')
						print('Hecho!\n\n')
						NuevoPaciente.estatus = "Fallecido"
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
								PaisDelPaciente.fallecidos += 1
						modificarEstatus(pacientes)
					elif respuesta.upper() == 'N':
						system('cls')
						modificarEstatus(pacientes)
					else:
						print('Ingrese una opcion valida\n')
			if opc == 3:
				while True:
					respuesta= input('Esta seguro que quiere cambiar el estatus a Curado? S/N\nActualmente esta en: '+NuevoPaciente.estatus+'\nOpcion: ')
					if respuesta.upper() == 'S':
						if NuevoPaciente.estatus== "Sospechoso":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.sospechosos -= 1
						elif NuevoPaciente.estatus== "Fallecido":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.fallecidos -= 1
						elif NuevoPaciente.estatus== "Activo":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.activos -= 1
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.descartados -= 1
						elif NuevoPaciente.estatus== "Curado":
							system('cls')
							print('Este paciente ya esta en el estatus de Curado!')
							print('')
							modificarEstatus(pacientes)
						NuevoPaciente.estatus = "Curado"
						system('cls')
						print('Hecho!\n\n')
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
								PaisDelPaciente.curados += 1
						modificarEstatus(pacientes)
					elif respuesta.upper() == 'N':
						system('cls')
						modificarEstatus(pacientes)
					else:
						print('Ingrese una opcion valida')
			if opc == 4:
				while True:
					print('El estatus esta actualmente en: '+NuevoPaciente.estatus+'\n')
					print('1-Sospechoso')
					print('2-Activo')
					print('3-Descartar (gripe/fiebre)')
					print('4-Volver')
					opc2= input('Opcion: ')
					if opc2 == '1':	
						if NuevoPaciente.estatus== "Sospechoso":
							system('cls')
							print('Este paciente ya esta en el estatus de Sospechoso!')
							print('')
							modificarEstatus(pacientes)
						elif NuevoPaciente.estatus== "Fallecido":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.fallecidos -= 1
						elif NuevoPaciente.estatus== "Activo":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.activos -= 1
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.descartados -= 1
						elif NuevoPaciente.estatus== "Curado":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.curados -= 1
						NuevoPaciente.estatus = "Sospechoso"
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
								PaisDelPaciente.sospechosos += 1
						system('cls')
						print('Hecho!\n\n')
						modificarEstatus(pacientes)
					elif opc2== '2':
						if NuevoPaciente.estatus== "Sospechoso":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.sospechosos -= 1
						elif NuevoPaciente.estatus== "Fallecido":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.fallecidos -= 1
						elif NuevoPaciente.estatus== "Activo":
							system('cls')
							print('Este paciente ya esta en el estatus de Infectado!')
							print('')
							modificarEstatus(pacientes)
						elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.descartados -= 1
						elif NuevoPaciente.estatus== "Curado":
							for pais in Lpaises:
								if pais.nombrepais == NuevoPaciente.pais.upper():
									PaisDelPaciente = pais
							PaisDelPaciente.curados -= 1
						NuevoPaciente.estatus = "Sospechoso"
						for pais in Lpaises:
							if pais.nombrepais == NuevoPaciente.pais.upper():
								PaisDelPaciente = pais
								PaisDelPaciente.activos += 1
						NuevoPaciente.estatus = "Activo"
						system('cls')
						print('Hecho!\n\n')
						modificarEstatus(pacientes)
					elif opc2== '3':
						while opc2!= '1' and opc2!= '2':
							print('1-Gripe')
							print('2-Alergia')
							opc2= input('Opcion:')
							if opc2== '1':
								if NuevoPaciente.estatus== "Sospechoso":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.sospechosos -= 1
								elif NuevoPaciente.estatus== "Fallecido":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.fallecidos -= 1
								elif NuevoPaciente.estatus== "Activo":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.activos -= 1
								elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
									system('cls')
									print('Este paciente ya esta en el estatus de Descartado!')
									print('')
									modificarEstatus(pacientes)
								elif NuevoPaciente.estatus== "Curado":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.curados -= 1
								NuevoPaciente.estatus = "Sospechoso"
								for pais in Lpaises:
									if pais.nombrepais == NuevoPaciente.pais.upper():
										PaisDelPaciente = pais
								PaisDelPaciente.descartados += 1
								NuevoPaciente.estatus = "Descartado (gripe)"
								system('cls')
								print('Hecho!\n\n')
								modificarEstatus(pacientes)
							elif opc2 == '2':
								if NuevoPaciente.estatus== "Sospechoso":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.sospechosos -= 1
								elif NuevoPaciente.estatus== "Fallecido":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.fallecidos -= 1
								elif NuevoPaciente.estatus== "Activo":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.activos -= 1
								elif NuevoPaciente.estatus== "Descartado (gripe)" or NuevoPaciente.estatus== "Descartado (alergia)" or NuevoPaciente.estatus== "Descartado (sin sintomas)":
									system('cls')
									print('Este paciente ya esta en el estatus de Descartado!')
									print('')
									modificarEstatus(pacientes)
								elif NuevoPaciente.estatus== "Curado":
									for pais in Lpaises:
										if pais.nombrepais == NuevoPaciente.pais.upper():
											PaisDelPaciente = pais
									PaisDelPaciente.curados -= 1
								NuevoPaciente.estatus = "Sospechoso"
								for pais in Lpaises:
									if pais.nombrepais == NuevoPaciente.pais.upper():
										PaisDelPaciente = pais
								PaisDelPaciente.descartados += 1
								NuevoPaciente.estatus = "Descartado (alergia)"
								system('cls')
								print('Hecho!\n\n')
								modificarEstatus(pacientes)
							else:
								print('Opcion invalida')
								print('')
								system('cls')
					elif opc2== '4':
						system('cls')
						modificarEstatus(pacientes)
					else:
						print('Opcion invalida')
						print('')
					system('cls')
					modificarEstatus(pacientes)
def menu():
	while True:
		system('cls')
		opc = ''
		print('1-Registar paciente sospechoso')
		print('2-Modificar estatus de los pacientes')
		print('3-Mostrar datos de los pacientes mayores/menores de edad')
		print('4-Mostrar casos segun edad/genero/pais/mundo')
		print('5-Mostrar datos de todos los pacientes registrados')
		opc1 = input('Opcion: ')
		if opc1 == '1':
			PaisYaExistente= InfectadosEnPaises(None)
			Paciente = agregar()
			Lpacientes.append(Paciente)
			for pais in Lpaises:
				if Paciente.pais.upper() == pais.nombrepais:
					pais.sospechosos += 1
					PaisYaExistente = pais
			if PaisYaExistente.nombrepais != Paciente.pais.upper():
				NuevoPais = InfectadosEnPaises(Paciente.pais.upper())
				NuevoPais.sospechosos += 1
				Lpaises.append(NuevoPais)
			print('Agregado con exito! ENTER para continuar')
			input()
		elif opc1 == '2':
			system('cls')
			modificarEstatus(Lpacientes)
		elif opc1 == '5':
			system('cls')
			if Lpacientes != []:
				for persona in Lpacientes:
					system('cls')
					print(persona.mostrar())
					opc = input('ENTER para mostrar siguiente persona o 3 para volver\n')
					if opc == '3':
						menu()
			else:
				print('El registro esta vacio')
				input()
		elif opc1 =='4':
			system('cls')
			while True:
				
				print('1-Mostrar por pais')
				print('2-Mostrar total mundial')
				print('3-Mostrar por edad')
				print('4-Mostrar por genero')
				print('5-Volver')
				opc2  =input('Opcion: ')
				if opc2 == '1':			
					if Lpaises == []:
						system('cls')
						print('No hay registro en ningun pais!')
						print('')
					else:
						for pais in Lpaises:
							system('cls')
							print(pais.mostrarInfectados())
							salida = input('ENTER para mostrar siguiente persona o 3 para volver\n')
							if salida == '3':
								menu()
						system('cls')
				elif opc2 == '2':
					totalinfectados= 0
					totalsospechosos= 0
					totalfallecidos= 0
					totaldescartados= 0
					totalcurados = 0
					system('cls')	
					if Lpaises == []:
						print('No hay infectados registrados todavia!')
						print('')
					else:
						for pais in Lpaises:
							totalinfectados += pais.activos
							totalsospechosos += pais.sospechosos
							totaldescartados += pais.descartados
							totalfallecidos += pais.fallecidos
							totalcurados += pais.curados
						system('cls')
						print('--------------A NIVEL MUNDIAL-----------------')
						print(f'''Infectados: {totalinfectados}
Fallecidos: {totalfallecidos}
Curados: {totalcurados}
Sospechosos: {totalsospechosos}
Descartados: {totaldescartados}

''')
						input('ENTER para continuar\n')
						system('cls')
				elif opc2 == '3':
					while True:
						system('cls')
						totalinfectados= 0
						totalsospechosos= 0
						totalfallecidos= 0
						totaldescartados= 0
						totalcurados = 0
						print('Desea ver los caso de')
						print('1-Niños')
						print('2-Adultos')
						print('3-Ancianos')
						print('4-Volver')
						opc3 = input('Opcion: ')
						if opc3 == '1':
							
							Edades = filter(lambda x: x.edad <18, Lpacientes)
							for niño in Edades:
								if niño.estatus == "Curado":
									totalcurados += 1
								elif niño.estatus == "Fallecido":
									totalfallecidos += 1
								elif niño.estatus == "Activo":
									totalinfectados += 1
								elif niño.estatus == "Sospechoso":
									totalsospechosos += 1
								elif niño.estatus== "Descartado (gripe)" or niño.estatus== "Descartado (alergia)" or niño.estatus== "Descartado (sin sintomas)":
									totaldescartados += 1
							print('--------------NIÑOS INFECTADOS-----------------')
							print(f'''Infectados: {totalinfectados}
Fallecidos: {totalfallecidos}
Curados: {totalcurados}
Sospechosos: {totalsospechosos}
Descartados: {totaldescartados}

''')
							input('ENTER para continuar\n')
							system('cls')
						elif opc3 == '2':
							Edades = filter(lambda x: x.edad >17 and x.edad<60, Lpacientes)
							for adulto in Edades:
								if adulto.estatus == "Curado":
									totalcurados += 1
								elif adulto.estatus == "Fallecido":
									totalfallecidos += 1
								elif adulto.estatus == "Activo":
									totalinfectados += 1
								elif adulto.estatus == "Sospechoso":
									totalsospechosos += 1
								elif adulto.estatus== "Descartado (gripe)" or adulto.estatus== "Descartado (alergia)" or adulto.estatus== "Descartado (sin sintomas)":
									totaldescartados += 1
							print('--------------ADULTOS INFECTADOS-----------------')
							print(f'''Infectados: {totalinfectados}
Fallecidos: {totalfallecidos}
Curados: {totalcurados}
Sospechosos: {totalsospechosos}
Descartados: {totaldescartados}

''')
							input('ENTER para continuar\n')
							system('cls')
						elif opc3 == '3':
							Edades = filter(lambda x: x.edad >59, Lpacientes)
							for anciano in Edades:
								if anciano.estatus == "Curado":
									totalcurados += 1
								elif anciano.estatus == "Fallecido":
									totalfallecidos += 1
								elif anciano.estatus == "Activo":
									totalinfectados += 1
								elif anciano.estatus == "Sospechoso":
									totalsospechosos += 1
								elif anciano.estatus== "Descartado (gripe)" or anciano.estatus== "Descartado (alergia)" or anciano.estatus== "Descartado (sin sintomas)":
									totaldescartados += 1
							print('--------------ANCIANOS INFECTADOS-----------------')
							print(f'''Infectados: {totalinfectados}
Fallecidos: {totalfallecidos}
Curados: {totalcurados}
Sospechosos: {totalsospechosos}
Descartados: {totaldescartados}

''')
							input('ENTER para continuar\n')
							system('cls')
						elif opc3 == '4':
							menu()
						else:
							system('cls')
							print('Opcion invalida')
							print('')
				elif opc2 == '4':
					system('cls')
					
					while True:
						totalinfectados= 0
						totalsospechosos= 0
						totalfallecidos= 0
						totaldescartados= 0
						totalcurados = 0
						print('Desea ver los caso de')
						print('1-Masculino')
						print('2-Feminino')
						print('3-Volver')
						opc3 = input('Opcion: ')
						if opc3 == '1':
							genero = filter(lambda x: x.genero == "Masculino",Lpacientes)
							for hombre in genero:
								if hombre.estatus == "Curado":
									totalcurados += 1
								elif hombre.estatus == "Fallecido":
									totalfallecidos += 1
								elif hombre.estatus == "Activo":
									totalinfectados += 1
								elif hombre.estatus == "Sospechoso":
									totalsospechosos += 1
								elif hombre.estatus== "Descartado (gripe)" or hombre.estatus== "Descartado (alergia)" or hombre.estatus== "Descartado (sin sintomas)":
									totaldescartados += 1
							print('--------------HOMBRES INFECTADOS-----------------')
							print(f'''Infectados: {totalinfectados}
Fallecidos: {totalfallecidos}
Curados: {totalcurados}
Sospechosos: {totalsospechosos}
Descartados: {totaldescartados}

''')
						elif opc3 == '2':
							genero = filter(lambda x: x.genero == "Femenino",Lpacientes)
							for mujer in genero:
								if hombre.estatus == "Curado":
									totalcurados += 1
								elif hombre.estatus == "Fallecido":
									totalfallecidos += 1
								elif hombre.estatus == "Activo":
									totalinfectados += 1
								elif hombre.estatus == "Sospechoso":
									totalsospechosos += 1
								elif hombre.estatus== "Descartado (gripe)" or hombre.estatus== "Descartado (alergia)" or hombre.estatus== "Descartado (sin sintomas)":
									totaldescartados += 1
							print('--------------MUJERES INFECTADAS-----------------')
							print(f'''Infectados: {totalinfectados}
Fallecidos: {totalfallecidos}
Curados: {totalcurados}
Sospechosos: {totalsospechosos}
Descartados: {totaldescartados}

''')
						elif opc3== '3':
							system('cls')
							break
						else:
							system('cls')
							print('Opcion invalida')
							print('')
						input('ENTER para continuar\n')
						system('cls')
				elif opc2 == '5':
					menu()
		elif opc1 == '3':
			while True:
				salida = ''
				system('cls')
				if Lpacientes == []:
					print('El registro esta vacio!')
					print('')
					input()
					break
				print('Ver datos de')
				print('1-Mayores de edad')
				print('2-Menores de edad')
				print('3-Volver')
				opci= input('Opcion: ')
				if opci == '1':
					Mayores = filter(lambda x: x.edad>17,Lpacientes)
					for persona in Mayores:
						print(persona.mostrar())
						salida =input('ENTER para continuar o 3 para volver')
						system('cls')
					if salida == '3':
						break
				elif opci == '2':
					Menores = filter(lambda x: x.edad<18,Lpacientes)
					if Mayores == []:
						print('El registro esta vacio!')
						input()
						break
					for persona in Menores:
						print(persona.mostrar())
						salida =input('ENTER para continuar o 3 para volver')
						system('cls')
					if salida == '3':
						break
				elif opci == '3':
					break
					
			
menu()
		
