class cuboSemantico:
	
	cubo_semantico = None

	def __init__(self):
		self.cubo_semantico = {
		'=': {
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
		'&&': {
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
		'||': {
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
		'>': {
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
		'<': {
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
		'!=': {
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
		'>=': {
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
		'<=': {
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
		'==': {
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
		'+': {
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
		'-': {
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
		'*': {
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
		'/': {
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