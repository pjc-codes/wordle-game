def wordle_board(guess_word_list: list[str], guess_num: int):
    for i in range(guess_num):
        print(f"|{guess_word_list[i][0]}|{guess_word_list[i][1]}|{
              guess_word_list[i][2]}|{guess_word_list[i][3]}|{guess_word_list[i][4]}|")
    for i in range(6-guess_num):
        print(f"|_|_|_|_|_|")


lst = ['abcde', 'fghij', 'lmnop','squat','plume','chunk']
lst = [word.upper() for word in lst]
n = 3
wordle_board(lst, 6)
