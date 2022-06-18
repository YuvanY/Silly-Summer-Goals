print('\t \t \t \t \t \t \t \t \t \t \t Welcome to Mad Libs\n')
print("Silly Summner Goals\n\n")
 
print('''
I could hardly believe it! School was over and there were _____ days of \n summer vacation to look forward to! I couldn't wait to ______ with \n my friends, ______, and take a road trip to ________.\n Of course, my ______ didn't want me to waste the summer \n watching _______, so they helped me come up with a few summer goals:\n
\n
1. Read ______ __________.\n
2. Practice my _________ for _______ minutes each morning.\n
3. Drink plenty of ________ and learn to eat _______ food.\n
4. Practice _______ and learn to \n________ a ___________ song.\n

\n This is going to be one __________ summer!
 \n\n\n''')

print('Fill the blanks accoding to the upper paragraph to make your own Silly Summer Goals\n')

first_blank = input('Enter what you think should be in the first blank (number): ')
second_blank = input('...second (verb): ')
third_blank = input('...third (verb): ')
forth_blank = input('...forth (place): ')
fifth_blank = input('...fifth (person/people): ')
sixth_blank = input('...sixth (Tv Show): ')
seventh_blank = input('...seventh (number): ')
eighth_blank = input('...eighth (plural noun): ')
ninth_blank = input('...ninth (noun): ')
eleventh_blank = input('...eleventh (number): ')
twelveth_blank = input('...twelve (liquid): ')
thirteenth_blank = input('...thirteenth (adjective): ')
foreteenth_blank = input('...fifteenth (noun): ')
foreteenth_blank = input('...sixteenth (verb): ')
fifteenth_blank = input('...fifteenth (adjective): ')
last_blank = input('...last (adjective): ')

Silly_Goals = f'''
I could hardly believe it! School was over and there were {first_blank} days of \n summer vacation to look forward to! I couldn't wait to {second_blank} with \n my friends, {third_blank}, and take a road trip to {forth_blank}.\n Of course, my {fifth_blank} didn't want me to waste the summer \n watching {sixth_blank}, so they helped me come up with a few summer goals:\n
\n
1. Read {seventh_blank} {eighth_blank}.\n
2. Practice my {ninth_blank} for {eleventh_blank} minutes each morning.\n
3. Drink plenty of {twelveth_blank} and learn to eat {thirteenth_blank} food.\n
4. Practice {foreteenth_blank} and learn to \n {fifteenth_blank} a(n) {sixth_blank} song.\n

\n This is going to be one {last_blank} summer!
 \n\n\n'''

print('Your "Silly Summer Goals" is ready\n\n')

print(Silly_Goals)
print('Thanks for Playing 3>')