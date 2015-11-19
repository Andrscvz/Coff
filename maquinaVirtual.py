import sys

class maquinaVirtual:

	dirPrincipal = None

	InstruccionIndex = 0

	cuadruplos = None

	memoria = [[[],[],[]],[[],[],[]]]

	stackCantidadEspacio = []  #cada elemento [Int, decimal , texto]

	stackPorReferenciaFunciones = [] #cada elemento[[direccion, direccion], ...]

	stackDireccionesFunciones = []

	stackRetornos = []

	contLocalInt = 0

	contLocalDecimal = 0

	contLocalTexto = 0
	def __init__(self, dirPrincipal:dict, cuadruplos:list, contGlobalInt:int, contGlobalDecimal:int, contGlobalTexto:int, contInicioInt:int, contInicioDecimal:int, contInicioTexto:int):
		self.dirPrincipal = dirPrincipal
		self.cuadruplos = cuadruplos
		self.memoria[0][0] = [0] * contGlobalInt
		self.memoria[0][1] = [0.0] * contGlobalDecimal
		self.memoria[0][2] = [""] * contGlobalTexto
		self.memoria[1][0] = [0] * contInicioInt
		self.memoria[1][1] = [0.0] * contInicioDecimal
		self.memoria[1][2] = [""] * contInicioTexto
		self.contLocalInt = contInicioInt
		self.contLocalDecimal = contInicioDecimal
		self.contLocalTexto = contInicioTexto
		self.stackCantidadEspacio.append([contInicioInt,contInicioDecimal, contInicioTexto])

	# calcula los indices de acuerdo a una funcion

	def obtenerDireccion(self, direccion:int):
		indexs = [0, 0, 0]
		if direccion >= 9000:
			indexs[0] = 1
			if direccion >= 9000 and direccion < 15000:
				indexs[1] = 0
				indexs[2] = direccion - 9000 - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 1][0] + self.contLocalInt
				return indexs
			elif direccion >= 15000 and direccion < 21000:
				indexs[1] = 1
				indexs[2] = direccion - 15000 - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 1][1] + self.contLocalDecimal
				return indexs
			elif direccion >= 21000 and direccion < 27000:
				indexs[1] = 2
				indexs[2] = direccion - 21000 - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 1][2] + self.contLocalTexto
				return indexs
		else:
			if direccion < 3000:
				indexs[1] = 0
				indexs[2] = direccion
				return indexs
			elif direccion >= 3000 and direccion < 6000:
				indexs[1] = 1
				indexs[2] = direccion - 3000
				return indexs
			elif direccion >= 6000 and direccion < 9000:
				indexs[1] = 2
				indexs[2] = direccion - 6000
				return indexs

	#Regresa el id de la clase padre
	def obtenerIdClasePadre(self,clase):
		return self.dirPrincipal[clase,0][0]

	# busca la cantidad de recursos que usa una funcion

	def obtenerTamanioFuncion(self):
		if type(self.cuadruplos[self.InstruccionIndex][3]) is list:
			return
		tamanio = None
		clase = self.cuadruplos[self.InstruccionIndex][2]
		funcion = self.cuadruplos[self.InstruccionIndex][3]
		if clase != None:
			idClasePadre = obtenerIdClasePadre(clase)
			self.cuadruplos[self.InstruccionIndex][3] = self.dirPrincipal[funcion,idClasePadre][3]
		else:
			self.cuadruplos[self.InstruccionIndex][3] = self.dirPrincipal[funcion,0][3]

	# hace operaciones aritmeticas y logicas entre 2 valores y lo guarda en una direccion

	def operacionBasica(self, op:str):
		aux1 = 0
		aux2 = 0
		if type(self.cuadruplos[self.InstruccionIndex][1]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][1])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][1]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][1][0]
			if type(aux1) is list:
				indexs = self.obtenerDireccion(aux1[0])
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(aux1)
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				

		if type(self.cuadruplos[self.InstruccionIndex][2]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][2])
			aux2 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][2]) is list:
			aux2 = self.cuadruplos[self.InstruccionIndex][2][0]
			if type(aux2) is list:
				indexs = self.obtenerDireccion(aux2[0])
				aux2 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(aux2)
				aux2 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
		if op == "+":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 + aux2
		elif op == "*":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 * aux2
		elif op == "/":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 / aux2
		elif op == "-":
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = aux1 - aux2
		elif op == "==":
			if aux1 == aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == ">":
			if aux1 > aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "&&":
			if aux1 and aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "||":
			if aux1 or aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "<":
			if aux1 < aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "!=":
			if aux1 != aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == ">=":
			if aux1 >= aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0
		elif op == "<=":
			if aux1 <= aux2:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 1
			else:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = 0

	# imprime un valor en consola

	def escribir(self):
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][3]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][3]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][3][0]
			if type(aux1) is list:
				indexs = self.obtenerDireccion(aux1[0])
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(aux1)
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
		print(aux1)

	# lee un valor de consola

	def leer(self):
		indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
		if indexs[1] == 0:
			while True:
				try:
					self.memoria[indexs[0]][indexs[1]][indexs[2]] = int(input('Escribe tu entrada:'))
					break
				except ValueError:
					print("Numero Invalido, Intente nuevamente")
		elif indexs[1] == 1:
			while True:
				try:
					self.memoria[indexs[0]][indexs[1]][indexs[2]] = float(input('Escribe tu entrada:'))
					break
				except ValueError:
					print("Numero invalido, Intente nuevamente")
		elif indexs[1] == 2:
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = input('Escribe tu entrada:')

	# se le asigna al program counter el indice del cuadruplo que se quierea ejecutar

	def gotof(self):
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][1]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][1])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][1]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][1][0]
			if type(aux1) is list:
				indexs = self.obtenerDireccion(aux1[0])
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(aux1)
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]	
		if aux1 == 0:
			self.InstruccionIndex = self.cuadruplos[self.InstruccionIndex][3] - 1

	# se le asigna un valor a una direccion de memoria especifica

	def asignar(self):
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][1]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][1])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][1]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][1][0]
			if type(aux1) is list:
				indexs = self.obtenerDireccion(aux1[0])
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(aux1)
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]	
		if type(self.cuadruplos[self.InstruccionIndex][3]) is list:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3][0][0])
			aux = self.memoria[indexs[0]][indexs[1]][indexs[2]]
			indexs = self.obtenerDireccion(aux)
		else:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
		if indexs[1] == 0:
			try:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = int(aux1)
			except ValueError:
				print("Numero invalido, no se pudo completar la asignacion")
		elif indexs[1] == 1:
			try:
				self.memoria[indexs[0]][indexs[1]][indexs[2]] = float(aux1)
			except ValueError:
				print("Numero invalido, no se pudo completar la asignacion")
		else:
			self.memoria[indexs[0]][indexs[1]][indexs[2]] = str(aux1)

	# genera recursos para la funcion a instanciar y guarda los parametros que seran por referencia

	def era(self):
		self.stackPorReferenciaFunciones.append([])
		self.obtenerTamanioFuncion()
		aux = self.cuadruplos[self.InstruccionIndex][3]
		self.stackCantidadEspacio.append(aux)
		self.memoria[1][0] = self.memoria[1][0] + ([0] * aux[0])
		self.contLocalInt = self.contLocalInt + aux[0]
		self.memoria[1][1] = self.memoria[1][1] + ([0.0] * aux[1])
		self.contLocalDecimal = self.contLocalDecimal + aux[1]
		self.memoria[1][2] = self.memoria[1][2] + ([""] * aux[2])
		self.contLocalTexto = self.contLocalTexto + aux[2]

	#cambia el program counter a uno especificado

	def gosub(self):
		self.stackDireccionesFunciones.append(self.InstruccionIndex)
		self.InstruccionIndex = self.cuadruplos[self.InstruccionIndex][3] - 1

	# se le asignan valores a los parametros de una funcion

	def param(self):
		aux = self.cuadruplos[self.InstruccionIndex]
		valor = None
		if type(aux[3]) is int:
			indexs = self.obtenerDireccion(aux[3])
			valor = self.memoria[indexs[0]][indexs[1]][indexs[2] - self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 2][indexs[1]]]

		elif type(aux[3]) is list:
			valor = aux[3][0]
			if type(valor) is list:
				indexs = self.obtenerDireccion(valor)
				valor = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(valor)
				valor = self.memoria[indexs[0]][indexs[1]][indexs[2]]
		indexs = self.obtenerDireccion(aux[2])
		self.memoria[indexs[0]][indexs[1]][indexs[2]] = valor
		if aux[1]:
			self.stackPorReferenciaFunciones[len(self.stackPorReferenciaFunciones) - 1].append([aux[2], aux[3]])

	# se asginan los valores a las variables que se pasaron por referencia al invocar una funcion

	def asignarReferencias(self, referencias:list):
		for par in referencias:
			indexs1 = self.obtenerDireccion(par[0])
			if par[1] is list:
				indexs2 = self.obtenerDireccion(par[1][0][0])
				aux = self.memoria[indexs2[0]][indexs2[1]][indexs2[2]]
				indexs2 = self.obtenerDireccion(aux)
			else:
				indexs2 = self.obtenerDireccion(par[1])
			self.memoria[indexs2[0]][indexs2[1]][indexs2[2]- self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 2][indexs2[1]]] = self.memoria[indexs1[0]][indexs1[1]][indexs1[2]]

	#libera recursos que uso la funcion

	def endproc(self):
		self.InstruccionIndex = self.stackDireccionesFunciones.pop()
		referencias = self.stackPorReferenciaFunciones.pop()
		self.asignarReferencias(referencias)
		aux = self.stackCantidadEspacio.pop()
		if aux[0] > 0:
			del self.memoria[1][0][-aux[0]:]
			self.contLocalInt = self.contLocalInt - aux[0]
		if aux[1] > 0:
			del self.memoria[1][1][-aux[1]:]
			self.contLocalDecimal = self.contLocalDecimal - aux[1]
		if aux[2] > 0:
			del self.memoria[1][2][-aux[2]:]
			self.contLocalTexto = self.contLocalTexto - aux[2]

	# le asigna valor a la direccion especifica

	def retornar(self):
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][3]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][3])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][3]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][3][0]
			if type(aux1) is list:
				indexs = self.obtenerDireccion(aux1)
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(aux1)
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
		if len(self.stackRetornos) > 0:	
			indexs2 = self.obtenerDireccion(self.stackRetornos.pop())
			self.memoria[indexs2[0]][indexs2[1]][indexs2[2]- self.stackCantidadEspacio[len(self.stackCantidadEspacio) - 2][indexs2[1]]] = aux1

	#almacena la direccion a la que se le asignara el valor de retorno

	def guardarDirRetornar(self):
		self.stackRetornos.append(self.cuadruplos[self.InstruccionIndex][3])

	# valida el indice de una lista

	def validarIndex(self):
		longLista = self.cuadruplos[self.InstruccionIndex][1][0]
		aux1 = None
		if type(self.cuadruplos[self.InstruccionIndex][2]) is int:
			indexs = self.obtenerDireccion(self.cuadruplos[self.InstruccionIndex][2])
			aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]

		elif type(self.cuadruplos[self.InstruccionIndex][2]) is list:
			aux1 = self.cuadruplos[self.InstruccionIndex][2][0]
			if type(aux1) is list:
				indexs = self.obtenerDireccion(aux1[0])
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
				indexs = self.obtenerDireccion(aux1)
				aux1 = self.memoria[indexs[0]][indexs[1]][indexs[2]]
		if aux1 < 0 or aux1 >= longLista:
			print ("Error en tiempo de ejecucion: Indice fuera de rango" )
			sys.exit()

