class cuboSemantico:
	
	cubo_semantico = None

	def __init__(self):
		self.cubo_semantico = {
		'==': {
			'entero': {
				'entero': 'entero',
				'decimal': None,
				'texto': None
			},
			'decimal': {
				'entero': None,
				'decimal': 'decimal',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'texto'
			}
		},
		'&&': {
			'entero': {
				'entero': 'entero',
				'decimal': None,
				'texto': None,
			},
			'decimal': {
				'entero': None,
				'decimal': None,
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': None
			}
		},
		'||': {
			'entero': {
				'entero': 'entero',
				'decimal': None,
				'texto': None
			},
			'decimal': {
				'entero': None,
				'decimal': None,
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': None
			}
		},
		'>': {
			'entero': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'decimal': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'entero'
			}
		},
		'<': {
			'entero': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'decimal': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'entero'
			}
		},
		'!=': {
			'entero': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'decimal': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'entero'
			}
		},
		'>=': {
			'entero': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'decimal': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'entero'
			}
		},
		'<=': {
			'entero': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'decimal': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'entero'
			}
		},
		'==': {
			'entero': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'decimal': {
				'entero': 'entero',
				'decimal': 'entero',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'entero'
			}
		},
		'+': {
			'entero': {
				'entero': 'entero',
				'decimal': 'decimal',
				'texto': None
			},
			'decimal': {
				'entero': 'decimal',
				'decimal': 'decimal',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': 'texto'
			}
		},
		'-': {
			'entero': {
				'entero': 'entero',
				'decimal': 'decimal',
				'texto': None
			},
			'decimal': {
				'entero': 'decimal',
				'decimal': 'decimal',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': None
			}
		},
		'*': {
			'entero': {
				'entero': 'entero',
				'decimal': 'decimal',
				'texto': None
			},
			'decimal': {
				'entero': 'decimal',
				'decimal': 'decimal',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': None
			}
		},
		'/': {
			'entero': {
				'entero': 'entero',
				'decimal': 'decimal',
				'texto': None
			},
			'decimal': {
				'entero': 'decimal',
				'decimal': 'decimal',
				'texto': None
			},
			'texto': {
				'entero': None,
				'decimal': None,
				'texto': None
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