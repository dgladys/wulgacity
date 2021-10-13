
def readLines(x):
    f = open(x, "r", encoding="windows-1250")
    lines = f.readlines()
    f.close()
    return lines

def normalize_city(city):
	city = city.strip().lower()
	return city
