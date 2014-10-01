__author__ = 'Adam'
from tamagotchi import Tamagatchi
import time


class TamagatchiWorld:
    """
        The world in which a Tamagatchi lives, breathes, sleeps, and eats.
        Do not fail your Tamagatchi.
        Do not fail.
    """
    def __init__(self):
        self.intro_message()
        name, gender, self.player_name = self.create_tomagatchi()
        self.tamagatchi = Tamagatchi(name, gender)
        self.choices = {
            '1': self.tamagatchi.feed,
            '2': self.tamagatchi.sleep,
            '3': self.tamagatchi.exercise,
            '4': self.tamagatchi.clean_poop,
            '5': self.tamagatchi.status
        }

    @staticmethod
    def create_tomagatchi():
        """
            Gain the input variables for the player's Tamagatchi pet.
        """
        time.sleep(5)
        print("\nBefore you can adopt a Tamagatchi pet, we need a little information.")
        gender = input("First, do you want a boy or a girl pet? >>  ")
        if 'b' in gender or 'm' in gender:
            gender = "male"
        else:
            gender = "female"
        pet_name = input("OK, a {0}. And what is the name of your new Tamagatchi pet? >>  ".format(gender))
        player_name = input("And what is your name? >>  ")
        return pet_name, gender, player_name

    @staticmethod
    def intro_message():
        print("\nWelcome to the Tamagatchi Universe!")
        print("Here you will take care of your very own Tamagatchi!")
        time.sleep(5)
        print("\nIt is your task to take care of your Tamagatchi, making sure he has enough food and sleep.")
        print("Don't let his health linger, either, or he may catch a disease!")

    def show_choices(self):
        print("""
        Tamagatchi Pet Options

        1. Feed
        2. Sleep
        3. Exercise
        4. Clean Poop
        5. Status of {0}

        """.format(self.tamagatchi.name))

    def play(self):
        """
            Interact with your Tamagatchi pet.
        """
        print("{0}! We are happy you have adopted your new Tamagatchi pet, ".format(self.player_name), end=" ")
        self.tamagatchi.colorized_pet_name()
        print("!")
        while True:
            sleep_time = time.time() + 180
            while time.time() < sleep_time:
                poop_time = time.time() + 20
                while time.time() < poop_time:
                    self.show_choices()
                    choice = input("Enter an option >>  ")
                    action = self.choices.get(choice)
                    if action:
                        action()
                    else:
                        print("{0} is not a valid choice".format(choice))
                self.tamagatchi.take_poop()
                self.tamagatchi.check_vitals()
            self.tamagatchi.sleep()


if __name__ == "__main__":
    t = TamagatchiWorld()
    t.play()