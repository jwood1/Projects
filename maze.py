#maze game
def game():
    print("Welcome to the A-Maze-ing Maze! I dare you to escape!")
​
    current_room = room0()
​
    while current_room != exit:
        current_room = current_room()
​
    current_room()
