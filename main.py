from biblioteca import Biblioteca

if __name__ == "__main__":
	biblioteca = Biblioteca()
	biblioteca.aggiungi_libro("Lo Hobbit", "66010b", "J.R.R. Tolkien", "Inglese")
	biblioteca.aggiungi_libro("Il Signore degli Anelli", "66011b", "J.R.R. Tolkien", "Inglese")
	biblioteca.aggiungi_libro("Artemis Fowl", "123456", "Eoin Colfer", "Inglese")
	biblioteca.aggiungi_libro("La Fattoria degli Animali", "aeiouy123", "George Orwell", "Americano")

	print(biblioteca.catalogo)
	print(biblioteca.autori)

	biblioteca.aggiungi_utente("paolo")
	biblioteca.aggiungi_utente("bruno")

	print(biblioteca.libri_disponibili())
	
	biblioteca.prestito("66010b", "000000")
	biblioteca.prestito("66010b", "000001")
	biblioteca.prestito("66011b", "000000")
	biblioteca.prestito("123456", "000000")
	biblioteca.prestito("aeiouy123", "000000")
	biblioteca.prestito("aeiouy123", "000001")

	biblioteca.restituzione("66010b", "000000")
	biblioteca.restituzione("66010a", "000000")
	biblioteca.restituzione("aeiouy123", "000000")

	print(biblioteca.storico_prestiti("000001"))