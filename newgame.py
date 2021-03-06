'''
With this module you can change the difficulty and run a new game.
'''

towers = [[], [], []]
nb_disc = [1, 8, 12]

def difficulty():
    print('\n', 'NEW GAME', '\n'*2,
          '1. EASY \n',
          '2. NORMAL \n',
          '3. HARD \n',
          '4. CUSTOM \n')
    while True:
        try:
            n = int(input('Choice (1, 2, 3 or 4): '))
            if n not in range(1, 5):
                continue
            elif n == 4:
                difficulty_custom()
        except:
            continue       
        return n

def difficulty_custom():
    n = int(input('Number of discs : '))
    nb_disc.append(n)

def help_info():
    print('\n', 'ADDITIONNAL COMMANDS', '\n'*2,
      'menu : Return to the main menu. \n',
      'save : Save your current game. \n',
      'quit : Quit the program without saving. \n')
    
def move():
    while True:
        n = input('Tower origin / Tower destination (Ex : 12) \n'
                  "Type 'help' to see the additionnals commands : ")
        if n == 'help':
            help_info()
        if n == 'menu':
            from mainmenu import main_menu
        if n == 'qqq':
            raise SystemExit
        if n == 'save':
            from loadgame import save
            save(towers, m)
        if not n.isdecimal():
            continue
        if len(n) != 2:
            continue
        tower_origin = int(n[0])
        tower_destination = int(n[1])
        if tower_origin == tower_destination:
            continue
        if (tower_origin not in range(1, 4)) or (tower_destination not in range(1, 4)):
            continue
        if towers[tower_origin-1] == []:
            continue
        if towers[tower_destination-1] == []:
            break
        if towers[tower_origin-1][0] < towers[tower_destination-1][0]:
            break
        if towers[tower_origin-1][0] > towers[tower_destination-1][0]:
            print("You can't do that !")
            continue
    disc = towers[tower_origin-1].pop(0)
    towers[tower_destination-1].insert(0, disc)
    
n = difficulty()
towers[0] = [i for i in range(1, nb_disc[n-1]+1)]
print('\n', "Tower 1 :", towers[0], '\n',
      "Tower 2 :", towers[1], '\n',
      "Tower 3 :", towers[2], '\n')

m = 0
while True:
    move()
    m += 1
    print('\n', "Tower 1 :", towers[0], '\n',
          "Tower 2 :", towers[1], '\n',
          "Tower 3 :", towers[2], '\n',
          '\n', "Moves :", m, '\n')
    if towers[0] == [] and (towers[1] == [] or towers[2] == []):
        print('Congratulations ! You Win in', m, 'moves !')
        a = input('Press ENTER to quit to the main menu ')
        from mainmenu import main_menu
