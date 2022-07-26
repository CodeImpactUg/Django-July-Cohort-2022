class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


if __name__ == "__main__":
    # creating a class object now
    # An object is class instance
    # instantiate the Parrot class
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)

    # access the class attributes
    print("Blu is a {}".format(blu.__class__.species))
    print("Woo is also a {}".format(woo.__class__.species))

    # access the instance attributes
    print("{} is {} years old".format(blu.name, blu.age))
    print("{} is {} years old".format(woo.name, woo.age))

    print(blu.species)
    print(woo.species)

    print(blu)  # prints out the class representation
    print(woo)
