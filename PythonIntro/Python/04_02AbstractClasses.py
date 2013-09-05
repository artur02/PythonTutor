from abc import ABCMeta, abstractmethod

class Animal(object, metaclass=ABCMeta):

    @abstractmethod
    def getAvgWeight(self):
        pass

class Talker(object, metaclass=ABCMeta):

    @abstractmethod
    def talk(self):
        pass

class Duck(Animal, Talker): 
    def getAvgWeight(self):
        return "10kg"

    def talk(self):
        return "Quack"

Animal.register(Duck)
Talker.register(Duck)

#animal = Animal()
duck = Duck()

print("Duck average weight: ", duck.getAvgWeight())
print("Duck talks: ", duck.talk())