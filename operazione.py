import datetime
class Operazione:
	def __init__(self, utente, libro, tipo):
		self.utente = utente
		self.libro = libro
		self.tipo = tipo
		self.data = datetime.datetime.now()

	def __repr__(self):
		return f"{self.tipo}(utente: {self.utente.id_tessera}, libro: {self.libro.isbn}, data: {self.data})"
