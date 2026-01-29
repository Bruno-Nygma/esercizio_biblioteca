class Libro:
	def __init__(self, titolo, isbn, autore):
		self.titolo = titolo
		self.isbn = isbn
		self.autore = autore
		self.disponibile = True

	def __repr__(self):
		return f"Libro(titolo: {self.titolo}, ISBN: {self.isbn}, autore: {self.autore.nome})"