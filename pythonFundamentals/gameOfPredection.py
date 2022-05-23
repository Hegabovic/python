import random

trials = []
counter = 10


def generateRandomNumber():
    return random.randint(0, 100)


isPlaying = input('do you want to play ? y / n  ')

if isPlaying.lower() == 'y':
    print('let the game starts now')
    random_number = generateRandomNumber()
    print('A random number has been generated guess the number now')
    print('                You have 10 trials                     ')

    while counter > 0:
        player_number = input('choose a number = ')
        if int(player_number) < 100:
            print(random_number)
            counter -= 1
            if int(player_number) == int(random_number):
                print('Good job you Nailed it')
                if counter > 0:
                    random_number = generateRandomNumber()
                    if int(player_number) == int(random_number):
                        print('Good job you Nailed it')
                    else:
                        if int(player_number) > int(random_number):
                            print('  try to decrease you input  ')
                            print('         try again           ')
                        else:
                            print('  try to increase you input  ')
                            print('         try again           ')
            else:
                if int(player_number) > int(random_number):
                    print('  try to decrease you input  ')
                    print('         try again           ')
                else:
                    print('  try to increase you input  ')
                    print('         try again           ')

        if counter == 0:
            print('you are out of trials play again soon')
            print('           See You Soon              ')
            print('     thank you for your time         ')

else:
    print('lets play later then 😴')
