import random

first = set()
second = set()
third = set()

firstword = input("please enter the first word you would like to scramble ")
secWord = input("please enter the second word you would like to scramble ")
thirdWord = input("please enter the third word you would like to scramble ")

for i in range(0, 10000):
    wordchanged = firstword
    word = ""
    if len(first) == (len(firstword)**2):
        break
    elif len(first)!= (len(firstword)**2):
        for letter in range(0, len(firstword)):
            randomized = random.randint(0, 1)
            if randomized == 0:
                word += str(wordchanged[letter].upper())
            if randomized == 1:
                word += str(wordchanged[letter].lower())
        first.add(word)
                 

for i in range(0, 10000):
    wordchanged = secWord
    word = ""
    if len(second) == (len(secWord)**2):
        break
    elif len(second)!= (len(secWord)**2):
        for letter in range(0, len(secWord)):
            randomized = random.randint(0, 1)
            if randomized == 0:
                word += str(wordchanged[letter].upper())
            if randomized == 1:
                word += str(wordchanged[letter].lower())
        second.add(word)

for i in range(0, 10000):
    wordchanged = thirdWord
    word = ""
    if len(third) == (len(thirdWord)**2):
        break
    elif len(third)!= (len(thirdWord)**2):
        for letter in range(0, len(thirdWord)):
            randomized = random.randint(0,1)
            if randomized == 0:
                word += str(wordchanged[letter].upper())
            if randomized == 1:
                word += str(wordchanged[letter].lower())
        third.add(word)

list1stword = list(first)
list2word = list(second)
list3word = list(third)
all_poss = list()

def combo(first, second, third):
    for i in first:
        for j in second:
            for k in third:
                all_poss.append(i + j + k)
                all_poss.append(i + k + j)
                all_poss.append(k + i + j)
                all_poss.append(k + j + i)
                all_poss.append(j + k + i)
                all_poss.append(j + i + k) 

combo(list1stword, list2word, list3word)
print(all_poss)

with open('password-list.txt', 'w') as filewrite:
    for password in all_poss:
        filewrite.write("%s\n" % password)
    print('Done')
    
