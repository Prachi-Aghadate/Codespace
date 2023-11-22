import random

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for _ in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = []
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while chances != 0 and flag == 0:
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue
            letterGuessed.append(guess)
            correct=0

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                    correct += 1
                else:
                    print('_', end=' ')
            
            if correct==len(set(word)):
                print('\nThe word is:',word)
                flag=1
                print("congratulations you win")
                break
        if chances <= 0 and not set(word).issubset(letterGuessed):
            print()
            print('You lost! Try again..')
            print(f'The word was {word}')

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
        
