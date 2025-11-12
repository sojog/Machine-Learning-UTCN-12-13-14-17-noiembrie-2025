""" Aceasta este documentatia pentru modul"""
## Orice in Python este un obiect

## Este un sablon de functionalitate

class Angajat:
    """ Aceasta este documentatia pentru clasa"""
    ## "__" -> metode magice
    ## self -> echivalent lui this  (referinta catre obiectul curent)
    def __init__(self, varsta):
        """ Aceasta este documentatia pentru functie"""
        self.varsta = varsta
    
    ## print(obiect) -> obiectul se transforma in string
    def __str__(self):
        return f"Angajatul are varsta {self.varsta}"


obiect = Angajat(21)
print(obiect)
print(obiect.varsta)
print(obiect.__doc__) ## __doc__ este o variabila magica 

obiect2 = Angajat(34)
print(obiect2)



