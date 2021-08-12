import random
from words_en_to_kr import words_en_to_kr


def flash_card_start():
    print('Start flash-cards? y/n')
    choice = input()

    if choice.lower() == 'y':
        choosing_word_count()
    elif choice.lower() == 'n':
        pass
    else:
        flash_card_start()


def choosing_word_count():
    print(f'How many words would you like? (max {len(words_en_to_kr)})')
    word_count = input()

    if not word_count.isnumeric():
        print('Given input is not number.')
        choosing_word_count()
    elif int(word_count) > len(words_en_to_kr):
        print('Given number is over the max word amount.')
        choosing_word_count()
    else:
        game_start(int(word_count))


def game_start(word_count):
    randomized_word_list = list(words_en_to_kr.items())
    random.shuffle(randomized_word_list)
    words_for_game = dict(randomized_word_list[:word_count])
    print('=========================================')

    correct = 0
    for eng_word, kr_word in words_for_game.items():
        guessed_word = input(f'>> {eng_word} - ').strip()

        if guessed_word == kr_word:
            print('Correct!')
            correct += 1
        else:
            print(f'Wrong! Correct word: {kr_word}')

    print('=========================================')
    print(f'Correct answers: {correct}/{word_count} ({correct*100/word_count}%)')
    print('Would you like to try again? y/n')
    again_input = input()

    if again_input.lower() == 'y' or again_input.lower() == 'ㅛ':
        choosing_word_count()
    else:
        pass


if __name__ == '__main__':
    flash_card_start()
