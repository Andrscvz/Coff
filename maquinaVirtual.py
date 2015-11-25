import sys

class maquinaVirtual:

	dirProcs = None

	cuadruploActual = 0

	cuadruplos = None

	memoria = [[[],[],[]],[[],[],[]]] #[[[Global Entero], [Global Decimal], [Global Texto]], [[Local Entero], [Local Decimal], [Local Texto]]]

	cantidadEspacioActual = []  #Cantidad de espacio de la funcion actual [localEnteras, localDecimales, localTexto]

	referenciaFuncion = [] #Guarda los parametros que se mandan por referencia

	guardarDireccionFuncionActual = [] #Guarda la direccion de la funcion actual para cuando termine la llamada a funcion pueda regresar al cuadruplo que se encontraba

	listaAtributos = [] #Los atributos de las clases del metodo que fue llamado

	direccionResultadoFuncion = [] #Guarda la direccion de memoria que va a tener el resultado del retorno de una funcion

	contLocalInt = 0

	contLocalDecimal = 0

	contLocalTexto = 0

	def __init__(self, dirProcs, cuadruplos, contGlobalInt, contGlobalDecimal, contGlobalTexto, contInicioInt, contInicioDecimal, contInicioTexto):
		self.dirProcs = dirProcs
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
		self.cantidadEspacioActual.append([contInicioInt,contInicioDecimal, contInicioTexto])

		while (self.cuadruplos[self.cuadruploActual][0] != "end"):
			#print(self.cuadruplos[self.cuadruploActual])
			if self.cuadruplos[self.cuadruploActual][0] in ["+", "-", "*", "/", "==", ">", "&&", "||", "<", "!=", ">=", "<="]:
				self.operacion(self.cuadruplos[self.cuadruploActual][0])

			elif self.cuadruplos[self.cuadruploActual][0] == "goto":
				self.cuadruploActual = self.cuadruplos[self.cuadruploActual][3] - 1

			elif self.cuadruplos[self.cuadruploActual][0] == "=":
				self.asignar()

			elif self.cuadruplos[self.cuadruploActual][0] == "endproc":
				self.endproc()

			elif self.cuadruplos[self.cuadruploActual][0] == "era":
				self.era()

			elif self.cuadruplos[self.cuadruploActual][0] == "param":
				self.param()

			elif self.cuadruplos[self.cuadruploActual][0] == "gotof":
				self.gotof()

			elif self.cuadruplos[self.cuadruploActual][0] == "gosub":
				self.gosub()

			elif self.cuadruplos[self.cuadruploActual][0] == "imprimir":
				self.imprimir()

			elif self.cuadruplos[self.cuadruploActual][0] == "leer":
				self.leer()

			elif self.cuadruplos[self.cuadruploActual][0] == "retornar":
				self.retornar()

			elif self.cuadruplos[self.cuadruploActual][0] == "resultado":
				self.guardarDireccionRetorno()

			elif self.cuadruplos[self.cuadruploActual][0] == "ver":
				self.validarRango()

			elif self.cuadruplos[self.cuadruploActual][0] == "atributo":
				self.atributo()

			self.cuadruploActual = self.cuadruploActual + 1


	# calcula los indices de acuerdo a una funcion

	def obtenerPosEnMemoria(self, direccion):
		posEnMemoria = [0, 0, 0]
		if direccion >= 15000:
			posEnMemoria[0] = 1
			if direccion >= 15000 and direccion < 25000:
				posEnMemoria[1] = 0
				posEnMemoria[2] = direccion - 15000 - self.cantidadEspacioActual[len(self.cantidadEspacioActual) - 1][0] + self.contLocalInt
				return posEnMemoria
			elif direccion >= 25000 and direccion < 35000:
				posEnMemoria[1] = 1
				posEnMemoria[2] = direccion - 25000 - self.cantidadEspacioActual[len(self.cantidadEspacioActual) - 1][1] + self.contLocalDecimal
				return posEnMemoria
			elif direccion >= 35000 and direccion < 45000:
				posEnMemoria[1] = 2
				posEnMemoria[2] = direccion - 35000 - self.cantidadEspacioActual[len(self.cantidadEspacioActual) - 1][2] + self.contLocalTexto
				return posEnMemoria
		else:
			if direccion < 5000:
				posEnMemoria[1] = 0
				posEnMemoria[2] = direccion
				return posEnMemoria
			elif direccion >= 5000 and direccion < 10000:
				posEnMemoria[1] = 1
				posEnMemoria[2] = direccion - 3000
				return posEnMemoria
			elif direccion >= 10000 and direccion < 15000:
				posEnMemoria[1] = 2
				posEnMemoria[2] = direccion - 6000
				return posEnMemoria

	#Regresa el id de la clase padre
	def obtenerIdClasePadre(self,clase):
		return self.dirProcs[clase,0][0]

	# busca la cantidad de recursos que usa una funcion

	def obtenerTamanioFuncion(self):
		if type(self.cuadruplos[self.cuadruploActual][3]) is list:
			return
		clase = None
		clase = self.cuadruplos[self.cuadruploActual][2]
		funcion = self.cuadruplos[self.cuadruploActual][3]
		if clase != None:
			idClasePadre = self.obtenerIdClasePadre(clase)
			idFuncion = None
			for i in self.dirProcs[clase,0][3]:
				if i[0] == funcion:
					idFuncion = i[1]
			self.cuadruplos[self.cuadruploActual][3] = self.dirProcs[funcion,idFuncion][3]
		else:
			self.cuadruplos[self.cuadruploActual][3] = self.dirProcs[funcion,0][3]

	# hace operaciones aritmeticas y logicas entre 2 valores y lo guarda en una direccion

	def operacion(self, op):
		aux1 = 0
		aux2 = 0
		if type(self.cuadruplos[self.cuadruploActual][1]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][1])
			aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		elif type(self.cuadruplos[self.cuadruploActual][1]) is list:
			aux1 = self.cuadruplos[self.cuadruploActual][1][0]
			if type(aux1) is list:
				posEnMemoria = self.obtenerPosEnMemoria(aux1[0])
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				posEnMemoria = self.obtenerPosEnMemoria(aux1)
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == self.cuadruplos[self.cuadruploActual][1]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1


		if type(self.cuadruplos[self.cuadruploActual][2]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][2])
			aux2 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		elif type(self.cuadruplos[self.cuadruploActual][2]) is list:
			aux2 = self.cuadruplos[self.cuadruploActual][2][0]
			if type(aux2) is list:
				posEnMemoria = self.obtenerPosEnMemoria(aux2[0])
				aux2 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				posEnMemoria = self.obtenerPosEnMemoria(aux2)
				aux2 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == self.cuadruplos[self.cuadruploActual][2]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					aux2 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1

		posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][3])

		if op == "+":
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = aux1 + aux2
		elif op == "*":
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = aux1 * aux2
		elif op == "/":
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = aux1 / aux2
		elif op == "-":
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = aux1 - aux2
		elif op == "==":
			if aux1 == aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0
		elif op == ">":
			if aux1 > aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0
		elif op == "&&":
			if aux1 and aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0
		elif op == "||":
			if aux1 or aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0
		elif op == "<":
			if aux1 < aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0
		elif op == "!=":
			if aux1 != aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0
		elif op == ">=":
			if aux1 >= aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0
		elif op == "<=":
			if aux1 <= aux2:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 1
			else:
				self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = 0

	# imprime un valor en consola

	def imprimir(self):
		aux1 = None
		if type(self.cuadruplos[self.cuadruploActual][3]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][3])
			aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		elif type(self.cuadruplos[self.cuadruploActual][3]) is list:
			aux1 = self.cuadruplos[self.cuadruploActual][3][0]
			if type(aux1) is list:
				posEnMemoria = self.obtenerPosEnMemoria(aux1[0])
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				posEnMemoria = self.obtenerPosEnMemoria(aux1)
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == self.cuadruplos[self.cuadruploActual][3]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1

		print(aux1)

	# lee un valor de consola

	def leer(self):
		if type(self.cuadruplos[self.cuadruploActual][3]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][3])
		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == self.cuadruplos[self.cuadruploActual][3]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1


		if posEnMemoria[1] == 0:
			while True:
				try:
					self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = int(input('>> '))
					break
				except ValueError:
					print("Numero Invalido, Intente nuevamente")
		elif posEnMemoria[1] == 1:
			while True:
				try:
					self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = float(input('>> '))
					break
				except ValueError:
					print("Numero invalido, Intente nuevamente")
		elif posEnMemoria[1] == 2:
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = input('>> ')

	# se le asigna al program counter el indice del cuadruplo que se quierea ejecutar

	def gotof(self):
		aux1 = None
		if type(self.cuadruplos[self.cuadruploActual][1]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][1])
			aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		elif type(self.cuadruplos[self.cuadruploActual][1]) is list:
			aux1 = self.cuadruplos[self.cuadruploActual][1][0]
			if type(aux1) is list:
				posEnMemoria = self.obtenerPosEnMemoria(aux1[0])
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				posEnMemoria = self.obtenerPosEnMemoria(aux1)
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]	
		if aux1 == 0:
			self.cuadruploActual = self.cuadruplos[self.cuadruploActual][3] - 1

	# se le asigna un valor a una direccion de memoria especifica

	def asignar(self):
		aux1 = None
		if type(self.cuadruplos[self.cuadruploActual][1]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][1])
			aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		elif type(self.cuadruplos[self.cuadruploActual][1]) is list:
			aux1 = self.cuadruplos[self.cuadruploActual][1][0]
			if type(aux1) is list:
				posEnMemoria = self.obtenerPosEnMemoria(aux1[0])
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				posEnMemoria = self.obtenerPosEnMemoria(aux1)
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == self.cuadruplos[self.cuadruploActual][1]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					aux2 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1	

		if type(self.cuadruplos[self.cuadruploActual][3]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][3])

		elif type(self.cuadruplos[self.cuadruploActual][3]) is list:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][3][0][0])
			aux = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
			posEnMemoria = self.obtenerPosEnMemoria(aux)
		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == self.cuadruplos[self.cuadruploActual][3]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					aux2 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1
		
		if posEnMemoria[1] == 0:
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = int(aux1)
		elif posEnMemoria[1] == 1:
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = float(aux1)
		else:
			self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = str(aux1)

	# genera recursos para la funcion a instanciar y guarda los parametros que seran por referencia

	def era(self):
		self.referenciaFuncion.append([])
		self.obtenerTamanioFuncion()
		aux = self.cuadruplos[self.cuadruploActual][3]
		self.cantidadEspacioActual.append(aux)
		self.memoria[1][0] = self.memoria[1][0] + ([0] * aux[0])
		self.contLocalInt = self.contLocalInt + aux[0]

		self.memoria[1][1] = self.memoria[1][1] + ([0.0] * aux[1])
		self.contLocalDecimal = self.contLocalDecimal + aux[1]

		self.memoria[1][2] = self.memoria[1][2] + ([""] * aux[2])
		self.contLocalTexto = self.contLocalTexto + aux[2]

	#cambia el program counter a uno especificado

	def gosub(self):
		self.guardarDireccionFuncionActual.append(self.cuadruploActual)
		self.cuadruploActual = int(self.cuadruplos[self.cuadruploActual][3]) - 1

	# se le asignan valores a los parametros de una funcion

	def param(self):
		aux = self.cuadruplos[self.cuadruploActual]
		valor = None
		if type(aux[3]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(aux[3])
			
			if posEnMemoria[0] == 0:
				valor = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
			else:
				valor = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2] - self.cantidadEspacioActual[len(self.cantidadEspacioActual) - 2][posEnMemoria[1]]]

		elif type(aux[3]) is list:
			valor = aux[3][0]
			if type(valor) is list:
				posEnMemoria = self.obtenerPosEnMemoria(valor)
				valor = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				posEnMemoria = self.obtenerPosEnMemoria(valor)
				valor = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == aux[3]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					valor = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1


		posEnMemoria = self.obtenerPosEnMemoria(aux[2])
		self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]] = valor
		if aux[1]:
			self.referenciaFuncion[len(self.referenciaFuncion) - 1].append([aux[2], aux[3]])

	# se asginan los valores a las variables que se pasaron por referencia al invocar una funcion

	def regresaValoresPorReferencia(self, referencias):
		for par in referencias:
			posEnMemoria1 = self.obtenerPosEnMemoria(par[0])
			if par[1] is list:
				posEnMemoria2 = self.obtenerPosEnMemoria(par[1][0][0])
				aux = self.memoria[posEnMemoria2[0]][posEnMemoria2[1]][posEnMemoria2[2]]
				posEnMemoria2 = self.obtenerPosEnMemoria(aux)
			else:
				posEnMemoria2 = self.obtenerPosEnMemoria(par[1])
			self.memoria[posEnMemoria2[0]][posEnMemoria2[1]][posEnMemoria2[2]- self.cantidadEspacioActual[len(self.cantidadEspacioActual) - 2][posEnMemoria2[1]]] = self.memoria[posEnMemoria1[0]][posEnMemoria1[1]][posEnMemoria1[2]]

	#libera recursos que uso la funcion

	def endproc(self):
		self.cuadruploActual = self.guardarDireccionFuncionActual.pop()
		referencias = self.referenciaFuncion.pop()
		self.regresaValoresPorReferencia(referencias)
		aux = self.cantidadEspacioActual.pop()
		if aux[0] > 0:
			del self.memoria[1][0][-aux[0]:]
			self.contLocalInt = self.contLocalInt - aux[0]
		if aux[1] > 0:
			del self.memoria[1][1][-aux[1]:]
			self.contLocalDecimal = self.contLocalDecimal - aux[1]
		if aux[2] > 0:
			del self.memoria[1][2][-aux[2]:]
			self.contLocalTexto = self.contLocalTexto - aux[2]

		del self.listaAtributos[:]

	# le asigna valor a la direccion especifica

	def retornar(self):
		aux1 = None

		if type(self.cuadruplos[self.cuadruploActual][3]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][3])
			aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		elif type(self.cuadruplos[self.cuadruploActual][3]) is list:
			aux1 = self.cuadruplos[self.cuadruploActual][3][0]
			if type(aux1) is list:
				posEnMemoria = self.obtenerPosEnMemoria(aux1)
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		else:
			i = 0
			while i < len(self.listaAtributos):
				if self.listaAtributos[i][0] == self.cuadruplos[self.cuadruploActual][3]:
					posEnMemoria = self.obtenerPosEnMemoria(self.listaAtributos[i][1])
					aux2 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				i = i + 1

		if len(self.direccionResultadoFuncion) > 0:	
			posEnMemoria2 = self.obtenerPosEnMemoria(self.direccionResultadoFuncion.pop())
			self.memoria[posEnMemoria2[0]][posEnMemoria2[1]][posEnMemoria2[2]- self.cantidadEspacioActual[len(self.cantidadEspacioActual) - 2][posEnMemoria2[1]]] = aux1

	#almacena la direccion a la que se le asignara el valor de retorno

	def guardarDireccionRetorno(self):
		self.direccionResultadoFuncion.append(self.cuadruplos[self.cuadruploActual][3])

	# valida el indice de una lista

	def validarRango(self):
		longLista = self.cuadruplos[self.cuadruploActual][3]
		aux1 = None
		if type(self.cuadruplos[self.cuadruploActual][1]) is int:
			posEnMemoria = self.obtenerPosEnMemoria(self.cuadruplos[self.cuadruploActual][1])
			aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]

		elif type(self.cuadruplos[self.cuadruploActual][1]) is list:
			aux1 = self.cuadruplos[self.cuadruploActual][1][0]
			if type(aux1) is list:
				posEnMemoria = self.obtenerPosEnMemoria(aux1[0])
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
				posEnMemoria = self.obtenerPosEnMemoria(aux1)
				aux1 = self.memoria[posEnMemoria[0]][posEnMemoria[1]][posEnMemoria[2]]
		if aux1 < 0 or aux1 > longLista:
			print ("Error en tiempo de ejecucion: Indice fuera de rango" )
			sys.exit()

	#Guarda las direcciones de los atributos de un objeto
	def atributo(self):
		atributo = self.cuadruplos[self.cuadruploActual][2]
		direccion = self.cuadruplos[self.cuadruploActual][3]
		self.listaAtributos.append([atributo,direccion])