import random
from os import system

def read_text():
    words = []
    with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
        words = [i for i in f]
    return words       

def select_word():
    selected_word = random.choice(read_text())
    selected_word = selected_word.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('\n','')
    return selected_word

def drawing_lines(word):
    random_selected_word = word
    number_line = len(random_selected_word)
    line_list = ['_' * number_line]
    line_string = ''.join(line_list)
    return line_string

def guessing_part(word, lines):
    w = list(word)
    l = list(lines)
    guessing_letter_selected_by_user = ''
    counter = 0

    while w != l:
        counter += 1
        guessing_letter_selected_by_user = input('Adivine con una letra: ')
        assert len(guessing_letter_selected_by_user) == 1, '¡Seleccionaste más de una letra!'
        system('clear')
        for i in range(0, len(w)):
            if w[i] == guessing_letter_selected_by_user:
                l[i]=w[i]
        print(' '.join(l).upper())
    print(f'¡Ganaste!, la palabra era: {word.upper()}, adivinaste en {counter} intentos')

def run():
    print('-' * 20)
    palabra = select_word()
    guessing_part(palabra, drawing_lines(palabra))
    print('-' * 20)

if __name__=='__main__':
    run()