import time
from lib.Functions import readLines
from lib.Functions import normalize_city 

cities = readLines("SpisMiejscowosci.txt")
words = readLines("SpisWulgaryzmow.txt")
print(words)

words_dict = {}
for word in words:
	word = word.strip()
	words_dict["".join(sorted(word))] = word 


for city in cities:
	city = normalize_city(city)
	sorted_city = "".join(sorted(city))
	if sorted_city in words_dict:
		print("%s - %s" % (words_dict[sorted_city], city))
	


