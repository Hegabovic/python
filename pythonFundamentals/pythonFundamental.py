import math
from collections import Counter
####################  declaring variables  #######################
from typing import TextIO

x1, x2, y1, y2 = 10.0, 20.0, 30.0, 40.0
repeated_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
oddString = 'hegabovic'
evenString = 'Abdullah'
#########################  Problem 1  ############################

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(distance)


#########################  Problem 2  ############################

def remove_repeated():
    unique_items_list = list(set(repeated_list))
    return unique_items_list


x = remove_repeated()
print(x)


#########################  Problem 3  ############################
def string_breaker(string):
    if len(string) % 2 == 0:
        middle_of_string = int(len(string) / 2)
        front_string = string[0:middle_of_string]
        back_string = string[middle_of_string::]
        return front_string, back_string
    else:
        middle_of_string = int((len(string) / 2) + 1)
        front_string = string[0:middle_of_string]
        back_string = string[middle_of_string::]
        return front_string, back_string


# test case: even string
front, back = string_breaker(evenString)
print(front)
print(back)
# test case: even string
front, back = string_breaker(oddString)
print(front)
print(back)
#########################  Problem 4  ############################
file_name = input('please enter the file name : ')
print('file name is ', file_name)
read_content = open(file_name, 'r')
comma_separated = (read_content.read()).split()
print(comma_separated)

counter = Counter(comma_separated)
most_repeated = counter.most_common(20)

file_name = open('popular_words.txt', 'w')

file_name.write(str(most_repeated))


#########################  Problem 5  ############################
def makeLowerCase(string):
    print(string.lower())


makeLowerCase('HI HUMAN, WE ARE VENOM')


#########################  Problem 6  ############################
def letterExist(string, char):
    print(f"here is my string {string} , my char {char}")
    if (char in string):
        myList = []
        for location, letter in enumerate(string):
            if letter == char:
                myList.append(location)
        print(myList)
    else:
        print('letter is not included in the string')


letterExist('abdallah', 'a')
###########################   Bonus   ############################
