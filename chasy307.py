
## File: chasy307.py
## Description: A brief description of this Python module.
## Author: Smita Chakraborty
## StudentID: 110366902
## EmailID: chasy307@mymail.unisa.edu.au
## This is my own work as defined by the University's Academic Misconduct Policy



from abc import ABC

class Material(ABC):
    def __init__(self, strength):
        self.strength = strength


class Wood(Material):
    def __init__(self, strength):
        super().__init__(strength)


class Metal(Material):
    def __init__(self, strength, purity):
        super().__init__(strength)
        self.purity = purity


class Gemstone(Material):
    def __init__(self, strength, magicPower):
        super().__init__(strength)
        self.magicPower = magicPower


class Maple(Wood):
    def __init__(self, strength=5):
        super().__init__(strength)


class Ash(Wood):
    def __init__(self, strength=3):
        super().__init__(strength)


class Oak(Wood):
    def __init__(self, strength=4):
        super().__init__(strength)


class Bronze(Metal):
    def __init__(self, strength=3, purity=1.3):
        super().__init__(strength, purity)


class Iron(Metal):
    def __init__(self, strength=6, purity=1.1):
        super().__init__(strength, purity)


class Steel(Metal):
    def __init__(self, strength=10, purity=1.8):
        super().__init__(strength, purity)


class Ruby(Gemstone):
    def __init__(self, strength=1, magicPower=1.8):
        super().__init__(strength, magicPower)


class Sapphire(Gemstone):
    def __init__(self, strength=1.2, magicPower=1.6):
        super().__init__(strength, magicPower)


class Emerald(Gemstone):
    def __init__(self, strength=1.6, magicPower=1.1):
        super().__init__(strength, magicPower)


class Diamond(Gemstone):
    def __init__(self, strength=2.1, magicPower=2.2):
        super().__init__(strength, magicPower)


class Amethyst(Gemstone):
    def __init__(self, strength=1.8, magicPower=3.2):
        super().__init__(strength, magicPower)


class Onyx(Gemstone):
    def __init__(self, strength=0.1, magicPower=4.6):
        super().__init__(strength, magicPower)

## Workshop class and initializes it with instances of the Forge and Enchanter classes.
class Workshop:
    def __init__(self, forge, enchanter):
        self.forge = forge
        self.enchanter = enchanter
        ##A list of materials is created
        self.materials = {}
        self.weapons = []
        self.enchantments = []

#get back
    def addMaterial(self, material_name, quantity):
    pass

    def removeMaterial(self, material_name, quantity):
    pass

    def addWeapon(self, weapon):
        self.weapons.append(weapon)

    def removeWeapon(self, weapon):
        if weapon in self.weapons:
            self.weapons.remove(weapon)

    def addEnchantment(self, enchantment):
        self.enchantments.append(enchantment)

    def removeEnchantment(self, enchantment):
        if enchantment in self.enchantments:
            self.enchantments.remove(enchantment)

 

class Enchantment:
    def __init__(self, name, magicDamage, effect, primaryMaterial, catalystMaterial):
        self._name = name
        self._magicDamage = magicDamage
        self._effect = effect
        self._primaryMaterial = primaryMaterial
        self._catalystMaterial = catalystMaterial

    def name(self):
        return self._name

    def magicDamage(self):
        return self._magicDamage

    def effect(self):
        return self._effect

    def primaryMaterial(self):
        return self._primaryMaterial

    def catalystMaterial(self):
        return self._catalystMaterial

    #magicDamage setter
    def magicDamage(self, value):
        self._magicDamage = value

    #effect setter
    def effect(self, value):
        self._effect = value

    def calculateMagicDamage(self):
        return self._primaryMaterial.magicPower + self._catalystMaterial.magicPower

    def useEffect(self):
        return f"{self._name} enchantment and {self._effect}"


