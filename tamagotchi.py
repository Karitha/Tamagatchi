__author__ = 'Adam'
from termcolor import colored
import time
import sys


class Tamagatchi:
    """
        A Tamagatchi pet

        The pet can be fed, poop, exercise contract diseases, and fall in love.
        It is your job to take care of your Tamagatchi!

        Main methods:

        - feed :      +5 food
        - poop :      +5 poop
        - exercise:   +5 health
        - sleep:      +15 health
        - clean_poop  -5 poop

    """

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.food = 50
        self.poop = 0
        self.health = 100
        self.age = 0

    def colorized_pet_name(self):
        """
            Colorize the pet name.
        """
        print(colored("{0}".format(self.name), "blue"), end="")

    def feed(self):
        """
            Feed your Tamagatchi. Each fed method adds "5" to the hunger value.
        """
        self.food += 5

        # Update message
        print("You have fed", end=" ")
        self.colorized_pet_name()
        print("!")
        print(colored("Hunger +5!", "green"))

    def take_poop(self):
        """
            Tamagatchi poops.
        """
        self.poop += 5

        # Update message
        self.colorized_pet_name()
        print(colored(" has pooped!".format(self.name), "yellow"))

    def exercise(self):
        """
            Tamagatchi must be exercised so that his health doesnt fall too far.
        """
        self.health += 5

        # Update message
        self.colorized_pet_name()
        print(" is feeling strong!")
        print(colored("Health +5!", "green"))

    def sleep(self):
        """
            Tamagatchi goes to sleep. Can not be awoken for 10 seconds.
            Tamagatchi recovers 10 health. He must sleep at least 1 time every 60 seconds or else
            face risk of disease or health dropping.
        """

        # Sleeping ...
        self.colorized_pet_name()
        print(": 'ZzZzZzZzZzZzZzZ'")
        time.sleep(2)
        self.colorized_pet_name()
        print(": 'zzzzzz'")
        time.sleep(3)

        self.health += 15

        # Update message
        self.colorized_pet_name()
        print(" is well rested!")
        print(colored("Health +15!", "green"))

    def clean_poop(self):
        """
            Clean a Tamagatchi poop.
        """
        if self.poop > 0:
            self.poop -= 5
        else:
            self.colorized_pet_name()
            print(" has not pooped recently. No poops to clean.")

        # Update message
        print("It is a little less stinky around here.")
        print(colored("Poop cleaned!", "green"))

    def check_vitals(self):
        """
            Check the vitals of the Tamagatchi.
            If food value is too low, remove some health.
            If food value == 100, Tamagatchi dies!

            If age reaches certain thresholds, Tamagatchi grows up.
            Once Tamagatchi reaches 100, Tamagatchi dies!

            If too many poops, Tamagatchi dies!
        """

        # Check food
        if self.food == 0:
            self.print_death_message()
        elif self.food < 15:
            self.colorized_pet_name()
            print(colored(" is hungry!", "red"))
            print(colored("Health -5", "red"))
        elif self.food < 40:
            self.colorized_pet_name()
            print(colored(": 'I am hungry! Plz feed me :*(.", "yellow"))

        # Check age
        if self.age == 15:
            self.colorized_pet_name()
            print(colored(" has grown to be a teenager!", "green"))
        elif self.age == 30:
            self.colorized_pet_name()
            print(colored(" has grown to be an adult!", "green"))
        elif self.age == 60:
            self.colorized_pet_name()
            print(colored(" has grown to be a golden oldie!", "green"))
        elif self.age == 100:
            self.print_death_message()

        # Check poops
        if self.poop >= 50:
            self.print_death_message()
        if self.poop >= 25:
            print(colored("There are too many poops here. "
                          "Consider cleaning them up to make a healthier environment for ", 'yellow'), end="")
            self.colorized_pet_name()
            print(colored(".", "yellow"))

    def print_death_message(self):
        self.colorized_pet_name()
        print(colored(" has died x.x", "red"))
        self.colorized_pet_name()
        print(colored("was {0} years old".format(self.age), "yellow"))
        sys.exit(0)

    def pet_score(self):
        """
            Calculate a pet score based on the 4 resource values for a Tamagatchi:
            food, poop, hunger, age

            Multipliers:
            Health * 1.1
            Poop * 2.0
            Food * 1.1
            Age * 1.2

            (Health - Poop + Food + Age) / 10
        """
        return int(((self.health * 1.1) - (self.poop * 2.0) + (self.food * 1.1) + (self.age * 1.2)) / 10)

    def status(self):
        """
            Display a status message on the player's Tamagatchi pet.
        """
        print("Your Tamagatchi pet, {0}!\n".format(self.name))
        print("Health - {0}".format(self.health))
        print("Hunger - {0}".format(self.food))
        print("Age    - {0}".format(self.age))
        print("There are {0} uncleaned poops!".format(self.poop/5))
        print("Your Pet score is, {0}!".format(self.pet_score()))