# lectura de los cuadruplos hasta que se encuentre el "END"

	def empezar(self):
		while (self.cuadruplos[self.InstruccionIndex][0] != "end"):
			if self.cuadruplos[self.InstruccionIndex][0] in ["+", "-", "*", "/", "==", ">", "&&", "||", "<", "!=", ">=", "<="]:
				self.operacionBasica(self.cuadruplos[self.InstruccionIndex][0])

			elif self.cuadruplos[self.InstruccionIndex][0] == "goto":
				self.InstruccionIndex = self.cuadruplos[self.InstruccionIndex][3] - 1

			elif self.cuadruplos[self.InstruccionIndex][0] == "=":
				self.asignar()

			elif self.cuadruplos[self.InstruccionIndex][0] == "endproc":
				self.endproc()

			elif self.cuadruplos[self.InstruccionIndex][0] == "era":
				self.era()

			elif self.cuadruplos[self.InstruccionIndex][0] == "param":
				self.param()

			elif self.cuadruplos[self.InstruccionIndex][0] == "gotof":
				self.gotof()

			elif self.cuadruplos[self.InstruccionIndex][0] == "gosub":
				self.gosub()

			elif self.cuadruplos[self.InstruccionIndex][0] == "imprimir":
				self.escribir()

			elif self.cuadruplos[self.InstruccionIndex][0] == "leer":
				self.leer()
			elif self.cuadruplos[self.InstruccionIndex][0] == "retornar":
				self.retornar()
			elif self.cuadruplos[self.InstruccionIndex][0] == "asignacionRetorno":
				self.guardarDirRetornar()
			elif self.cuadruplos[self.InstruccionIndex][0] == 'validarIndex':
				self.validarIndex()
			self.InstruccionIndex = self.InstruccionIndex + 1


