from utente import Utente
from autore import Autore
from libro import Libro
from operazione import Operazione

class Biblioteca:
	def __init__(self):
		self.catalogo = []
		self.autori = []
		self.storico_operazioni = []
		self.utenti = []
		self.counter_id = 0

	def aggiungi_libro(self, titolo, isbn, nome, nazionalita):
		autore = Autore(nome, nazionalita)
		for l in self.catalogo:
			if l.isbn == isbn:
				print("Questo libro è già presente!")
				return False

		for a in self.autori:
			if a == autore:
				libro = Libro(titolo, isbn, a)
				self.catalogo.append(libro)
				return True
		
		self.autori.append(autore)
		libro = Libro(titolo, isbn, autore)
		self.catalogo.append(libro)
		return True

	def aggiungi_utente(self, nome):
		tessera = str(self.counter_id).zfill(6)
		self.counter_id += 1
		utente = Utente(nome, tessera)
		self.utenti.append(utente)

	def prestito(self, isbn, tessera_utente):
		for l in self.catalogo:
			if l.isbn == isbn:
				if l.disponibile:

					for u in self.utenti:
						if u.id_tessera == tessera_utente:
							if u.is_pieno_prestiti():
								print("Ha raggiunto il limite di prestiti")
								return False
							l.disponibile = False
							u.prestiti += 1
							prestito = Operazione(tessera_utente, isbn, "prestito")
							self.storico_operazioni.append(prestito)
							return True

					print("Questo numero di tessera non esiste")
					return False

				else:
					print("Il libro non è disponibile")
					return False
		print("Mi spiace, il libro che cerca non è nel nostro catalogo")
		return False

	def restituzione(self, isbn, tessera_utente):
		pass

	def ricerca_titolo(self, titolo):
		pass

	def ricerca_autore(self, nome):
		pass

	def libri_disponibili(self):
		pass

	def storico_prestiti(self, numero_tessera):
		pass
