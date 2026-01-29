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
	
	biblioteca.prestito("66010b", "000000")
	biblioteca.prestito("66010b", "000001")
	biblioteca.prestito("66011b", "000000")
	biblioteca.prestito("123456", "000000")
	biblioteca.prestito("aeiouy123", "000000")
	biblioteca.prestito("aeiouy123", "000001")


	print(biblioteca.storico_operazioni)