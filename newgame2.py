'''
With this module you can change the difficulty and run a new game.
'''

##########
#NEW GAME#
##########

def test_input_difficulty():
    while True:
        print('\n', 'NEW GAME', '\n'*2,
              '1. EASY \n',
              '2. NORMAL \n',
              '3. HARD \n',
              '4. EXPERT \n')
        try:
            n = int(input('Choice (1, 2, 3 or 4): '))
            if n not in range(1, 5):
                continue
        except:
            continue       
        return n
        
towers = [[], [], []]

nb_disc = [5, 8, 10, 12]

def test_move():
    while True:
        n = input('Tower origin / Tower destination (Ex : 12): ')
        if not n.isdecimal():
            continue
        if len(n) != 2:
            continue
        tower_source = int(n[0])
        tower_destination = int(n[1])
        if tower_source == tower_destination:
            continue
        if (tower_source not in range(1, 4)) or (tower_destination not in range(1, 4)):
            continue
        if towers[tower_source-1] == []:
            continue
        if towers[tower_destination-1] == []:
            break
        if towers[tower_source-1][0] < towers[tower_destination-1][0]:
            break
    disc = towers[tower_source-1].pop(0)
    towers[tower_destination-1].insert(0, disc)
         
                
        
n = test_input_difficulty()
towers[0] = [i for i in range(1, nb_disc[n-1]+1)]
print('\n', "Tower 1 :", towers[0], '\n',
      "Tower 2 :", towers[1], '\n',
      "Tower 3 :", towers[2], '\n')
while True:
    test_move()
    print('\n', "Tower 1 :", towers[0], '\n',
          "Tower 2 :", towers[1], '\n',
          "Tower 3 :", towers[2], '\n')




    
    
    

