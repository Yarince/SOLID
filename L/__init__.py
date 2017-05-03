from abc import abstractmethod, ABCMeta


class IDuck(metaclass=ABCMeta):
    @abstractmethod
    def swim(self): pass


class ElectricDuck(IDuck):
    IsTurnedOn = False

    def turn_on(self):
        self.IsTurnedOn = True

    def swim(self):
        self.turn_on()
        # Electronic duck won't swim if it's turned off
        if not self.IsTurnedOn:
            return
        print("Electronic swimming")
        # swim logic


class Duck(IDuck):
    def swim(self):
        print("Swimming")
        # Swim logic


def make_duck_swim(duck):
    if isinstance(duck, IDuck):
        duck.swim()

make_duck_swim(ElectricDuck())
make_duck_swim(Duck())
