# WORDLE 


The objective of *Wordle* is to guess a hidden five-letter word within six attempts. After each guess, the letters are color-coded:
- <span style="color: green;">green</span> for correct letters in the right position,
-  <span style="color: orange;">yellow</span> for correct letters in the wrong position
-  <span style="color: red;">red</span> for incorrect letters. 
  
The goal is to figure out the word by using these clues, with only one word to guess each day. 

**wordle.py** - my python program for NYT's wordle game.

I have also coded the option to play in **hard** mode or **easy** mode.

1. **Easy Mode**: In this mode, players have no restrictions on the guesses they can make.

2. **Hard Mode**: In this mode, after any guess, if you have a letter in the correct position, you must include that letter in the same position the next guess. Additionally, any other revealed letters (even those not in the correct positions) must also be included in the next guess.

