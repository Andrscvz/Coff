class cuboSemantico:
	
	cubo_semantico = None

	def __init__(self):
		self.cubo_semantico = {
		'IGUAL': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': None,
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': None,
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'TEXTO'
			}
		},
		'CONDICIONY': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': None,
				'TEXTO': None,
			},
			'DECIMAL': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		},
		'CONDICIONO': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': None,
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		},
		'MAYQUE': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'ENTERO'
			}
		},
		'MENQUE': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'ENTERO'
			}
		},
		'DIF': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'ENTERO'
			}
		},
		'MAYIGUALQUE': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'ENTERO'
			}
		},
		'MENIGUALQUE': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'ENTERO'
			}
		},
		'IGUALQUE': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'ENTERO',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'ENTERO'
			}
		},
		'SUMA': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': 'TEXTO'
			}
		},
		'RESTA': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		},
		'MULT': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		},
		'DIV': {
			'ENTERO': {
				'ENTERO': 'ENTERO',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'DECIMAL': {
				'ENTERO': 'DECIMAL',
				'DECIMAL': 'DECIMAL',
				'TEXTO': None
			},
			'TEXTO': {
				'ENTERO': None,
				'DECIMAL': None,
				'TEXTO': None
			}
		}
	}

	def checarSemanticaExp(self,oper1,oper2,op):
		res = self.cubo_semantico.get(op)
		if res != None:
			res = res.get(oper1)
			if res != None:
				res = res.get(oper2)
		return res