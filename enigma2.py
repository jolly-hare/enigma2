import string
import re


def unmorse(message):
    MORSE_CODE_DICT = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
    message = message.replace("_", "-") + " "
    decipher = ''
    citext = ''
    i = 0
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
    return decipher


'''ENIGMA 2 PUZZLE'''
# teaser tweet: https://twitter.com/SOLgods_/status/1460659253623066630
# teaser tweet image: https://pbs.twimg.com/media/FEVN11ZX0AYGr6J?format=jpg&name=large
# teaser tweet indicates "rabbit food" via google translate (malayalam language)
# *** LEFT PAGE ***
# Roman Numerals
# 1 XXV . VI . MCMXLII == 25 6 1942 # Anatoli Bugorski's bday
# 2 III . IV . MCMLXII == 3 4 1962 # Peter Bugorski's bday??? Peter Higgs???
# Continue fathers work
# Quarks 4623514605352 == enigma 1 key sequence
# Blue Binary/Hex
# Morse  .-. .- -... -... .. - == RABBIT
# *** RIGHT PAGE ***
# Morse
# top .. -- --- -... ... . ... == IM OBSES
# mid -.-. . .--. .- == CEPA | KIPA
# bottom_1 -.. .. -- .. -.. .. ..- -- == DIMIDIUM == latin for "the/a half"
# bottom_2 ...- .. .. -.. . .-. -. == VIIDERN
# *** ACROSS PAGES ***
# Morse_1 -.-. . == CE
# Morse_2 -.. .-. == DR
# Morse_3 .-. -. == RN
# Big red 0100 0001 1000 == 256 1 4096 (Hex 2 Dec) == 4 1 8 (Bin 2 Dec) == 4 18 == D R
# Big red 0001 0110 0010 == 1 272 16 (Hex 2 Dec) == 1 6 2 (Bin 2 Dec) == 16 2 == P B
# Feynman Diagram of Mutual Annihilation
# new site went live 11/17/2021
# https://thefracture.art/ contains a block of binary
bgmatrix1_1 = '''111101110001011101001100000111010100010111010011000101010111010100110101110001'''
bgmatrix1_2 = '''tbd'''
bgmatrix2_1 = '''tbd'''
bgmatrix2_2 = '''tbd'''
bgmatrix3 = '''tbd'''
enigma2_chap3 = '''No one will forget the day it happened…
Ringing so immense you could not hear glass shattering across the city. A white-hot flash so severe covering your eyes was not enough to reduce the burn.
Complete sensory overload—so overpowering, it felt as though I had been transported to some blank void where nothing existed. Not even my own thoughts. Empty chaos.
I remember thinking, “This must be hell” but then… the ringing stopped.
And I saw what hell really looked like.
The screams.
Who you were or who you knew was meaningless. At that moment of dread all sense of compassion was lost. The weak were trampled into the ground beneath the shoes of those who could still stand. People scurried like animals—rats, chucking each other aside clawing at the entrance to that godforsaken bunker desperate for the salvation that awaited inside. That last ray of hope glistening in doom.
Self-preservation was all that mattered.
I am not proud of what I had to do to get into that filthy hovel we called our ‘sanctuary’, but I’d be lying if I said I wouldn’t do it again.
Far off in the distance, a giant dome shield reflected sun rays our way—The Utopion. It lay tranquil against the foreground of mayhem surrounding our streets, completely unfazed as it always had been towards the suffering of our people.
I wish I saved myself from watching what happened next—to bathe still in that blissful ignorance…that unknowing peace. It was inevitable, I guess…our undoing, our downfall. I suppose to them we were only sub-human. Inferior. A stain of the imperfect past waiting to be cleansed from the gene pool of the future. A crack in the cog of evolution. A defect.
The Bridged, that’s how they saw us.
“Look! It’s moving!” —a frightened shriek from the corner. I redirected my gaze towards the voice, then eyed where its speaker was pointing.
My heart stopped.
The Utopion Dome had opened for the first time…ever.
In that instance, I knew what was coming. Total annihilation. Absolute. Destruction. I witnessed the entire scope of civilization as I knew it, the one I called home, rendered completely decimated without mercy of a second thought.
I saw it. I felt it. It was…evil.
That day ended in pain—agony, torture, loss…I thought it was over, all of it. Everything.
It wasn’t. Our suffering had only just begun.'''
# https://thefracture.art/holy-enigma-2/
enigma2text = '''
Here lies the Holy Enigma 2.0. The highly anticipated sequel to the original Holy Enigma that some of you may be unpleasantly familiar with. The original Enigma lies here if you have not yet experienced it. If you wish to undertake the new challenge we wish you luck:
The God’s horrifying presence still remains unexplained. They are trying to communicate with you. Each victory is guiding you one step forward towards understanding these terrifying beings and The Fracture.
An Army of 6,666 demented cross-dimentional entities hunting mercilessly. They are searching ruthlessly for something or someone. That is clear. Why? We do not know.
Supersymmetry was just a theory. That was what they said. After the incident the data was manipulated and nullified to the public. No one could know what they saw. He knew that each particle in our universe had a partner somewhere.. He just needed to see it himself. To confirm everything his Father had experienced. To see them.
'''
enigma2text_short = '''
The God’s horrifying presence still remains unexplained. They are trying to communicate with you. Each victory is guiding you one step forward towards understanding these terrifying beings and The Fracture. An Army of 6,666 demented cross-dimentional entities hunting mercilessly. They are searching ruthlessly for something or someone. That is clear. Why? We do not know. Supersymmetry was just a theory. That was what they said. After the incident the data was manipulated and nullified to the public. No one could know what they saw. He knew that each particle in our universe had a partner somewhere.. He just needed to see it himself. To confirm everything his Father had experienced. To see them.
'''
enigma2text_short_tweaked = '''
The God’s horrifying presence still remains unexplained. They are trying to communicate with you. Each victory is guiding you one step forward towards understanding these terrifying beings and The Fracture. An Army of 6,666 demented cross-dimentional entities hunting mercilessly. They are searching ruthlessly for something or someone. That is clear. Why, we do not know. Supersymmetry was just a theory. That was what they said. After the incident the data was manipulated and nullified to the public. No one could know what they saw. He knew that each particle in our universe had a partner somewhere,  he just needed to see it himself. To confirm everything his Father had experienced, to see them.
'''
source = enigma2_chap3
sentences = re.split('\? |\. |\n', source.strip())
print(f'sentences parsed: {len(sentences)}')
#print(sentences)
print(f'unmorse= {unmorse("- ... .-")}')
set_1 = [11, 6, 10, 7, 12, 4, 13, 3, 8, 1, 9, 5, 2]
doubled_set = [(element - 1) * 2 for element in set_1]
print(f'set: \n  {doubled_set} =\n  {[list(string.ascii_uppercase)[i] for i in doubled_set] }')
for j in range(len(doubled_set)):
    doubled_set = doubled_set[j:] + doubled_set[:j]
    shifted = []
    for i in doubled_set:
        shifted.append(list(string.ascii_uppercase)[i])
    print("".join(shifted))
