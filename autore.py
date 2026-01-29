class Autore:
	def __init__(self, nome, nazionalita):
		self.nome = nome
		self.nazionalita = nazionalita

	def __eq__(self, autore):
		if self.nome == autore.nome and self.nazionalita == autore.nazionalita:
			return True
		return False