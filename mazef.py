
class Station:
    def __init__(self, number=None, description=None, connections=None):
        self.number = number
        self.description = description
        self.connections = connections

station_list = {}


#for i in station_list:
#    print("Station %d Connections" % i.number)
#    for j in i.connections:
#        print(j)





class Game:

    def __init__(self):
        self.station_list = {}
        self.current_station = 0
        self.station_info = {
                            0: {"connections": [1,4,5],
                                "description": "This is a big, open, busy area, filled with strange people. It is\
                                very hot and muggy. This is where your journey begins as you board the train."},
                            1: {"connections": [0,2,4,5,6],
                                "description": "This is an abandoned stop but you see flashing lights. You see only one person,\
                                sleeping on a bench. You can exit the train here to check out the lights and talk to the person."},
                            2: {"connections": [1,3,5,6,7],
                                "description": "This station leads to an icy, dark village. You see a good amount of people\
                                walking, stumbling around. The brew is flowing in the fire-heated taverns here."},
                            3: {"connections": [2,6,7,],
                                "description": "This is a tropical paradise. A village with no cars, mostly locals, great\
                                food and drink. This is a place you might want to come back to permanently."},
                            4: {"connections": [0,1,5,8,9],
                                "description": "This is a custom description"},
                            5: {"connections": [0,1,2,4,6,8,9,10],
                                "description": "This is a custom description"},
                            6: {"connections": [1,2,3,5,7,9,10,11],
                                "description": "This is a custom description"},
                            7: {"connections": [2,3,6,10,11],
                                "description": "This is a custom description"},
                            8: {"connections": [4,5,9],
                                "description": "This is a custom description"},
                            9: {"connections": [4,5,6,8,10],
                                "description": "This is a custom description"},
                            10: {"connections": [5,6,7,9,11],
                                 "description": "This is a custom description"},
                            11: {"connections": [6,7,10],
                                 "description": "This is a custom description"}
                        }

        for i in self.station_info.keys():
            s = Station(number=i, description=self.station_info[i]["description"],
                        connections=self.station_info[i]["connections"])
            self.station_list[i] = s

    def start_game(self):
        count = 0
        print("Welcome to the fiesta train - You are at Station 0")
        station_in = input("How many stations would you like to visit (up to 100)? \n")
        if int(station_in) in range(101):
            num_stations = int(station_in)

        while count < num_stations:

            print("You are at Station %d \n" % self.current_station)
            print("Your available connections are")

            for i in self.station_list[self.current_station].connections:
                print(i)

            user_in = input("Please make a selection! \n")


            if user_in == "q" or user_in == "Q":
                return False
            elif int(user_in) in \
               self.station_list[self.current_station].connections:
                print(self.station_list[int(user_in)].description)
                self.current_station = int(user_in)
                count+=1
            else:
                print("Please enter a valid station\n")

        print("you have reached your final station!\n"
              "Thank you for riding the train. GoodBYE!")



g = Game()
g.start_game()
