# This is a class, which defines the attributes and methods of our Molecule with will be used for the HDI Calculator
# halogens (F, Cl, Br, and I) are grouped together as 1, because they all share the same value as H when implemented into the HDI equation
# Chalcogens (O, S, Se, Te, Po, Lv) are always equal to 0
# Created by Caleb_Culler
class Molecule:
    def __init__ (self, carbons, hydrogens, nitrogens, chalcogens, halogens, phosphorus): 
        self.carbons = carbons
        self.hydrogens = hydrogens
        self.nitrogens = nitrogens
        self.chalcogens = chalcogens
        self.halogens = halogens
        self.phosphorus = phosphorus

    # Setter Methods
    def set_number_of_carbons(self, number_of_carbons): 
        self.carbons = number_of_carbons

    def set_number_of_hydrogens(self, number_of_hydrogens): 
        self.hydrogens = number_of_hydrogens
  
    def set_number_of_nitrogens(self, number_of_nitrogens): 
        self.nitrogens = number_of_nitrogens
 
    def set_number_of_chalcogens(self, number_of_chalcogens): 
        self.chalcogens = number_of_chalcogens

    def set_number_of_halogens(self, number_of_halogens): 
        self.halogens = number_of_halogens

    def set_number_of_phosphorus(self, number_of_phosphorus):
        self.phosphrous = number_of_phosphorus 

    # Getter Methods

    def get_number_of_carbons(self): 
        return self.carbons
 
    def get_number_of_hydrogens(self): 
        return self.hydrogens

    def get_number_of_nitrogens(self): 
        return self.nitrogens

    def get_number_of_chalcogens(self): 
       return self.chalcogens

    def get_number_of_halogens(self): 
        return self.halogens

    def get_number_of_phosphrous(self): 
        return self.phosphorus
    
    def calculate_HDI (self):
        numerator = (2 * self.carbons) + 2 + self.nitrogens - self.halogens - self.hydrogens
        hdi = numerator / 2
        return hdi
     
    def __str__(self):
        formula = " "
        
        if self.carbons > 0:
            formula += f"C{self.carbons if self.carbons > 1 else ''}"
   
        if self.hydrogens > 0:
            formula += f"H{self.hydrogens if self.hydrogens > 1 else ''}"
   
        if self.nitrogens > 0:
            formula += f"N{self.nitrogens if self.nitrogens > 1 else ''}"
   
        if self.halogens > 0:
            formula += f"X{self.halogens if self.halogens > 1 else ''}"
   
        if self. chalcogens > 0:
            formula += f"O{self.chalcogens if self.chalcogens > 1 else ''}"
   
        if self.phosphorus > 0:
            formula += f"P{self.phosphorus if self.phosphorus > 1 else ''}"
        
        return f"Molecule:{formula}"

mol = Molecule(4,9, 1, 1, 0,0)

print("Carbon Atoms:", mol. carbons)
print("Hydrogen Atoms:", mol. hydrogens)
print("Nitrogen Atoms", mol.nitrogens)
print("Chalcogen Atoms", mol. chalcogens)
print("Halogen Atoms", mol.halogens)
print ("Phosphrous Atoms:", mol.phosphorus) 
print (mol)
print ("HDI:" , mol.calculate_HDI())