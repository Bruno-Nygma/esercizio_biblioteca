from biblioteca import Biblioteca

if __name__ == "__main__":
	biblioteca = Biblioteca()
	
	#Il menu funziona fino al numero 5

	print("Benvenuto nel gestionale della biblioteca! Cosa vuoi fare?")
	print("1)  aggiungere nuovi libri al catalogo della biblioteca")
	print("2)  iscrivere nuovi utenti")
	print("3)  effettuare il prestito di un libro a un utente")
	print("4)  registrare la restituzione di un libro")
	print("5)  cercare libri per titolo (anche parziale)")
	print("6)  visualizzare tutti i libri attualmente disponibili")
	print("7)  visualizzare lo storico dei prestiti di un utente")
	print("0)  uscire dall'applicazione\n\n")

	scelta = input("Inserisci il numero corrispondente all'opzione scelta: ")

	if scelta == "1":
		print("\n\n===AGGIUNTA LIBRO===\n")
		titolo = input("Inserisci il titolo del libro: ")
		isbn = input("Inserisci il codice ISBN del libro: ")
		nome = input("Inserisci il nome dell'autore: ")
		nazionalita = input("Inserisci la nazionalità dell'autore: ")
		biblioteca.aggiungi_libro(titolo, isbn, nome, nazionalita)
	else if scelta == "2":
		print("\n\n===INSERIMENTO UTENTE===\n")
		nome = input("Inserisci il nome del nuovo utente: ")
		biblioteca.aggiungi_utente(nome)
	else if scelta == "3":
		print("\n\n===PRESTITO===\n")
		isbn = input("Inserisci il codice ISBN del libro: ")
		tessera = input("Inserisci il numero di tessera dell'utente: ")
		biblioteca.prestito(isbn, tessera)
	else if scelta == "4":
		print("\n\n===RESTITUZIONE===\n")
		isbn = input("Inserisci il codice ISBN del libro: ")
		tessera = input("Inserisci il numero di tessera dell'utente: ")
		biblioteca.restituzione(isbn, tessera)
	else if scelta == "5":
		print("\n\n===RICERCA OER TITOLO===\n")
		titolo = input("Inserisci il titolo da cercare (anche parziale)")
		print(biblioteca.ricerca_titolo(titolo))
