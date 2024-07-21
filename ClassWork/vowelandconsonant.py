userInput = input('Type a word: ')

vowel = 0
consonant = 0

if 'a'.lower() in (userInput):
	vowel += 1

if 'e'.lower() in (userInput):
	vowel += 1

if 'i'.lower()in (userInput):
	vowel += 1

if 'o'.lower() in (userInput):
	vowel += 1

if 'u'.lower() in (userInput):
	vowel += 1

if 'b'.lower() in (userInput):
	consonant += 1

if 'c'.lower() in (userInput):
	consonant += 1

if 'd'.lower() in (userInput):
	consonant += 1

if 'f'.lower() in (userInput):
	consonant += 1

if 'g'.lower() in (userInput):
	consonant += 1

if 'h'.lower() in (userInput):
	consonant += 1

if 'j'.lower() in (userInput):
	consonant += 1

if 'k'.lower() in (userInput):
	consonant += 1

if 'l'.lower() in (userInput):
	consonant += 1

if 'm'.lower() in (userInput):
	consonant += 1

if 'n'.lower() in (userInput):
	consonant += 1

if 'p'.lower() in (userInput):
	consonant += 1

if 'q'.lower() in (userInput):
	consonant += 1

if 'r'.lower() in (userInput):
	consonant += 1

if 's'.lower() in (userInput):
	consonant += 1

if 't'.lower() in (userInput):
	consonant += 1

if 'v'.lower() in (userInput):
	consonant += 1

if 'w'.lower() in (userInput):
	consonant += 1

if 'x'.lower() in (userInput):
	consonant += 1

if 'y'.lower() in (userInput):
	consonant += 1

if 'z'.lower() in (userInput):
	consonant += 1


print (f'Total number of vowel is {vowel}')
print (f'Total number of consonant is {consonant}')
