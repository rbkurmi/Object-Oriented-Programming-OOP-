class Bird:
    def sound(self):
        print("Chirp Chirp")

class Dog:
    def sound(self):
        print("Bark Bark")

# Function demonstrating polymorphism
def animal_sound(animal):
    animal.sound()

bird = Bird()
dog = Dog()

animal_sound(bird)  # Output: Chirp Chirp
animal_sound(dog)   # Output: Bark Bark
