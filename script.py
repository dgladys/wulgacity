from lib.Functions import read_lines
from lib.VulgFinder import VulgFinder

cities = read_lines("SpisMiejscowosci.txt")
vulgarisms = read_lines("SpisWulgaryzmow.txt")

finder = VulgFinder()
finder.set_cities(cities)
finder.set_vulgarisms(vulgarisms)
found = finder.process()

if len(found):
    print("Found some cities (%d) that can be combined to vulgarisms:" % len(found))
    for key in found:
        print("  * %s - %s" % (key, found[key]))
else:
    print("Not found any cities, which can be combined into vulgarisms")
