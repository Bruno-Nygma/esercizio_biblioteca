import datetime
class Operazione:
	def __init__(self, tessera_utente, isbn, tipo):
		self.tessera_utente = tessera_utente
		self.isbn = isbn
		self.tipo = tipo
		self.data = datetime.datetime.now()

	def __repr__(self):
		return f"{self.tipo}(utente: {self.tessera_utente}, libro: {self.isbn}, data: {self.data})"
