import random
HANGpic=['''
   _________
   vvvvvvvvv







   ========= ''','''
   _________
   vvvvvvvvv





   =========''','''
   _________
   vvvvvvvvvv



   ==========''','''
   __________
   vvvvvvvvvv

   ==========''','''
   __________
   vvvvvvvvvv
   ==========''']
words={1:'dosa golgappe softy biscuit toffee coffee tea chocolate pasta maggi noodles chat kofta puri sabji rasogulla papdi burger samosa pizza '.split(),
       2:'bear lion elephant fox jackal tiger dog cat deer snake giraffe zebra koala goat camel mouse horse donkey bull cow hippopotamus '.split(),
       3:'english maths hindi biology geography history civics computer GK drawing chemistry physics sanskrit'.split(),
       4:'ironMan spiderman thor batman superman flash hulk optimus groot starlord rocket shaktiman superman motu patlu shinchan shiva '.split(),
       5:'dron badminton cricket basketball chess ludo snakeandladder toytrain football '.split()}
def getrandom(wordList,level):
    if level=='1':
        print('Enter your specialisation:::')
        print('1.Khana   2.Animals   3.Subjects   4.Superheroes   5.Games') 
        wkey = int(input())
        windex = random.randint(0,len(wordList[wkey])-1)
        return wordList[wkey][windex]
    else:
        print('Jarraa sambhal ke..........')
        wkey=random.choice(list(wordList.keys()))
        windex=random.randint(0,len(wordList[wkey])-1)
        return wordList[wkey][windex]

def display(Hangpic,missedLetters,correctLetters,secretword):
    print(HANGpic[len(missedLetters)])
    print('Missed letters : ',end='')
    for i in missedLetters:
        print(i,end='')
    print()
    print('*******************')
    blanks='?'*len(secretword)
    for j in range(len(secretword)):
        if secretword[j] in correctLetters:
            blanks=blanks[:j]+secretword[j]+blanks[j+1:]
    for letters in blanks:
        print(letters,end='')
    print()
def getguess(alreadyguessed):
    while True:
        print('Guess a letter')
        guess=input()
        guess=guess.lower()
        if len(guess)!=1:
            print('Enter a single letter')
        elif guess in alreadyguessed:
            print('Already guessed, choose again...')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('ENTER a letter.....You foooool..')
        else:
            return guess
def playagain():
    print('Wanna play again.(no/yes/no)')
    res=input()
    return res.lower().startswith('y')
print('~~~~~~~~~~~~~~~~~~~~The falling shutter version of     H A N G M A N~~~~~~~~~~~~~~~~~~~~~')
print('Apna naam btao : ',end='')
name=input()
missedLetters=''
correctLetters=''
print(name+' CHOOSE THE LEVEL OF GAME... Jara dekhe toh Kitne dimaaaag vale ho?...')
print('1. Easy     2.Hard               (For easy - enter 1 , for hard - enter 2)')
level=input()
secretword=getrandom(words,level)
gameisdone=False
while True:
    display(HANGpic,missedLetters,correctLetters,secretword)
    guess = getguess(missedLetters+correctLetters)
    if guess in secretword:
        correctLetters=correctLetters+guess
        flag = True
        for i in range(len(secretword)):
            if secretword[i] not in correctLetters:
                flag=False
                break
        if flag:
            print('SABASH!!!! '+name+' . The secret word is '+secretword+' . You have guessed right..')
            gameisdone=True
    else:
        missedLetters=missedLetters + guess
        if len(missedLetters)==len(HANGpic)-1:
            print('He He He ...... !!!!!! YOU LOST... HO HA HAAAA')
            gameisdone=True
            print('Aapki koshish nakaam rahi , itne missed guesses : '+str(len(missedLetters))+' aur itne correct guesses '+ str(len(correctLetters))+' the word was -- ')
            print(secretword)
            display(HANGpic,missedLetters,correctLetters,secretword)
    if gameisdone:
        if playagain():
            print('OHO.. Toh phir se khelna hai '+name+' Chalo theek haiiii ...CHOOSE THE LEVEL OF GAME...Dekhen Kitne dimaaaag vale ho?...(1/2)')
            level=input()
            missedLetters=''
            correctLetters=''
            gameisdone=False
            secretword=getrandom(words,level)
        else:
            print('Ba - Byeeeee')
            break
                
    
        
    
            
         
