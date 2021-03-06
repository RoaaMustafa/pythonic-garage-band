from abc import ABC, abstractmethod
class Musician(ABC):
    """
    Musician Class
    """
    members = []
    
    def __init__(self, name):
        self.name=name
        Musician.members.append(self.name)
        

        
@abstractmethod        
def __str__():
        pass
@abstractmethod    
def __repr__():
        pass
      
def get_instrument():
        pass
      
def play_solo():
        pass
         
    
    
class Guitarist(Musician):
    """
    Guitarist Class
    """
    def __str__(self):
        return (f"My name is {self.name} and I play guitar")
    
    def __repr__(self):
        return (f'Guitarist instance. Name = {self.name}')

    def play_solo(self):
        return ("face melting guitar solo")

    def get_instrument(self):
        return ('guitar')

    
    
class Drummer(Musician):
    """
    Drummer Class
    """
    def __str__(self):
        return (f"My name is {self.name} and I play drums")
    
    def __repr__(self):
        return (f'Drummer instance. Name = {self.name}')

    def play_solo(self):
        return ("rattle boom crash")

    def get_instrument(self):
        return ('drums')

class Bassist(Musician):
    """
    Bassist Class
    """
    def __str__(self):
        return (f"My name is {self.name} and I play bass")
    
    def __repr__(self):
        return (f'Bassist instance. Name = {self.name}')

    def get_instrument(self):
        return ('bass')
    
    def play_solo(self):
        return ("bom bom buh bom")
    
    
class Band(Musician):
    instances=[]
    def __init__(self, name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
        
    def play_solos(self):
        solos=[]
        for item in self.members:
            solos.append(item.play_solo())
        return solos
    
    @classmethod
    def to_list(cls):
        
        return cls.instances

    def __str__(self):
        
        return (f"We are {self.name} and we are music band")

    def __repr__(self):

        return (f"Band instance. Name = {self.name}")
   