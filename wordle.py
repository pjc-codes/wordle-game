import random
import os
from time import sleep
from termcolor import colored


def wordle_board(guess_list: list[str] = [], guess_num: int = 0, result_list: list[list[int]] = []):
    colors = ['yellow', 'green', 'red']
    for i in range(guess_num):
        print(colored(f" {guess_list[i][0]}",
              color=colors[result_list[i][0]]), end="")
        print("|", colored(f"{guess_list[i][1]}",
              color=colors[result_list[i][1]]), end="")
        print("|", colored(f"{guess_list[i][2]}",
              color=colors[result_list[i][2]]), end="")
        print("|", colored(f"{guess_list[i][3]}",
              color=colors[result_list[i][3]]), end="")
        print("|", colored(
            f"{guess_list[i][4]}", color=colors[result_list[i][4]]), end="")
        print()

    for i in range(6-guess_num):
        # print(f"  |  |  |  |  ")
        print(f"__|__|__|__|__")


def get_guess_easy(guess_list: list[str], word_list: list[str], result_list: list[list[int]], word):
    while True:
        try:
            guess = input("Enter your guess : ")
            if (len(guess) == 5) and guess.isalpha() and (guess in word_list):
                if guess in guess_list:
                    print("You've already guessed that word.")
                    raise ValueError
                guess_list.append(guess.upper())
                result = check_guess(guess_list[-1], word)
                result_list.append(result)
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid 5-letter word.")


def get_guess_hard(guess_list: list[str], word_list: list[str], result_list: list[list[int]], word):
    while True:
        try:
            guess = input("Enter your guess : ")
            if (len(guess) == 5) and guess.isalpha() and (guess in word_list):
                if guess in guess_list:
                    print("You've already guessed that word.")
                    raise ValueError
                elif guess_list == []:
                    guess_list.append(guess.upper())
                    guess_result = check_guess(guess.upper(), word)
                    result_list.append(guess_result)
                else:
                    guess = guess.upper()
                    guess_result = check_guess(guess, guess_list[-1])
                    if guess_result.count(0)+guess_result.count(1) < result_list[-1].count(0)+result_list[-1].count(1):
                        print("All revealed letters must be used.")
                        raise ValueError
                    for i in range(5):
                        if (result_list[-1][i] == 1 and (guess_result[i] != 1 or guess[i] != guess_list[-1][i])):
                            print(
                                "All revealed letters must be used. You're in hard mode - green must be in green.")
                            raise ValueError

                    guess_result = check_guess(guess, word)
                    result_list.append(guess_result)
                    guess_list.append(guess)
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid 5-letter word.")


def get_words():
    words = []
    with open("words.txt") as file:
        for line in file:
            words.append(line.strip())
    return words


def check_guess(guess: str, word: str) -> list[int]:
    if word == guess:
        return [1, 1, 1, 1, 1]
    word_dict = {}
    for char in word:
        word_dict[char] = word_dict.get(char, 0) + 1
    correct = [2]*5
    # first pass to identify correct letters in correct position
    for i in range(5):
        if guess[i] == word[i]:
            correct[i] = 1
            word_dict[guess[i]] -= 1
    # second pass to identify correct letters in wrong positions
    for i in range(5):
        if (correct[i] == 2) and (guess[i] in word_dict) and (word_dict[guess[i]] > 0):
            correct[i] = 0
            word_dict[guess[i]] -= 1
    return correct


def wordle():
    word_list = get_words()
    word = random.choice(word_list).upper()
    guess_list = []
    guess_num = 0
    result_list = []
    wordle_board()
    hard_mode = input("Do you want to play in Hard Mode? (y/n) : ").upper()
    while guess_num < 6:
        if hard_mode == 'Y':
            get_guess_hard(guess_list, word_list, result_list, word)
        else:
            get_guess_easy(guess_list, word_list, result_list, word)

        sleep(0.2)
        os.system('clear')
        guess_num += 1
        wordle_board(guess_list, guess_num, result_list)
        if result_list[-1] == [1, 1, 1, 1, 1]:
            print("You win!")
            break

    print(f"The word was {word}.")


if __name__ == "__main__":
    wordle()
