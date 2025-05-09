from pprint import pprint
from spellchecker import SpellChecker
spell = SpellChecker()
import re
from datetime import datetime
date = f"{datetime.now():%Y-%m-%d}"




file_outname = r'C:\Users\ortass\OneDrive - ConocoPhillips\notepadplusplus\wordle.txt'

def get_input(guess_number):


    #remove_letter_list = []

    print('guess #', guess_number, ":")
    guess = input()
    print('input match:')
    match = input()
    return guess, match
    
def get_final_answer():
    print('You loser, what is the answer?: ')
    guess = input()
    return(guess)

def print_results(guess, guess_number, guess_history, match_history, percent_guess_history):
    print(2*'\n')
    if guess_number == 7:
        print('Number of guesses: X')
    else:
        print('Number of guesses: ', guess_number)
    print('Final answer: ',guess)
    print('Guess history: ',guess_history)
    print('Match history: ',match_history)
    print('% next solve: ',percent_guess_history)
    if guess_number == 1:
        guess_rating =  'freaking impossible'
    elif guess_number == 2:
        guess_rating = 'sweet'
    elif guess_number == 3:
        guess_rating = 'pretty, pretty, pretty good'
    elif guess_number == 4:
        guess_rating = 'average'
    elif guess_number == 5:
        guess_rating = 'a bit rough'
    elif guess_number == 6:
        guess_rating = 'just barely make it'
    elif guess_number == 7:
        guess_rating = 'such a failure'
    print(guess_rating)

    # print out to file
    f = open(file_outname, mode="a")
    # this is in mode append
    # w - to write
    # r - to read
    
    print('Enter date or <enter> for today (format: 2020-05-01)')
    date_input_string = 'Enter date: '
    date_input = input(date_input_string)
    if date_input == '':
        date_input = date
    
        
    
    file_output = 'Date: ' + date_input + '\n'
    f.write(file_output)
    file_output = 'Number of guesses: ' + str(guess_number) + '\n'
    f.write(file_output)
    file_output = 'Final answer: ' + guess + '\n'
    f.write(file_output)
    guess_history = " ".join(guess_history)
    file_output = 'Guess history: ' + guess_history + '\n'
    f.write(file_output)
    match_history = " ".join(match_history)
    file_output = 'Match history: ' + match_history + '\n'
    f.write(file_output)
    percent_guess_history = " ".join(percent_guess_history)
    file_output = '% next solve: ' + percent_guess_history + '\n'
    f.write(file_output)
    file_output = guess_rating + '\n'
    f.write(file_output)
    file_output = '\n'
    f.write(file_output)
    
    f.close



    return

def word_check(wordle_letters, word):
    #wordle_letters = ["s","c","u","e"]
    #word = "computers"
    # https://stackoverflow.com/questions/45589756/how-to-check-if-three-specific-letters-exist-in-word-using-regular-expression
    # 
    re_pattern_base = "".join([fr"(?=\S*{letter})" for letter in wordle_letters])
    re_pattern_full = rf"\b{re_pattern_base}.+\b"
    if re.search(re_pattern_full,word, re.IGNORECASE):
        return True
    # code from copilot   < was trying when I thought above didn't work
    #return all(letter in word for letter in wordle_letters)


def process_word(available_letters_array, good_letters, guess, match):
    
    letter_exclude = ['','','','','']
    remove_letter_list = []
    good_letters_guess = ['','','','','']
    required_letters = []
    
    i = 0
    while i < 5:
     
        if match[i] == 'y':
            letter_exclude[i] = (guess[i])
            if guess[i] not in required_letters:
                required_letters.append(guess[i])
        elif  match[i] == 'g':
            good_letters_guess[i] = guess[i]
            if guess[i] not in required_letters:
                required_letters.append(guess[i])
        elif match[i] == 'x':
            remove_letter_list.append(guess[i])
        
        i += 1
        
    #remove excluded letters - marked x    
    for item in remove_letter_list:
        for array_item in available_letters_array:
            try:
                array_item.remove(item)
            except:
                pass
            
    #remove specific letters from columns - marked y
    i = 0
    for item in letter_exclude:
        if item != '':
            try:
                available_letters_array[i].remove(item)
            except:
                pass
        i += 1

    # capture specific letters - marked g
    #print('good letter: ',good_letters_guess)
    i = 0
    for item in good_letters_guess:
        if item != '':
            try:
                good_letters[i] = item
            except:
                pass
        i += 1

    return available_letters_array, good_letters, required_letters

    

