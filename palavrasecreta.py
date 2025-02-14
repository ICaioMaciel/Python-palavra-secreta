import random as rd

random_words = ['Carro', 'Barco', 'Aviao', 'Galinha', 'Passaro', 'Cachorro', 'gato', 'tubarao'] 
secret_word = rd.choice(random_words).upper()
corrects_letters = '' 
number_guesses = 0  

while True: 
    guessWord = input(f'\ntype a letter: ').upper()
    number_guesses += 1
    
    if len(guessWord) > 1: 
        print('type just one letter')
        continue 

    if(guessWord) in secret_word: 
        corrects_letters +=(guessWord) 

    formed_word = '' 
    for secret_letter in secret_word: 
        if secret_letter in corrects_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'
            
    print(f'\nPalavra formada: {formed_word}')
    
    if formed_word == secret_word:
        print('\nVocê ganhou!! Parabéns!')
        print(f'Seu numero de tentativas foram: {number_guesses}')
        break
    