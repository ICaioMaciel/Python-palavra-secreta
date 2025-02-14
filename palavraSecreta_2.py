import random as rd

with open('lista_palavras.txt', encoding= 'UTF-8') as file:
    word_list = file.read().splitlines()
    
secret_word = rd.choice(word_list)
correct_letter = ''
guesses_counter = 0
guessed_letter = []

while True: 
    guess_letter = input('\nType a letter: ').upper()
    
    if guess_letter in guessed_letter:
        print('That letter is alredy used!!')
        print(guessed_letter)
        continue
    
    for letter in guess_letter:
        guessed_letter.append(guess_letter)
        
    guesses_counter += 1

    if len(guess_letter) > 1:
        print('Type one letter!!!')
        continue
    elif not guess_letter.isalpha():
        print("You have to type a letter!!!")
        continue

    if(guess_letter) in secret_word:
        correct_letter += (guess_letter)
    
    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in correct_letter:
            formed_word += secret_letter
        else:
            formed_word += '*'
    
    print(f'\nWord formed: {formed_word}')
    
    if formed_word == secret_word:
        print('\nYou Win! Congratulations!!!')
        print(f'You finished with {guesses_counter} tries ')
        break