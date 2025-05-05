#!/usr/bin/python3
class Checkbook:
	def __init__(self):
		self.balance = 0.0

	def deposit(self, amount):
		self.balance += amount
		print("Déposé : ${:.2f}".format(amount))
		print("Solde actuel : ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		if amount > self.balance:
			print("Fonds insuffisants pour effectuer le retrait.")
		else:
			self.balance -= amount
			print("Retiré : ${:.2f}".format(amount))
			print("Solde actuel : ${:.2f}".format(self.balance))

	def get_balance(self):
		print("Solde actuel : ${:.2f}".format(self.balance))


def main():
	cb = Checkbook()
	while True:
		action = input("Que voulez-vous faire ? (deposit, withdraw, balance, exit) : ").lower()
		if action == 'exit':
			print("Merci d’avoir utilisé le carnet de chèques.")
			break
		elif action == 'deposit':
			try:
				amount = float(input("Entrez le montant à déposer : $"))
				if amount <= 0:
					print("Veuillez entrer un montant positif.")
				else:
					cb.deposit(amount)
			except ValueError:
				print("Entrée invalide. Veuillez entrer un nombre.")
		elif action == 'withdraw':
			try:
				amount = float(input("Entrez le montant à retirer : $"))
				if amount <= 0:
					print("Veuillez entrer un montant positif.")
				else:
					cb.withdraw(amount)
			except ValueError:
				print("Entrée invalide. Veuillez entrer un nombre.")
		elif action == 'balance':
			cb.get_balance()
		else:
			print("Commande invalide. Veuillez réessayer.")

if __name__ == "__main__":
	main()

"""
Améliorations :
Ajout de try...except pour intercepter les erreurs de conversion avec float().
Gestion des entrées négatives.
Messages d'erreur clairs à l’utilisateur.

Ce que ce code gère maintenant :
Entrée invalide comme des lettres ou symboles (abc, @, etc.)
Montants négatifs ou nuls
Commandes inconnues
"""
