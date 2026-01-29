class Utente:
	def __init__(self, nome, id_tessera):
		self.nome = nome
		self.id_tessera = id_tessera
		self.prestiti = 0

	def __repr__(self):
		return f"Utente(nome: {self.nome}, id_tessera: {self.id_tessera})"

	def is_pieno_prestiti(self):
		if self.prestiti == 3:
			return True
		return False