print('V tomto kratkem dotazniku zjistime, jake je Vase znameni zverokruhu. Jdeme na to!')
mesic = str(input("Napiste mesic narozeni: "))
den = int(input("Zadejte den narozeni: "))
if den < 31:
	if mesic == 'leden':
		znameni = 'kozoroh' if (den < 20) else 'vodnar'
	elif mesic == 'unor':
		znameni = 'vodnar' if (den < 20) else 'ryby'
	elif mesic == 'brezen':
		znameni = 'ryby' if (den < 20) else 'beran'
	elif mesic == 'duben':
		znameni = 'beran' if (den < 20) else 'byk'
	elif mesic == 'kveten':
		znameni = 'byk' if (den < 20) else 'blizenci'
	elif mesic == 'cerven':
		znameni = 'blizenci' if (den < 21) else 'rak'
	elif mesic == 'cervenec':
		znameni = 'rak' if (den < 23) else 'lev'
	elif mesic == 'srpen':
		znameni = 'lev' if (den < 23) else 'panna'
	elif mesic == 'zari':
		znameni = 'panna' if (den < 23) else 'vahy'
	elif mesic == 'rijen':
		znameni = 'vahy' if (den < 23) else 'stir'
	elif mesic == 'listopad':
		znameni = 'stir' if (den < 22) else 'strelec'
	elif mesic == 'prosinec':
		znameni = 'strelec' if (den < 21) else 'kozoroh'
	print("Vase znameni je: ", znameni)
else:
	print('Pokud vim, mesic ma nanejvys 31 dni')
