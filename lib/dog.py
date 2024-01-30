#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__ (self, name = "Jim", breed = "Pug"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and (len(new_name)> 0 and len(new_name) < 25):
            self._name = new_name
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, new_breed):
        if type(new_breed) == str and (new_breed in APPROVED_BREEDS):
            self._breed = new_breed
        else:
            print("Breed must be in list of approved breeds.")
    pass