def print_header():
    #print('sample data;   canoe   yxxyg      -answer score')
    #print('sample data;   canoe xyxxx; marsh xyyxxx; dairy ygyyx; rapid ggggg')
    #print('sample data;   canoe xyxxx; graph xyyxx; sitar xxxyy; album yxyyy; umbra yyyyg; rumba ggggg')
    #print('sample data;   canoe xxxxx; humid xxxyy; dirty ggxgg; ditty ggggg')
    #print('sample data;   canoe xyxxg; stale gxgxg; shake gxgxg; spare gxgxg; seaze gxgxg; suave ggggg')
    #print('sample data;   canoe xyxxx; graph xggxx; frail xgggg; blitz xyyyx; trail ggggg')
    #print('sample data;   canoe xgxxx; hasty xgxxg; jazzy xgxxg; party xgxxg; wombs xxyxx; mammy ggxxg - answer madly')
    print('\n'*2)
    print('Input Wordle guesses')
    print('Matches are:')
    print('     x = letter no in word')
    print('     g = letter in word in correct position')
    print('     y = letter in word but not in correct position')
    print('\n'*2)

def find_solutions(available_letters_array,good_letters, required_letters):
    first_letter_list = available_letters_array[0]
    second_letter_list = available_letters_array[1]
    third_letter_list = available_letters_array[2]
    fourth_letter_list = available_letters_array[3]
    fifth_letter_list = available_letters_array[4]

    first_letter = good_letters[0]
    second_letter = good_letters[1]
    third_letter = good_letters[2]
    fourth_letter = good_letters[3]
    fifth_letter = good_letters[4]
    
    # itterate every possible choice 
    choices = []
    #first
    for item in first_letter_list:
        if first_letter == '':
            first = item
        else:
            first = first_letter
        #second
        for item in second_letter_list:
            if second_letter == '':
                second = item
            else:
                second = second_letter
            #third
            for item in third_letter_list:
                if third_letter == '':
                    third = item
                else:
                    third = third_letter
                #fourth
                for item in fourth_letter_list:
                    if fourth_letter == '':
                        fourth = item
                    else:
                        fourth = fourth_letter
                    #fifth
                    for item in fifth_letter_list:
                        if fifth_letter == '':
                            fifth = item
                        else:
                            fifth = fifth_letter
                        output = first + second + third + fourth + fifth
                        four_letter_output = first + second + third + fourth
                        plural = False
                        if output not in choices:
                            #required_met = check_required(output, required_letters)
                            if output in spell:
                                #added this function call 3/10/25
                                #print(good_letters, output)
                                if output[4] == 's':
                                    if four_letter_output in spell:
                                        plural = True
                                if word_check(required_letters, output):
                                    if len(output) == 5:
                                        if plural == False:
                                            choices.append(output)
    print('Number of possible words: ', len(choices))
    print('Possible Words: ',choices)
    print('\n')
    return choices




all_letters_list = 'abcdefghijklmnopqrstuvwxyz'
all_letters_list = list(all_letters_list)
guess_number = 0

available_letters_array = [list(all_letters_list),list(all_letters_list),list(all_letters_list),list(all_letters_list
),list(all_letters_list)]


#============================================================

# init list 
#letter_exclude = ['','','','','']
good_letters = ['','','','',''] 
guess_number = 0
percent_guess_history = ['n/a']
#previous_guess =  ''
#previous_guess_known_letters = ''
#previous_guess_available_letters = ''
guess_history = []
match_history = []


print_header()

#============================================================

final_answer = False
#process guess

while guess_number <= 6 and final_answer == False:
    guess_number += 1
    guess, match = get_input(guess_number)
    guess_history.append(guess)
    match_history.append(match)
    available_letters_array, good_letters, required_letters =  process_word(available_letters_array, good_letters, guess, match)
    print("good_letters: ", good_letters)   
    if match != 'ggggg':
      if guess_number >= 2:
            choices = find_solutions(available_letters_array, good_letters, required_letters)
            percent_chance = 1 / len(choices) * 100
            formatted_number = f"{percent_chance:.1f}"
            percent_chance = str(formatted_number)
            percent_guess_history.append(percent_chance)
            print('percent chance of solving with next guess: ',str(percent_chance), '%')
            print('\n')
            if guess_number == 6 and match != 'ggggg':
                guess = get_final_answer()
                final_answer = True
                guess_number += 1
                print_results(guess, guess_number, guess_history, percent_guess_history)
    elif match == 'ggggg':
            final_answer = True
            print_results(guess, guess_number, guess_history, match_history, percent_guess_history)



