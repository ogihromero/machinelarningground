class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self) -> None:
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self) -> None:
        super().breathe()
        print("doing this underwater.")

    def swim(self) -> None:
        print("moving in water.")


nemo = Fish()
nemo.breathe()


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"


doggo = Dog()
print(f"A dog is {doggo.temperament}")

sparky = Labrador()
print(f"Sparky is {sparky.temperament}")
