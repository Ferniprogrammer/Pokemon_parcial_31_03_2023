#!/usr/bin/env python
# -*- coding: utf-8 -*-

from weapon_type import WeaponType

"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.



class Pokemon():
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = Pokemon(id, pokemon_name, weapon_type, health_points,
                   attack_rating, defense_rating)

    Parameters
    ----------
      [in] id ID of the Pokemon.
      [in] pokemon_name Name of the Pokemon.
      [in] weapon_type Type of weapon that carries out the Pokemon.
      [in] health_points Points of health that the Pokemon has.
      [in] attack_rating Attack rating of the Pokemon.
      [in] defense_rating Defense rating of the Pokemon.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Pokemon.

    Attributes
    ----------

    Example
    -------
      >>> from pokemon import Pokemon
      >>> from weapon_type import WeaponType
      >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
    """
    
    known_pokemon_ids = [] 
    
    def __init__(self, id, pokemon_name, weapon_type, hp, attack, defence):
        
        #Forma de comprobar que el id no se repite o el pokemon no se repite
        
        if id in Pokemon.known_pokemon_ids:
            raise ValueError("This pokemon id is already in use. Please, choose another one or check that the pokemon does not already exist.")
        Pokemon.known_pokemon_ids.append(id)
        
        self._id = id
        #Protegida ya que si tocan la id puede haber un fallo en todo el programa al eliminar una id en especifico, pero las subclases deben poder acceder a él
        self._pokemon_name = pokemon_name
        #Protegida ya que si cambian el nombre no afecta al programa, pero es un identificador más intuitivo que la id para el jugador
        self._weapon_type = weapon_type
        #Protegida ya que el cambiar el nombre del arma no afecta al programa, pero si que puede confundir al jugador
        if hp > 100 or hp < 1:
            raise ValueError("The health points of a pokemon must be between 1 and 100.")
        self._hp = hp
        #Protegida ya que si el jugador cambia la vida del pokemon puede crear un pokemon inmortal o uno que tenga vida negativa, pero no rompe el programa
        if attack > 10 or attack < 1:
            raise ValueError("The attack rating of a pokemon must be between 1 and 10.")
        self._attack = attack
        #Protegida ya que si el jugador cambia el ataque del pokemon puede crear un pokemon que no pueda atacar o que tenga un ataque infinito, pero no rompe el programa
        if defence > 10 or defence < 1:
            raise ValueError("The defense rating of a pokemon must be between 1 and 10.")
        self._defence = defence
        #Protegida ya que si el jugador cambia la defensa del pokemon puede crear un pokemon que no pueda defenderse o que tenga una defensa infinita, pero no rompe el programa
        
    def __del__(self):
        Pokemon.known_pokemon_ids.remove(self._id)
           
    def __str__(self):
        return "Pokemon ID {:d} with name {:s} has as weapon {:s} and health {:d}".format(self._id, self._pokemon_name, self._weapon_type.name, self._hp)
    
    def is_alive(self):
        
        if self._hp > 0:
            return True
        else:
            hp = 0
            return False
    def get_id(self):
        return self._id 
    def get_pokemon_name(self):
        return self._pokemon_name
    def get_weapon_type(self):
        return self._weapon_type
    def get_health_points(self):
        return self._hp
    def get_attack_rating(self):
        return self._attack   
    def get_defense_rating(self):
        return self._defence
    
    def fight_attack(self, pokemon_to_attack):
        total_damage =  self._attack
        hit = pokemon_to_attack.fight_defense(total_damage)
        return hit
        
    def fight_defense(self, total_damage):
   
        if total_damage > self._defence:
            self._hp = self._hp - (total_damage - self._defence)    
            return True
        else:
            return False
        
        
        
        
        
def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    
    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
