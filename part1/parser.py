
txt = input("Veuillez entrer le nom du fichier à ouvrir:\n")
file = open(txt, "r")
#TODO Load in memory the file

def count():
	file.seek(0)
	words = 0
	for line in file:
		words += len(line.split())
	print(words)

def mid():
	file.seek(0) #reset to the first line
	numbers = []
	for line in file:
		words = line.split()
		for w in words:
			try:
				numbers.append(float(w))
			except ValueError: #if the conversion fail continue 
				continue
	total = 0
	for n in numbers:
		total += float(n)
	#five 2 significant digits
	print(format(total/len(numbers),'.2f') if len(numbers) > 0 else 0) 
	print(total)


#do number 3-4 don't work
def findProducOrCatalog():
	file.seek(0)
	wcount = 0
	occurance = 0

	for line in file:
		words = line.split()
		if len(words) > 0:
			if words[0][0] in [';', '#' ]:
				pass
			else:
				for e in ["/produit/", "/product/", "/catalog"]:
					print(e)
					wcount = words.count(e)
					occurance += wcount
					if wcount > 0 :
						wcount += 1
	print(wcount)
	#print(occurance)
	#print(occurance/count)



count()
mid()
#findProducOrCatalog()



#print(txt.count(' '))
#print("La moyenne et la somme de tous les nombres (possiblement avec décimales) mentionnés dans le texte {s} ", )
#print("Le nombre de lignes comprenant ​")