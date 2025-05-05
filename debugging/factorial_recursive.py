#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Description :
	Calcule récursivement la factorielle d’un nombre entier.

	Paramètres :
	n (int) — Un entier non négatif dont on veut calculer la factorielle.

	Return :
	int — La factorielle de n. Par convention, 0! = 1.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
