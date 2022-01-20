def rl_Encrypt(RL_lettre, RL_clef):
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	i_lettre = alphabet.index(RL_lettre)
	i_cle = alphabet.index(RL_clef)

	result = get_matrice(alphabet)[i_lettre][i_cle]

	return result

def get_matrice(alphabet):
	tableau = []
	for a in range(len(alphabet)):
		b = [alphabet[(i+a)%26] for i in range(len(alphabet))]
		tableau.append(b)
	return tableau

def afficher(matrice):
	for l in matrice:
		print(l)


if __name__ == "__main__":
	print(rl_Encrypt("c", "m"))
	print(rl_Encrypt("a", "a"))
	print(rl_Encrypt("r", "l"))
	print(rl_Encrypt("r", "i"))
	print(rl_Encrypt("e", "c"))
	print(rl_Encrypt("d", "e"))
	print(rl_Encrypt("e", "m"))
	#Like this
