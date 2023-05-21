import random
import time

random.seed()

time.sleep(1/2)
print ("_________        ___.                                     __     _____________________________   ")
time.sleep(1/2)
print ("\_   ___ \___.__.\_ |__   _________________  __ __  ____ |  | __ \______   \_   _____/\______ \  ")
time.sleep(1/2)
print ("/    \  \<   |  | | __ \_/ __ \_  __ \____ \|  |  \/    \|  |/ /  |       _/|    __)_  |    |  \ ")
time.sleep(1/2)
print ("\     \___\___  | | \_\ \  ___/|  | \/  |_> >  |  /   |  \    <   |    |   \|        \ |    `   \ ")
time.sleep(1/2)
print (" \______  / ____| |___  /\___  >__|  |   __/|____/|___|  /__|_ \  |____|_  /_______  //_______  /")
time.sleep(1/2)
print ("        \/\/          \/     \/      |__|              \/     \/         \/        \/         \/ ")
time.sleep(1/2)
print ("INITIATIVE ROLL PAL - Made by Kylmaenen & Google Bard!")
print ("")
time.sleep(1)
print ("-----------------------WAKE THE FUCK UP SAMURAI, WE HAVE A CITY TO BURN B)-----------------------")
print ("")
time.sleep(1)
print ("[INFO]")
print ("Players still get to roll their dice, goons' initiative is rolled automatically.")
print ("There's no need to reroll, the script will sort equal initiative values randomly!")
print ("! means a goon rolled a positive crit, ? a negative crit ")
print ("")

time.sleep(1/5)

while True:
    print ("///Insert your chooms///")

    player_characters = []

    while True:
        try:
            name = input("PLAYER: ")
            if not name:    
                raise ValueError('empty string')
            value = int(input("INITIATIVE: "))


            player_characters.append({
                "name": name,
                "value": value
            })
        except ValueError:
                print("//Nah that ain't right. Try again//.")
                continue

        answer = input("Any other chooms? (y/n): ")
        if answer == "n":
            break

    print ("-----------------------")
    print ("///Insert your goons///")

    non_player_characters = []

    while True:
        try:
            non_player_character_name = input("ENEMY: ")
            if not non_player_character_name:
                raise ValueError('empty string')
            base_value = int(input("REF: "))
            random_value = random.randint(1, 10)
            non_player_character_value = base_value + random_value
            if random_value == 1:
                random_subtract_value = random.randint(1, 10)
                non_player_character_name = non_player_character_name + "?"
                non_player_character_value -= random_subtract_value
            elif random_value == 10:
                random_add_value = random.randint(1, 10)
                non_player_character_name = non_player_character_name + "!"
                non_player_character_value += random_add_value

            non_player_characters.append({
                "name": non_player_character_name,
                "value": non_player_character_value
         })
        except ValueError:
                print("//Nah that ain't right. Try again//.")
                continue
        
        answer = input("Any other goons? (y/n): ")
        if answer == "n":
            break

    all_characters = player_characters + non_player_characters

    all_characters_set = set()
    for character in all_characters:
        all_characters_set.add(tuple(character.values()))

    for value in all_characters_set:
        characters_with_same_value = [character for character in
        all_characters if tuple(character.values()) == value]
        random.shuffle(characters_with_same_value)
        for character in characters_with_same_value:
            all_characters.remove(character)
            all_characters.insert(0, character)

    all_characters.sort(key=lambda character: character["value"], reverse=True)

    for character in all_characters:
        if character["value"] < 1:
            character["value"] = 1

    print ("")
    print ("")
    print ("----------------------------------")
    print ("IT'S F*CKING FRIDAY NIGHT CHOOMBA!")
    print ("----------------------------------")


    for character in all_characters:
        print(character["name"], character["value"])

    print ("----------------------------------")
    print ("----------------------------------")
    print ("")
    print ("")

    while True:
        answer = str(input('Need anotha round? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("//What?!//")
    if answer == 'y' :
        print ("")
        print ("---------HERE WE GO AGAIN---------")
        print ("")
        time.sleep(1/2)
        continue
    else:
        print("K CYA")
        time.sleep(1)
        break