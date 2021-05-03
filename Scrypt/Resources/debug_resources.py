


class debugar:
	"""
	Tem função de ajudar no acompanhamento do processo da automaçãp e\n 
	para debugar os erros encontrados.
	"""
	def __init__(self, procurar, m2, endereco, acao, ativado):
		self.procurar = procurar
		self.m2 = m2
		self.endereco = endereco
		self.acao = acao
		self.ativado = ativado


	def sttus(procurar = 'N/A', m2 = 'N/A', endereco = 'N/A', descricao = 'N/A', acao = 'N/A', ativado = False):
		"""
		Mostra status das strings de pesquisa
		kwargs -- procurar, m2, endereco, descricao, acao, ativado = False por padrão
		"""
		if ativado == True:
			print('_'*50)
			print('*'*50)
			print(f'Pesquisa: {procurar}')
			print('*'*50)
			print(f'>>>m2 = {m2}')
			print(f'>>>Endereço = {endereco}')
			print('>>>Descricao = ok')
			print(f'>>>acao = {acao}')
			print('_'*50)
		else:
			pass
				





