from lib.Functions import normalize_city
from lib.Functions import sort_string


class VulgFinder:
    def __init__(self):
        self.vulgarisms_list = None
        self.cities_list = None

    def set_vulgarisms(self, vulgarism_list):
        self.vulgarisms_list = vulgarism_list

    def set_cities(self, cities_list):
        self.cities_list = cities_list

    def process(self):

        if self.vulgarisms_list is None or self.cities_list is None:
            raise ValueError("No expected parameters given")

        vulgarism_dictionary = self.prepare_vulgarisms()
        result_dictionary = {}
        for city in self.cities_list:
            city = normalize_city(city)
            sorted_city = sort_string(city)
            if sorted_city in vulgarism_dictionary:
                result_dictionary[city] = vulgarism_dictionary[sorted_city]
        return result_dictionary

    def prepare_vulgarisms(self):
        vulgarisms_dict = {}
        for vulgarism in self.vulgarisms_list:
            vulgarism = vulgarism.strip()
            vulgarisms_dict[sort_string(vulgarism)] = vulgarism
        return vulgarisms_dict
