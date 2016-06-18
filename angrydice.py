import random


class Angry_Dice:

    possible_values = {

    1:
"""
+-------+
|       |
|   o   |
|       |
+-------+""",
	2:
"""
+-------+
| o     |
|       |
|     o |
+-------+""",
	3:
"""
+-------+
| \   / |
| ^   ^ |
| ----- |
+-------+""",
	4:
"""
+-------+
| o   o |
|       |
| o   o |
+-------+""",
	5:
"""
+-------+
| o   o |
|   o   |
| o   o |
+-------+""",
	6:
"""
+-------+
| o   o |
| o   o |
| o   o |
+-------+
	"""
            }





    def __init__(self):
        print("Welcome to the angry dice game")
        self.count = 0

    def round_one(self):
    #First round function for Angry_Dice class

        print("Round one")

        roll1 = 0
        roll2 = 0
        roll_again = 0

        while True:
            user_input = input("Press enter to roll the die!")
            roll1, roll2 = random.randint(1,6), random.randint(1,6)
            self.count += 1

            if (((roll1 or roll2) == 1) and ((roll1 or roll2) == 2)):
                print("You win this round, round 1!")
                break
            elif ((roll1 or roll2) == 1):
                while roll_again != 2:
                    user_input = input("You rolled a 1, need a 2. Press enter to roll again!")
                    roll_again = random.randint(1,6)
                    self.count += 1
                    print("Rolled a %s" % roll_again)
                    print("%s attempts" % self.count)
                break
            elif ((roll1 or roll2) == 2):
                while roll_again != 1:
                    user_input = input("You rolled a 2, need a 1. Press enter to roll again!")
                    roll_again = random.randint(1,6)
                    self.count += 1
                    print("Rolled a %s" % roll_again)
                    print("%s attempts" % self.count)
                break
        #print("you completed round 1 with %s trys!" % self.count)

    def round_two(self):

        print("Round two")

        roll3 = 0
        roll4 = 0
        roll_again = 0

        while True:
            user_input = input("Press enter to roll the die!")
            roll3, roll4 = random.randint(1,6), random.randint(1,6)
            self.count += 1

            if (((roll3 or roll4) == 3) and ((roll3 or roll4) == 4)):
                print("You win this round, round 2!")
                break
            elif ((roll3 or roll4) == 3):
                while roll_again != 4:
                    user_input = input("You rolled an Angry Die, need a 4. Press enter to roll again!")
                    roll_again = random.randint(1,6)
                    self.count += 1
                    print("Rolled a %s" % roll_again)
                    print("%s attempts" % self.count)
                    break
                    #print("you completed round 2 with %s trys!" % self.count)

            elif ((roll3 and roll4) == 3):
                print("Uuuhh..You rolled two Angry Dice and must start over!")






#if __name__ == "__main__":
test = Angry_Dice()
test.round_one()
test.round_two()
