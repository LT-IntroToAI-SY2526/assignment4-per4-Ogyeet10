# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    #  a simple dog class to learn OOP concepts
    # breed-breed of the dog
    # fur_color- the fur color of dog
    # name- name of dog 

    def __init__(self, breed="dog", fur_color="black", name="no name", age=1):
        """Initialize a new Dog with breed, fur_color, name and age"""
        self.breed = breed
        self.fur_color = fur_color
        self.name = name
        self.age = age

    def birthday(self):
        """celebrate dogs bday"""
        self.age += 1
        return f"{self.name}  celebrated their {self.age} birthday"

    def __str__(self):
        """String representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"

    def bark(self):
        return f" {self.name} says: Woof Woof "

    def paint_dog(self, new_color):
        old_color = self.fur_color
        self.fur_color = new_color
        return f"{self.name} changed their fur color from {old_color} to {new_color}"

if __name__ == "__main__":
    berg_dog = Dog("labrador", "black", "logan", 9)
    print(berg_dog.paint_dog("neon green"))
    aidan_dog = Dog("lab pitt mix", "grey", "cubbie", 9)
    default_dog = Dog()
    print(aidan_dog.birthday())
    print(berg_dog.paint_dog("neon green"))