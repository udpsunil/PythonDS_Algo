class Dog:
    # This is the constructor for the class.
    # This is called when a Dog object is created.
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

    # Acessor method that returs speakText stored in the object
    def speak(self):
        return self.speakText

    # Accessor method to get the name
    def getName(self):
        return self.name

    # Accessor method to return birthday
    def birthDate(self):
        return f"{self.month}/{self.day}/{self.year}"

    # Mutator method to change behaviour
    def changeBark(self, bark):
        self.speakText = bark

    # Overloading operator
    def __add__(self, otherDog):
        return Dog(f"Puppy of {self.name} and {otherDog.name}", self.month, 
        self.day, self.year+1, self.speakText+otherDog.speakText)

def main():
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeBark("woofywoofy")
    print(boyDog.speak())
    puppy = boyDog + girlDog
    print(puppy.speak())
    print(puppy.getName())
    print(puppy.birthDate())
    
if __name__ == "__main__":
    main()