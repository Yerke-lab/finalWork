
from datetime import datetime

class Animal:
    def __init__(self, name, birthdate):
        self._name = name
        self._birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        self._command = []

    def make_sound(self):
        pass

    def show_info(self):
        print(f"Name: {self._name}")
        print(f"Birthdate: {self._birthdate.strftime('%Y-%m-%d')}")

    def show_commands(self):
        print(f"{self._name}'s Commands:")
        for command in self._command:
            print(command)

    def add_command(self, command):
        self._command.append(command)

    def train(self, new_commands):
        self._command.extend(new_commands)

class Dog(Animal):
    def __init__(self, name, birthdate, breed):
        super().__init__(name, birthdate)
        self._breed = breed

    def make_sound(self):
        print("Gav!")

    def show_info(self):
        super().show_info()
        print(f"Breed: {self._breed}")


class Cat(Animal):
    def __init__(self, name, birthdate, color):
        super().__init__(name, birthdate)
        self._color = color

    def make_sound(self):
        print("Myau!")

    def show_info(self):
        super().show_info()
        print(f"Color: {self._color}")

class Hamster(Animal):
    def __init__(self, name, birthdate, fur_color):
        super().__init__(name, birthdate)
        self._fur_color = fur_color

    def make_sound(self):
        print("Peek!")

    def show_info(self):
        super().show_info()
        print(f"Fur Color: {self._fur_color}")


class Horse(Animal):
    def __init__(self, name, birthdate, color):
        super().__init__(name, birthdate)
        self._color = color

    def make_sound(self):
        print("Igo-go!")

    def show_info(self):
        super().show_info()
        print(f"Color: {self._color}")


class Donkey(Animal):
    def __init__(self, name, birthdate, height):
        super().__init__(name, birthdate)
        self._height = height

    def make_sound(self):
        print("Ia-ia!")

    def show_info(self):
        super().show_info()
        print(f"Height: {self._height} hands")


class AnimalRegistry:
    def __init__(self):
        self._animals = []
        self._counter = counter()

    def add_animal(self, animal):
        self._animals.append(animal)
        self._counter.add() 

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
            print(f"Removed {animal._name} from the registry.")
        else:
            print("Animal not found in the registry.")

    def show_all_animals(self):
        if self._animals:
            print("Animal Registry:")
            for animal in self._animals:
                animal.show_info()
                print()
        else:
            print("No animals in the registry.")

    def find_animal(self, name):
        for animal in self._animals:
            if animal._name.lower() == name.lower():
                return animal
        return None

class counter:
    def __init__(self):
        self._value = 0

    def add(self):
        self._value += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None and self._value > 0:
            raise Exception("Work with an object of type 'Counter' was not in the resource try or the resource remained open.")



registry = AnimalRegistry()

try:
    with counter() as counter:

        while True:
            print("---- Animal Registry Menu ----")
            print("1. Add a new animal")
            print("2. Find an animal")
            print("3. Remove an animal")
            print("4. Show all animals")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                animal_name = input("Enter the name of the animal: ")
                animal_birthdate = input("Enter the birthdate of the animal (YYYY-MM-DD): ")
                animal_type = input("Enter the type of the animal (dog, cat, hamster, horse, donkey): ")
                if animal_type.lower() == "dog":
                    animal_breed = input("Enter the breed of the dog: ")
                    animal = Dog(animal_name, animal_birthdate, animal_breed)
                    animal.add_command("Sit")
                    animal.add_command("Stay")
                elif animal_type.lower() == "cat":
                    animal_color = input("Enter the color of the cat: ")
                    animal = Cat(animal_name, animal_birthdate, animal_color)
                    animal.add_command("Meow")
                    animal.add_command("Purr")
                elif animal_type.lower() == "horse":
                    animal_color = input("Enter the color of the horse: ")
                    animal = Horse(animal_name, animal_birthdate, animal_color)
                    animal.add_command("Gallop")
                    animal.add_command("Trot")
                elif animal_type.lower() == "hamster":
                    animal_fur_color = input("Enter the fur color of the hamster: ")
                    animal = Hamster(animal_name, animal_birthdate, animal_fur_color)
                    animal.add_command("Run on wheel")
                    animal.add_command("Hide in tubes")
                elif animal_type.lower() == "donkey":
                    animal_height = float(input("Enter the height of the donkey (in hands): "))
                    animal = Donkey(animal_name, animal_birthdate, animal_height)
                    animal.add_command("Carry load")
                    animal.add_command("Bray")
                else:
                    animal = Animal(animal_name, animal_birthdate)

                registry.add_animal(animal)
                print(f"{animal_name} has been added to the registry.")

            elif choice == "2":
                animal_name = input("Enter the name of the animal: ")
                animal = registry.find_animal(animal_name)
                if animal:
                    print(f"Found animal: {animal_name}")
                    animal.show_info()
                    animal.show_commands()
                else:
                    print(f"Animal '{animal_name}' not found in the registry.")

            elif choice == "3":
                animal_name = input("Enter the name of the animal: ")
                animal = registry.find_animal(animal_name)
                if animal:
                    registry.remove_animal(animal)
                else:
                    print(f"Animal '{animal_name}' not found in the registry.")

            elif choice == "4":
                registry.show_all_animals()

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")
except Exception as e:
    print(f"An error occurred: {e}")    