#Binary sources
blackrighttop = ['100', '01001100', '001']
bluecircle = ['1011', '0110', '1010', '0111', '1100', '0100', '1101', '0011', '1000', '0001', '1001', '0101', '0010']
bluelefttop = ['0101', '00010100', '1001', '0111', '00010011']  # == ENIGM
blueleftbottom = ['00100000', '00011000', '0101', '00100010', '00010100', '1001']  # == TREVNI | INVERT
blueleftfive = ['0100', '0110', '0010', '0011', '0101']  # ?= first five digits of enigma 1 key sequence
bluerighttop = ['0010', '0000', '0001', '0010']  # == 2012
red_top = ['0100', '0001', '1000']     # == 4 1 8 | 4  18
red_bottom = ['0001', '0110', '0010']  # == 1 6 2 | 16  2
red_all = ['0100', '00011000', '00010110', '0010']
foo = bluerighttop + bluelefttop + blueleftbottom

thesource = bluecircle
thesource_dec = []
thesource_alphabet = []
source_bin_head = '0b'
for i in thesource:
    # Left 4 bits are tens place, right four bits are ones place
    if len(i) == 8:
        leftbits = i[:4]
        leftbin = source_bin_head + leftbits
        leftdec = int(leftbin, 2)
        rightbits = i[4:]
        rightbin = source_bin_head + rightbits
        rightdec = int(rightbin, 2)
        source_dec = (leftdec * 10) + rightdec
    else:
        source_bin = source_bin_head + i
        source_dec = int(source_bin, 2)
    source_hex = hex(source_dec)
    if source_dec < 27:
        source_alphabet = list(string.ascii_uppercase)[source_dec-1]
    else:
        source_alphabet = 'n/a'
    print(f'(0b{i}): dec({source_dec}) alphabet({source_alphabet}) ascii({ascii(chr(source_dec))}) hex({source_hex})')
    thesource_dec.append(source_dec)
    thesource_alphabet.append(source_alphabet)

# TESTING ONLY
# thesource_dec = [11, 6, 10, 7, 12, 4, 13, 3, 8, 1, 9, 5, 2]
#
# THERE IS SOMETHING IN THE INNER LOOP PERHAPS NOT FUNCTIONING PROPERLY
#
# rotate the sequence by one position per loop
print(f'First_letters_nth_word || Last_letters_nth_word || Sentence_nth_char || SentenceRev_nth_char\n{"*"*90}')
for source_rotate in range(len(thesource_dec)):
    thesource_dec = thesource_dec[source_rotate:] + thesource_dec[:source_rotate]
    #print(f'\ntesting with sequence+{source_rotate}: {thesource_dec}')
    key_letters = []
    key_letters_rev = []
    key_sum = 0
    first_letters = []
    last_letters = []
    sentence_letters = []
    sentence_letters_rev = []
    # get the n[0]th letter in the text, then skip n[1], then skip n[2]...
    for i in thesource_dec:
        key_letters.append(source[key_sum + i])
        key_sum += i
    key_sum = 0
    for i in thesource_dec:
        key_letters_rev.append(source[-key_sum - i])
        key_sum += i
    for idx, i in enumerate(sentences):
        if idx > len(thesource):
            continue
        # get each sentence's individual words
        sentence_words = i.strip().split(" ")
        #print(sentence_words)
        # get the nth word or letter from the idx sentence as dictated by the sequence
        try:
            which_word = sentence_words[thesource_dec[idx]]
            first_letters.append(which_word[0])
            last_letters.append(which_word[-1])
        except:  # fill with underscores for errors
            first_letters.append('_')
            last_letters.append('_')
        try:
            which_letter = i[thesource_dec[idx]]
            sentence_letters.append(which_letter)
            rev = list(i)
            rev.reverse()
            which_letter_rev = rev[thesource_dec[idx]]
            sentence_letters_rev.append(which_letter_rev)
        except:  # fill with underscores for errors
            sentence_letters.append('_')
            sentence_letters_rev.append('_')
    a = "".join(first_letters)
    b = "".join(last_letters)
    c = "".join(sentence_letters)
    d = "".join(sentence_letters_rev)
    e = "".join(key_letters)
    f = "".join(key_letters_rev)
    print(f'{a} || {b} || {c} || {d} || {e} || {f} ||')

